# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/taulukko/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([08277d6c ...](https://git.sr.ht/~sthagen/taulukko/blob/default/etc/sbom/cdx.json.sha256 "sha256:08277d6cfa6bd3564414005860d30481f390ce2785c78415b738af65e52243c3")).
<!--[[[end]]] (checksum: c1c4577131e399f31fbee71c4d2d3289)-->
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
| Name                                                                 | Version                                                    | License                                                 | Author                                                                                | Description (from packaging data)                                                                               |
|:---------------------------------------------------------------------|:-----------------------------------------------------------|:--------------------------------------------------------|:--------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
| [DataProperty](https://github.com/thombashi/DataProperty)            | [1.0.1](https://pypi.org/project/DataProperty/1.0.1/)      | MIT License                                             | Tsuyoshi Hombashi                                                                     | Python library for extract property from data.                                                                  |
| [attrs](https://www.attrs.org/en/stable/changelog.html)              | [23.1.0](https://pypi.org/project/attrs/23.1.0/)           | MIT License                                             | Hynek Schlawack <hs@ox.cx>                                                            | Classes Without Boilerplate                                                                                     |
| [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/) | [4.12.2](https://pypi.org/project/beautifulsoup4/4.12.2/)  | MIT License                                             | Leonard Richardson <leonardr@segfault.org>                                            | Screen-scraping library                                                                                         |
| [chardet](https://github.com/chardet/chardet)                        | [5.2.0](https://pypi.org/project/chardet/5.2.0/)           | GNU Lesser General Public License v2 or later (LGPLv2+) | Mark Pilgrim                                                                          | Universal encoding detector for Python 3                                                                        |
| [click](https://palletsprojects.com/p/click/)                        | [8.1.6](https://pypi.org/project/click/8.1.6/)             | BSD License                                             | Pallets <contact@palletsprojects.com>                                                 | Composable command line interface toolkit                                                                       |
| [jsonschema](https://github.com/python-jsonschema/jsonschema)        | [4.19.0](https://pypi.org/project/jsonschema/4.19.0/)      | MIT License                                             | Julian Berman                                                                         | An implementation of JSON Schema validation for Python                                                          |
| [mbstrdecoder](https://github.com/thombashi/mbstrdecoder)            | [1.1.3](https://pypi.org/project/mbstrdecoder/1.1.3/)      | MIT License                                             | Tsuyoshi Hombashi                                                                     | mbstrdecoder is a Python library for multi-byte character string decoder                                        |
| [path](https://github.com/jaraco/path)                               | [16.7.1](https://pypi.org/project/path/16.7.1/)            | MIT License                                             | Jason Orendorff                                                                       | A module wrapper for os.path                                                                                    |
| [pathvalidate](https://github.com/thombashi/pathvalidate)            | [3.1.0](https://pypi.org/project/pathvalidate/3.1.0/)      | MIT License                                             | Tsuyoshi Hombashi                                                                     | pathvalidate is a Python library to sanitize/validate a string such as filenames/file-paths/etc.                |
| [setuptools](https://github.com/pypa/setuptools)                     | [68.2.2](https://pypi.org/project/setuptools/68.2.2/)      | MIT License                                             | Python Packaging Authority                                                            | Easily download, build, install, upgrade, and uninstall Python packages                                         |
| [soupsieve](https://github.com/facelessuser/soupsieve)               | [2.4.1](https://pypi.org/project/soupsieve/2.4.1/)         | MIT License                                             | Isaac Muse <Isaac.Muse@gmail.com>                                                     | A modern CSS selector implementation for Beautiful Soup.                                                        |
| [tabledata](https://github.com/thombashi/tabledata)                  | [1.3.1](https://pypi.org/project/tabledata/1.3.1/)         | MIT License                                             | Tsuyoshi Hombashi                                                                     | tabledata is a Python library to represent tabular data. Used for pytablewriter/pytablereader/SimpleSQLite/etc. |
| [tcolorpy](https://github.com/thombashi/tcolorpy)                    | [0.1.3](https://pypi.org/project/tcolorpy/0.1.3/)          | MIT License                                             | Tsuyoshi Hombashi                                                                     | tcolopy is a Python library to apply true color for terminal text.                                              |
| [typepy](https://github.com/thombashi/typepy)                        | [1.3.2](https://pypi.org/project/typepy/1.3.2/)            | MIT License                                             | Tsuyoshi Hombashi                                                                     | typepy is a Python library for variable type checker/validator/converter at a run time.                         |
| [typing_extensions](https://github.com/python/typing_extensions)     | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/) | Python Software Foundation License                      | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+                                                          |
<!--[[[end]]] (checksum: 3f62438782a0e9f0a1a29d6f95e846d7)-->

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
