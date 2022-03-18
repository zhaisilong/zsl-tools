# Read The Docs

## Sphinx

Sphinx 是一个基于 Python 的文档生成项目，最早只是用来生成 Python 官方文档，随着工具的完善， 越来越多的知名的项目也用他来生成文档，甚至完全可以用他来写书采用 `reStructuredText` 作为文档写作语言, 不过也可以通过模块支持其他格式，待会我会介绍怎样支持`MarkDown`格式。

Sphinx 提供的 `API documentation` 生成器称为 `sphinx-apidoc`

```bash
pip install sphinx sphinx-autobuild sphinx_rtd_theme
cd path_to_your_repo
sphinx-quickstart
```

```bash
Separate source and build directories (y/n) [n]:y  
Project name: scrapy-cookbook  
Author name(s): Xiong Neng  
Project version []: 0.2  
Project release [1.0]: 0.2.2  
Project language [en]: zh_CN
```

编译以及本地服务器托管

```bash
make html
cd build/html
python3 -m http.server 8000
# 清除编译输出，会删除 build 下的文件
make clean
# 重新编译
make html
```

### 使用主题修改 `conf.py`

```python
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

### 运行构建

*-b* 选择了生成器，Sphinx将会生成HTML格式

```bash
sphinx-build -b html sourcedir builddir
```

因为 `sphinx-quickstart` 生成了 `Makefile` 和 `make.bat` 文件，这些文件能够减少不少工作：有了它们你就可以运行

```bash
make html
```

### 配置 Sphinx 项目以获得 Markdown 支持

[recommonmark — Recommonmark 0.7.1 documentation](https://recommonmark.readthedocs.io/en/latest/index.html)

```bash
pip install recommonmark
# 然后修改 conf.py
extensions = ['recommonmark']
```

支持 markdown 的表格，表格在本地可行但是无法**托管到 Read the docs 上**。因此，这里推介大家学一下 reStructure

```bash
pip install sphinx-markdown-tables
# 然后修改 conf.py
extensions = [
'sphinx_markdown_tables',
]
```

目前不支持 markdown 的数学公式

## Markdown to reStructuredText with Pandoc 

如果你熟悉 Markdown 写作。你可以使用 Pandoc 将成稿的 Markdown 转化为 reStructuredText

```shell
sudo apt install pandoc
pandoc -s test.md -o test.rst
```

## FAQ

用 Read The Docs build 时 pdf 生成错误，在 `config.py` 添加

```python
latex_elements={# The paper size ('letterpaper' or 'a4paper').
'papersize':'a4paper',# The font size ('10pt', '11pt' or '12pt').
'pointsize':'12pt','classoptions':',oneside','babel':'',#必須
'inputenc':'',#必須
'utf8extra':'',#必須
# Additional stuff for the LaTeX preamble.
'preamble': r"""
\usepackage{xeCJK}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
\setCJKmainfont{WenQuanYi Micro Hei}
\setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
\setCJKfamilyfont{song}{WenQuanYi Micro Hei}
\setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
"""}
```

## See also

- [使用 ReadtheDocs 托管文档](https://www.xncoding.com/2017/01/22/fullstack/readthedoc.html)