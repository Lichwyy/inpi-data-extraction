from bs4 import BeautifulSoup
import re
from models.models import Patent, Classification, Priority, InternationalApplication, Party

class INPIParser:
    
    def parser_cod_pedido(self, html):
        return re.findall(r"CodPedido=(\d+)", html)
    
 

    def extract_inid_text(self, soup, inid_code):
        pattern = re.compile(rf"\({inid_code}\)")
        tag = soup.find(string=pattern)
        if not tag:
            return None
        return re.sub(r"\s+", " ",tag.parent.parent.parent.get_text(" ", strip=True))
    
    def parser_detail(self, html: str) -> Patent:
        soup = BeautifulSoup(html, "html.parser")
        patent = Patent(
            publication_number=self._parse_inid(soup, "11"),
            application_number=self._parse_inid(soup, "21"),
            filing_date=self._parse_inid(soup, "22"),
            publication_date=self._parse_inid(soup, "43"),
            examination_publication_date=self._parse_inid(soup, "47"),
            title=self._parse_inid(soup, "54"),
            abstract=self._parse_inid(soup, "57"),
            national_phase_start_date=self._parse_inid(soup, "85")
        )
        patent.priorities.append(self._parse_priorities(soup))
        patent.classifications.extend(self._parse_classifications(soup))
        patent.international_applications.extend(self._parse_international_applications(soup))
        patent.parties.extend(list(self._parse_parties(soup)))
        patent.parties.extend(list(self._parse_inventors(soup)))
        return patent

    def _parse_inid(self, soup, code:str):
        text = self.extract_inid_text(soup, code)
        if not text:
            return None
        return re.sub(rf"\({code}\)\s*[^:]*:\s*", "", text).strip()
    
    def _parse_inventors(self, soup):
        text = self.extract_inid_text(soup, "72")
        if not text:
            return None
        text = re.sub(r"\(72\)", "", text)
        return [i.strip() for i in text.split(";") if i.strip()]
    

    def _parse_priorities(self, soup):
        text = self.extract_inid_text(soup, "30")
        if text == None:
            return None
        pattern = r"\(32\)\s*Data:\s*([A-Z\s]+?)\s+([\d/,]+)\s+(\d{2}/\d{2}/\d{4})"
        match = re.search(pattern, text)
        if match:
            text = list(match.groups())
        return Priority(
               number=text[1].strip(),
               date=text[2].strip(),
               country=text[0].strip()
                    )
        
        
    def _parse_classifications(self, soup):
        ipc = self.extract_inid_text(soup, "51")
        cpc = self.extract_inid_text(soup, "52")

        if ipc != None:
            for cls in self._parse_classifications_text(ipc, "IPC", True):
                yield cls
        if cpc != None:
            for cls in self._parse_classifications_text(cpc, "CPC", False):
                yield cls

    def _parse_classifications_text(self, text:str, system:str, has_year:bool):
        ipc_pattern = re.compile(
                r"""
                (?P<code>[A-Z]\d{2}[A-Z]?\s\d+/\d+) 
                (?:\s*;\s*|\s+)                      
                \1                                    
                \s*\(
                (?P<year>\d{4}\.\d{2})                
                \s*\)
                \s*
                (?P<description>.*?)
                (?=
                    [A-Z]\d{2}[A-Z]?\s\d+/\d+          
                    |$                                
                )
                """,
                re.VERBOSE | re.DOTALL
            )
        cpc_pattern = re.compile(
                    r"""
                    (?P<code>[A-Z]\d{2}[A-Z]?\s\d+/\d+)   
                    (?:\s*;\s*|\s+)                         
                    \1                                     
                    \s*
                    (?P<description>.*?)
                    (?=
                        [A-Z]\d{2}[A-Z]?\s\d+/\d+           
                        |$                                   
                    )
                    """,
                    re.VERBOSE | re.DOTALL
                )

        pattern = ipc_pattern if has_year else cpc_pattern
        for match in pattern.finditer(text):
            yield Classification(
                    system=system,
                    code=match.group("code"),
                    year=match.group("year") if has_year else None,
                    description=match.group("description").strip()
                )

    def _parse_international_applications(self, soup):
        pct = self.extract_inid_text(soup, "86")
        wo = self.extract_inid_text(soup, "87")
        pattern = re.compile(
                    r"""
                    \(\d+\)\s*                          
                    (?P<type>[A-Z.]+)\s+Número:\s*     
                    (?P<number>\S+)\s+                  
                    Data:\s*(?P<date>\d{2}/\d{2}/\d{4}) 
                    """,
                    re.VERBOSE
                )
        text = " ".join(filter(None, [pct, wo]))
        if text == " " or text == None:
            return None
        for match in re.finditer(pattern,text):
            if match.group(1).strip() == "PCT":
                yield InternationalApplication(
                    application_type=match.group(1),
                    number=match.group(2),
                    date=match.group(3),
                    authority="INPI"
                )
            elif match.group(1).strip() == "W.O.":
                yield InternationalApplication(
                    application_type=match.group(1),
                    number=match.group(2),
                    date=match.group(3),
                    authority="WIPO"
                )

    def _parse_parties(self, soup):
        depositors = self.extract_inid_text(soup, "71")
        assignee = self.extract_inid_text(soup, "73")
        agent = self.extract_inid_text(soup, "74")
        text = " ".join(filter(None, [depositors, assignee, agent]))
        if text == " " or text == None:
            return None
        pattern = r"\(\d+\)\s+([^:]+):\s+([^(]+)(?:\s+\(([^)]+)\))?"

        matches = re.findall(pattern, text)

        for match in matches:
            role = match[0].strip().split()[2] if match[0] else None
            name = match[1].strip() if match[1] else None
            country = match[2].strip() if match[2] else None
            yield Party(
                name=name,
                role=role,
                country=country
                )
        
    def _parse_inventors(self, soup):
        text = self.extract_inid_text(soup, "72")
        if text == None:
            return 
        pattern = r"\(72\)\s+Nome do Inventor:\s"

        text = re.sub(pattern, "", text).strip().split(" / ")
        for inventor in text:
            yield Party(
                name=inventor,
                role="Inventor",
                country=None
            )
