# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([5d2d01b9 ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:5d2d01b993f76d66a26c3af0525a89246546117740d75c712cd1985b961af9e6")).
<!--[[[end]]] (checksum: 12a84b4d89384d72913bc89b1be17b0d)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                        | Version                                                  | License     | Author            | Description (from packaging data)                                                                                                                                                                                                                                  |
|:------------------------------------------------------------|:---------------------------------------------------------|:------------|:------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [pytablereader](https://github.com/thombashi/pytablereader) | [0.31.3](https://pypi.org/project/pytablereader/0.31.3/) | MIT License | Tsuyoshi Hombashi | pytablereader is a Python library to load structured table data from files/strings/URL with various data format: CSV / Excel / Google-Sheets / HTML / JSON / LDJSON / LTSV / Markdown / SQLite / TSV.                                                              |
| [pytablewriter](https://github.com/thombashi/pytablewriter) | [0.64.2](https://pypi.org/project/pytablewriter/0.64.2/) | MIT License | Tsuyoshi Hombashi | pytablewriter is a Python library to write a table in various formats: AsciiDoc / CSV / Elasticsearch / HTML / JavaScript / JSON / LaTeX / LDJSON / LTSV / Markdown / MediaWiki / NumPy / Excel / Pandas / Python / reStructuredText / SQLite / TOML / TSV / YAML. |
| [typer](https://github.com/tiangolo/typer)                  | [0.7.0](https://pypi.org/project/typer/0.7.0/)           | MIT License | Sebastián Ramírez | Typer, build great CLIs. Easy to code. Based on Python type hints.                                                                                                                                                                                                 |
<!--[[[end]]] (checksum: 86332e1c132409d36473133b3f626344)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/) | BSD License | Armin Ronacher | Composable command line interface toolkit |
<!--[[[end]]] (checksum: dc3a866a7aa3332404bde3da87727cb9)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
pytablereader==0.31.3
  - beautifulsoup4 [required: >=4.5.3,<5, installed: 4.11.1]
    - soupsieve [required: >1.2, installed: 2.3.2.post1]
  - DataProperty [required: >=0.54.2,<2, installed: 0.55.0]
    - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
      - chardet [required: >=3.0.4,<6, installed: 5.0.0]
    - typepy [required: >=1.2.0,<2, installed: 1.3.0]
      - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
        - chardet [required: >=3.0.4,<6, installed: 5.0.0]
  - jsonschema [required: >=2.5.1,<5, installed: 4.17.1]
    - attrs [required: >=17.4.0, installed: 22.1.0]
    - pyrsistent [required: >=0.14.0,!=0.17.2,!=0.17.1,!=0.17.0, installed: 0.19.2]
  - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
    - chardet [required: >=3.0.4,<6, installed: 5.0.0]
  - path [required: >=13,<17, installed: 16.5.0]
  - pathvalidate [required: >=2.3.0,<3, installed: 2.5.2]
  - setuptools [required: >=38.3.0, installed: 65.6.3]
  - tabledata [required: >=1.1.1,<2, installed: 1.3.0]
    - DataProperty [required: >=0.53.0,<2, installed: 0.55.0]
      - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
        - chardet [required: >=3.0.4,<6, installed: 5.0.0]
      - typepy [required: >=1.2.0,<2, installed: 1.3.0]
        - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
          - chardet [required: >=3.0.4,<6, installed: 5.0.0]
    - typepy [required: >=1.2.0,<2, installed: 1.3.0]
      - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
        - chardet [required: >=3.0.4,<6, installed: 5.0.0]
  - typepy [required: >=1.2.0,<2, installed: 1.3.0]
    - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
      - chardet [required: >=3.0.4,<6, installed: 5.0.0]
pytablewriter==0.64.2
  - DataProperty [required: >=0.55.0,<2, installed: 0.55.0]
    - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
      - chardet [required: >=3.0.4,<6, installed: 5.0.0]
    - typepy [required: >=1.2.0,<2, installed: 1.3.0]
      - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
        - chardet [required: >=3.0.4,<6, installed: 5.0.0]
  - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
    - chardet [required: >=3.0.4,<6, installed: 5.0.0]
  - pathvalidate [required: >=2.3.0,<3, installed: 2.5.2]
  - setuptools [required: >=38.3.0, installed: 65.6.3]
  - tabledata [required: >=1.3.0,<2, installed: 1.3.0]
    - DataProperty [required: >=0.53.0,<2, installed: 0.55.0]
      - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
        - chardet [required: >=3.0.4,<6, installed: 5.0.0]
      - typepy [required: >=1.2.0,<2, installed: 1.3.0]
        - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
          - chardet [required: >=3.0.4,<6, installed: 5.0.0]
    - typepy [required: >=1.2.0,<2, installed: 1.3.0]
      - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
        - chardet [required: >=3.0.4,<6, installed: 5.0.0]
  - tcolorpy [required: >=0.0.5,<1, installed: 0.1.2]
  - typepy [required: >=1.2.0,<2, installed: 1.3.0]
    - mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.1]
      - chardet [required: >=3.0.4,<6, installed: 5.0.0]
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: f5fb193daf47c6862a2aa4c2fb4cd76a)-->
