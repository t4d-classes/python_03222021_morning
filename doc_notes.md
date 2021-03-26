# Documenting Python Code

There are numerous tools available for documenting Python code. Documenting includes both the adding of structured comments to code as well as generating easy to use documentation.

A popular and complex documentation generation tool is Sphinx. It uses Restructured Text [https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). Sphinx is not easy to setup. It includes a full configuration and build system. While it does a great job, it is often overkill for generating documention for a project.

For this introductory course, three simpler tools will be explored. Each of these tools allows for docstring-based inline code documentation to be viewed with one command.

- help - used within the Python REPL environment
- pydoc - a Standard Library module
- pdoc - 3rd party package

## Help

Start a REPL session.

```bash
python
```

Import the module for which help is needed.

```python
import models.history
```

View the help documentation.

```python
help(models.history)
```

## Pydoc

Start the PyDoc web server that serves up the generated documentation. Open the web site in your browser.

```bash
python -m pydoc -b
```

## PDoc

Install the `pdoc` package ([https://pdoc.dev/docs/](https://pdoc.dev/docs/)).

```bash
python -m pip install pdoc
```

Use a glob to find all Python files, generate documentation, and display it via a web application.

```bash
pdoc ./**/*.py
```

Use the numpy documentation style: ([https://numpydoc.readthedocs.io/en/latest/format.html](https://numpydoc.readthedocs.io/en/latest/format.html))

```bash
pdoc --docformat numpy ./**/*.py
```

Use the Google documentation style: (inside document: [https://google.github.io/styleguide/pyguide.html](https://google.github.io/styleguide/pyguide.html))

```bash
pdoc --docformat google ./**/*.py
```

Output the documentation to an HTML folder instead of running a web server.

```bash
pdoc -o ./html --docformat google ./**/*.py
```

## Python Style Guide

For reference, here are some helpful links to style guides which provide some best practices on documenting code.

- Python Style Guide - [https://pep8.org/](https://pep8.org/)
- Guidance of Python DocStrings - [https://www.python.org/dev/peps/pep-0257/](https://www.python.org/dev/peps/pep-0257/)
- Google's Python Style Guide - [https://google.github.io/styleguide/pyguide.html](https://google.github.io/styleguide/pyguide.html)
- Real Python Commenting Guide - [https://realpython.com/python-comments-guide/](https://realpython.com/python-comments-guide/)
