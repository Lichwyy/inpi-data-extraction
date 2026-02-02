from typing import List, Optional
from datetime import date

class Patent:
    """
    Core entity representing a patent application or publication.
    This object should be stable and independent of data source (INPI, WIPO, etc).
    """

    def __init__(
        self,
        publication_number: Optional[str] = None,   # INID (11)
        application_number: Optional[str] = None,   # INID (21)
        filing_date: Optional[date] = None,         # INID (22)
        publication_date: Optional[date] = None,    # INID (43)
        examination_publication_date: Optional[date] = None,  # INID (47)
        title: Optional[str] = None,                # INID (54)
        abstract: Optional[str] = None,             # INID (57)
        country: Optional[str] = "BR",              # # The data only comes from inpi, so for now every patent is going to be BR
        source: Optional[str] = "INPI",               # data source
        national_phase_start_date: Optional[date] = None  # INID (85)
    ):
        self.publication_number = publication_number
        self.application_number = application_number
        self.filing_date = filing_date
        self.publication_date = publication_date
        self.examination_publication_date = examination_publication_date
        self.title = title
        self.abstract = abstract
        self.country = country
        self.source = source
        self.national_phase_start_date = national_phase_start_date
        

        # Relations
        self.priorities: List[Priority] = []
        self.classifications: List[Classification] = []
        self.international_applications: List[InternationalApplication] = []
        self.parties: List[Party] = [] 


class Priority:
    """
    Represents a priority claim of a patent.
    Covers INID (33) - (Country), (31) - (Number), (32) - (Date)
    """

    def __init__(
        self,
        number: Optional[str] = None,
        date: Optional[date] = None,
        country: Optional[str] = None 
    ):
        self.number = number
        self.date = date
        self.country = country

class Classification:
    """
    Represents a patent classification (IPC, CPC, national, etc).
    """

    def __init__(
        self,
        system: Optional[str] = None,        # IPC, CPC, NCL, etc
        code: Optional[str] = None,
        year: Optional[str] = None,
        description: Optional[str] = None
    ):
        self.system = system
        self.code = code
        self.year = year
        self.description = description


class InternationalApplication:
    """
    Represents an international filing or publication (PCT, WO, etc).
    Covers INID (86), (87) and future equivalents.
    """

    def __init__(
        self,
        application_type: Optional[str] = None,  # PCT, WO, EP, etc
        number: Optional[str] = None,
        date: Optional[date] = None,
        authority: Optional[str] = None          # WIPO, EPO, etc
    ):
        self.application_type = application_type
        self.number = number
        self.date = date
        self.authority = authority


class Party:
    """
    Represents a person or organization related to a patent.
    Used for depositors, inventors, assignees, agents, etc.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        country: Optional[str] = None,
        role: Optional[str] = None 
    ):
        self.name = name
        self.country = country
        self.role = role
