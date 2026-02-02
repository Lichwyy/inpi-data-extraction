# inpi-data-extraction
Extrai dados de patentes a partir da busca pública do INPI (Brasil) usando Python.

## Visão geral
O fluxo principal lê números de pedido em `patents_ids/patents_ids.txt`, autentica no INPI usando credenciais via variáveis de ambiente e busca os detalhes para cada pedido. O parser converte o HTML em objetos de domínio (Patent, Priority, Classification, InternationalApplication, Party) e o módulo de persistência acompanha quais números já foram processados.

## Requisitos
- Python 3.13 (o Pipfile está configurado para essa versão)
- Variáveis de ambiente `login` e `pass` com credenciais válidas do INPI
- Pipenv (recomendado para reproduzir o ambiente)

## Instalação
```bash
pipenv install
```

## Execução rápida
O script principal usa a lista de números de pedido em `patents_ids/patents_ids.txt`.
```bash
pipenv run python main.py
```

## Estrutura do projeto
- `main.py`: orquestra busca, reautenticação e parsing.
- `correto/`: cliente HTTP, busca, detalhes e parser do HTML do INPI.
- `models/`: modelos de dados para patentes e relacionamentos.
- `persistence/`: controle de IDs enviados/não enviados.
- `patents_ids/`: entrada e saída de IDs processados.
- `utils/`: utilitários para leitura/escrita de arquivos e impressão de objetos.

## Componentes principais

### main.py
- `reauthenticate(response, inpi_search, number)`: reautentica se a sessão expirar e repete a busca.
```python
html = inpisearch.search_by_number(numero)
reauthenticate(html, inpisearch, numero)
```
Se precisar do HTML após reautenticação, execute a busca novamente com `search_by_number`.

### correto/inpi_client.py
- `INPIClient()`: cria sessão HTTP e carrega `login`/`pass` do ambiente.
- `authenticate()`: realiza login no INPI para liberar requisições.
- `expired_session(response: str) -> bool`: detecta sessão expirada.

### correto/inpi_search.py
- `INPISearch.search_by_number(numero: str) -> str`: busca pelo número do pedido e retorna HTML.

### correto/inpi_detail_service.py
- `INPIDetailService.get_data(codPedido: str) -> str`: obtém HTML detalhado.

### correto/inpi_parser.py
- `parser_cod_pedido(html: str) -> list[str]`: extrai `CodPedido` do HTML de busca.
- `extract_inid_text(soup, inid_code) -> str | None`: localiza texto de um código INID.
- `parser_detail(html: str) -> Patent`: transforma o HTML detalhado em um `Patent`.
- Métodos privados (_parse_inid, _parse_priorities, _parse_classifications, _parse_international_applications, _parse_parties, _parse_inventors) processam cada bloco específico.

### persistence/persistence.py
- `Persistence()`: prepara arquivos `ids_sent.txt` e `ids_not_sent.txt`.
- `is_sent(number: str) -> bool`: verifica se o número já foi enviado.
- `mark_sent(number: str)`: marca como enviado e atualiza os arquivos.
- `mark_not_sent(number: str)`: marca como não enviado.

### utils/file_manager.py
- `FileManager.read_lines(path: Path) -> list[str]`: lê linhas de um arquivo.
- `FileManager.write_lines(path: Path, lines: list[str])`: sobrescreve linhas.
- `FileManager.append_line(path: Path, line: str)`: adiciona linha no fim.

## Observações
- O código depende das credenciais do INPI para funcionar corretamente.
- Não há suite de testes configurada no repositório atualmente.
