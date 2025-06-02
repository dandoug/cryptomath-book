# Cryptological Mathematics Exercises

I created this project while I was reading through ***Cryptological Mathematics*** by Robert Edward Leward (2000).  At the same time, I was eager to learn about using [MathJax](https://www.mathjax.org/) and [Jupyter Book](https://jupyterbook.org/en/stable/intro.html).

## Setup

The project is built and tested locally on macOS Sequoia 15.3.2 using Python 3.11.11 (installed from pyenv 2.5.3, which in turn was installed with homebrew), but I try my best to avoid version and operating system dependencies wherever possible.

### Python Environment

From the project root, execute this (adjust for your platform)

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```

I'm working in and using Jetbrins IDEs (DataSpell and PyCharm), but you should be able to use whatever works best for you.

## Building the Python Book

Once the environment is installed and activated, you should be able to build the book using

```bash
jupyter-book clean  .
jupyter-book build  .
```

The book will be available in the `_build/html/index.html` file after building.

## Running the github workflow locally

The local-only `.secrets` file should have a single line, `GITHUB_TOKEN=...` with the PAT token for committing the gh-pages update.

```bash
act -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest --secret-file .secrets
```

