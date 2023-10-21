# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/taulukko/blob/default/sbom/cdx.json) with SHA256 checksum ([a790d962 ...](https://git.sr.ht/~sthagen/taulukko/blob/default/sbom/cdx.json.sha256 "sha256:a790d96252b19314483d4dcbaf3486ab8748c1a7f96b39de6b9ec3965938fd81")).
<!--[[[end]]] (checksum: b3b2191065ddafaffbf3c30300b89330)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                        | Version                                                  | License     | Author            | Description (from packaging data)                                                                                                                                                                                                                                  |
|:------------------------------------------------------------|:---------------------------------------------------------|:------------|:------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [pytablereader](https://github.com/thombashi/pytablereader) | [0.31.4](https://pypi.org/project/pytablereader/0.31.4/) | MIT License | Tsuyoshi Hombashi | pytablereader is a Python library to load structured table data from files/strings/URL with various data format: CSV / Excel / Google-Sheets / HTML / JSON / LDJSON / LTSV / Markdown / SQLite / TSV.                                                              |
| [pytablewriter](https://github.com/thombashi/pytablewriter) | [1.2.0](https://pypi.org/project/pytablewriter/1.2.0/)   | MIT License | Tsuyoshi Hombashi | pytablewriter is a Python library to write a table in various formats: AsciiDoc / CSV / Elasticsearch / HTML / JavaScript / JSON / LaTeX / LDJSON / LTSV / Markdown / MediaWiki / NumPy / Excel / Pandas / Python / reStructuredText / SQLite / TOML / TSV / YAML. |
| [typer](https://github.com/tiangolo/typer)                  | [0.9.0](https://pypi.org/project/typer/0.9.0/)           | MIT License | Sebastián Ramírez | Typer, build great CLIs. Easy to code. Based on Python type hints.                                                                                                                                                                                                 |
<!--[[[end]]] (checksum: 86eef61ebc4c9efd13e3c854268e2613)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name | Version | License | Author | Description (from packaging data) |
|:-----|:--------|:--------|:-------|:----------------------------------|
<!--[[[end]]] (checksum: 8a87b89207db0be2864af66f9266660c)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
pytablereader==0.31.4
├── beautifulsoup4 [required: >=4.5.3,<5, installed: 4.12.2]
│   └── soupsieve [required: >1.2, installed: 2.4.1]
├── DataProperty [required: >=0.54.2,<2, installed: 1.0.1]
│   ├── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│   │   └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
│   └── typepy [required: >=1.2.0,<2, installed: 1.3.2]
│       └── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│           └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
├── jsonschema [required: >=2.5.1,<5, installed: 4.19.0]
│   ├── attrs [required: >=22.2.0, installed: 23.1.0]
│   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.7.1]
│   │   └── referencing [required: >=0.28.0, installed: 0.30.2]
│   │       ├── attrs [required: >=22.2.0, installed: 23.1.0]
│   │       └── rpds-py [required: >=0.7.0, installed: 0.9.2]
│   ├── referencing [required: >=0.28.4, installed: 0.30.2]
│   │   ├── attrs [required: >=22.2.0, installed: 23.1.0]
│   │   └── rpds-py [required: >=0.7.0, installed: 0.9.2]
│   └── rpds-py [required: >=0.7.1, installed: 0.9.2]
├── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│   └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
├── path [required: >=13,<17, installed: 16.7.1]
├── pathvalidate [required: >=2.5.2,<4, installed: 3.1.0]
├── setuptools [required: >=38.3.0, installed: 68.2.2]
├── tabledata [required: >=1.1.1,<2, installed: 1.3.1]
│   ├── DataProperty [required: >=0.54.2,<2, installed: 1.0.1]
│   │   ├── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│   │   │   └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
│   │   └── typepy [required: >=1.2.0,<2, installed: 1.3.2]
│   │       └── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│   │           └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
│   └── typepy [required: >=1.2.0,<2, installed: 1.3.2]
│       └── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│           └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
└── typepy [required: >=1.2.0,<2, installed: 1.3.2]
    └── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
        └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
pytablewriter==1.2.0
├── DataProperty [required: >=1.0.1,<2, installed: 1.0.1]
│   ├── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│   │   └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
│   └── typepy [required: >=1.2.0,<2, installed: 1.3.2]
│       └── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│           └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
├── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│   └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
├── pathvalidate [required: >=2.3.0,<4, installed: 3.1.0]
├── setuptools [required: >=38.3.0, installed: 68.2.2]
├── tabledata [required: >=1.3.1,<2, installed: 1.3.1]
│   ├── DataProperty [required: >=0.54.2,<2, installed: 1.0.1]
│   │   ├── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│   │   │   └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
│   │   └── typepy [required: >=1.2.0,<2, installed: 1.3.2]
│   │       └── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│   │           └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
│   └── typepy [required: >=1.2.0,<2, installed: 1.3.2]
│       └── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
│           └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
├── tcolorpy [required: >=0.0.5,<1, installed: 0.1.3]
└── typepy [required: >=1.3.2,<2, installed: 1.3.2]
    └── mbstrdecoder [required: >=1.0.0,<2, installed: 1.1.3]
        └── chardet [required: >=3.0.4,<6, installed: 5.2.0]
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 615ee470bfce691d072a4e9f7b1a78f9)-->
