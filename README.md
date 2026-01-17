# inpi-data-extraction
Este repositório extrai dados de patentes da base do INPI usando Python.

## Requisitos
- Python 3.13
- Variáveis de ambiente `login` e `pass` com credenciais válidas do INPI
- Pipenv (opcional, recomendado)

## Instalação
```bash
pipenv install
```

## Execução rápida
O fluxo principal lê IDs do arquivo `patents_ids/patents_ids.txt` e processa cada patente:
```bash
pipenv run python main.py
```

## Seções do projeto
- `main.py`: fluxo principal de consulta e parsing.
- `inpi/`: cliente HTTP, busca, detalhe e parsing da resposta do INPI.
- `models/`: modelos de dados (Patent, Priority, Classification, InternationalApplication, Party).
- `persistence/`: controle de IDs enviados/não enviados.
- `patents_ids/`: arquivos de entrada e saída de IDs.
- `utils/`: utilitários para arquivos e impressão de objetos.

## Uso das funções

### main.py
- `reauthenticate(response, inpi_search, number)`: reautentica se a sessão expirou e repete a busca do número.
  ```python
  html = inpisearch.search_by_number(numero)
  reauthenticate(html, inpisearch, numero)
  updated_html = inpisearch.search_by_number(numero)
  ```
  A função não retorna o HTML atualizado; se precisar do conteúdo após reautenticar, repita a busca e use o retorno.

### inpi/inpi_client.py
- `INPIClient()`: cria uma sessão e carrega `login`/`pass` do ambiente.
- `authenticate()`: autentica no INPI para liberar requisições.
  ```python
  client = INPIClient()
  client.authenticate()
  ```
- `expired_session(response: str) -> bool`: indica se a resposta aponta para sessão expirada.

### inpi/inpi_search.py
- `INPISearch.search_by_number(numero: str) -> str`: busca pelo número do pedido e retorna HTML.
  ```python
  search = INPISearch(client)
  html = search.search_by_number("BR102022000001")
  ```

### inpi/inpi_detail_service.py
- `INPIDetailService.get_data(codPedido: str) -> str`: obtém o HTML detalhado do pedido.
  ```python
  detail = INPIDetailService(client)
  html = detail.get_data("123456789")
  ```

### inpi/inpi_parser.py
- `parser_cod_pedido(html: str) -> list[str]`: extrai `CodPedido` do HTML de busca.
- `extract_inid_text(soup, inid_code) -> str | None`: localiza o texto de um código INID.
- `parser_detail(html: str) -> Patent`: parseia o HTML detalhado e retorna um `Patent` completo.
  ```python
  parser = INPIParser()
  codigos = parser.parser_cod_pedido(html_busca)
  patente = parser.parser_detail(html_detalhe)
  ```
- `_parse_inid(soup, code: str) -> str | None`: uso interno para extrair campos INID.
- `_parse_priorities(soup) -> Priority | None`: uso interno para prioridades (INID 30/31/32/33).
- `_parse_classifications(soup) -> Iterable[Classification]`: uso interno para IPC/CPC.
- `_parse_classifications_text(text, system, has_year) -> Iterable[Classification]`: uso interno por texto.
- `_parse_international_applications(soup) -> Iterable[InternationalApplication]`: uso interno para INID 86/87.
- `_parse_parties(soup) -> Iterable[Party]`: uso interno para depositantes/cessionários/representantes.
- `_parse_inventors(soup) -> Iterable[Party]`: uso interno para inventores (INID 72).

### persistence/persistence.py
- `Persistence()`: prepara arquivos `ids_sent.txt` e `ids_not_sent.txt` e carrega estados.
- `is_sent(number: str) -> bool`: verifica se o número já foi enviado.
- `is_not_sent(number: str) -> bool`: verifica se o número está marcado como não enviado.
- `mark_sent(number: str)`: marca como enviado e atualiza os arquivos.
- `mark_not_sent(number: str)`: marca como não enviado.
  ```python
  persistence = Persistence()
  if not persistence.is_sent(numero):
      persistence.mark_sent(numero)
  ```

### utils/file_manager.py
- `FileManager.read_lines(path: Path) -> list[str]`: lê linhas de um arquivo.
- `FileManager.write_lines(path: Path, lines: list[str])`: sobrescreve linhas no arquivo.
- `FileManager.append_line(path: Path, line: str)`: adiciona uma linha no fim.
  ```python
  lines = FileManager.read_lines(Path("patents_ids/patents_ids.txt"))
  FileManager.append_line(Path("patents_ids/ids_sent.txt"), "BR102022000001")
  ```

### utils/random.py
- `print_obj(obj)`: imprime campos principais de um objeto `Patent`.
- `print_ot(list)`: imprime nome/role/país para cada `Party`.
