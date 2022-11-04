### Hexlet tests and linter status:
[![Actions Status](https://github.com/algrince/python-project-51/workflows/hexlet-check/badge.svg)](https://github.com/algrince/python-project-51/actions)
[![Python CI](https://github.com/algrince/python-project-51/actions/workflows/pyci.yml/badge.svg)](https://github.com/algrince/python-project-51/actions/workflows/pyci.yml)
### Codeclimate:
[![Maintainability](https://api.codeclimate.com/v1/badges/148a999878818271cff2/maintainability)](https://codeclimate.com/github/algrince/python-project-51/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/148a999878818271cff2/test_coverage)](https://codeclimate.com/github/algrince/python-project-51/test_coverage)

## Description
Page-loader is a CLI utility that downloads pages from the Internet to indicated directory. If there is no directory indicated to the utility, the download will be made to the directory *os.getcwd()*.
The result of the download is: 
- A html file that contains the main page. 
- A sub-dictory that includes images *(.png, .jpeg)*, scripts *(.js)* and links *(.html, .css)* that are needed for opening the page. 
**Only the content that is placed in the same source as the main page is downloaded**
The progress is shown in the command line using logging and progress bar. When download in completed, the utility shows path to new generated file.

Please note that there was no publication made fo this package. 

## Instalation
1. Clone the repository:
`git clone https://github.com/algrince/python-project-51.git`
2. Go to the project folder:
`cd python-project-51`
3. Proceed to the setup:
`make setup`

### Naming and code changes
The utility names files using their links. Every symbol in the original url is replaced by '-', scheme is omitted. Every file is given its corresponded extension. If the original file has an extension that is not listed above, it will be saved with an extension fit for the file type from the list above. The sub-directory that conteins content is named after the main page with '_files' added.

Additionally, the utility makes changes in source html code of the main page. For every piece of content that is downloaded, its source *(src, href)* is replaced with path to the file.

## Usage
This utility can be used in command line and also it can be imported to other projects as dependecy.
#### CLI-utility
```
usage: page-loader [-h] [-o OUTPUT] PAGE

downloads a web page and saves it in a dictory

positional arguments:
  PAGE                  url of page to download

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        set path to the output directory (default: directory of launch)
```
#### Library
```
from page_loader import download

file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
print(file_path)  # => '/var/tmp/ru-hexlet-io-courses.html'
```

## Demo
The demo was made wuthout installing the package. The program was called using `poetry run`.
<details>
  <summary>Demo</summary>
<a href="https://asciinema.org/a/JdNzVxcBlsANaf6SLIJKhPtBW" target="_blank"><img src="https://asciinema.org/a/JdNzVxcBlsANaf6SLIJKhPtBW.svg" /></a>
</details>