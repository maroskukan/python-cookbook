# Python Cookbook
- [Python Cookbook](#python-cookbook)
  - [Introduction](#introduction)
    - [Use Cases](#use-cases)
    - [Characteristics](#characteristics)
  - [Documentation](#documentation)
  - [Environment](#environment)
    - [Local environment](#local-environment)
    - [Remote environment](#remote-environment)
  - [Virtual environment](#virtual-environment)
  - [Code Linting](#code-linting)

## Introduction

Python has a place amongs the world most popular programming languages due to its simplicity and easy of use.

### Use Cases
It is good choice for many different use cases including:
- **Web Development**
  - API (Flask, Bottle, Pyramid)
  - Websites (Django, TurboGeats, web2py)
  - App - CMS, ERP (Plone, django-cms, Mezzanine)
- **Data Science**
  - Big Data
  - Machine Learning
- **Education and Learning**
- **Scripting**
  - System Configuration
  - Application Extensibility

### Characteristics

Some key characteristics of this language include:
- **Unique Syntax**, uses significant whitespace as oppose to C-like Syntax (`{}`, `;`)
- **General purpose**, covers different use cases with its standard and 3rd party libraries
- **Multi-paradigm**, supports structured, functional and object-oriented programming
- **Interpreted**, language runtime handles the code translation as opposed to compiled language.
- **Garbage-collected**, data in memory that is no longer used needs to be cleaned. Python does this automatically
- **Dynamically-types**, no need to define the data type during variable initialization, as opposed to static typed languages


## Documentation

I have found the following websites very useful when learning Python.
- [Python Project](https://www.python.org/)
- [Pypi](https://pypi.python.org)
- [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- [Pylint](https://www.pylint.org/)
- [Python Playground](https://www.katacoda.com/courses/python/playground)
- [Jdoodle](https://www.jdoodle.com/)

## Environment

### Local environment

Python is very easy to install on your local machine. Whether you are running Windows, Linux or Mac OS, there is a good chance that it is available through package manager.

On Windows, you can leverage Chocolatey, an unoficial, but very pupular Windows package manager.
```powershell
choco install python3
```

On Ubuntu, you can leverage APT, the built in package manager.
```bash
apt-get install python3
```

On Mac, you can levelrage [HomeBrew](https://brew.sh/), the unoficial Mac OS package manager.
```bash
brew install python3
```

The Python package manager `pip` is also included with installation by default.

### Remote environment

If you do not want to install any binaries on your system, you can take advantage of [Katacoda](https://www.katacoda.com/) which provides an online [Python Playground](https://www.katacoda.com/courses/python/playground) inside what looks like a docker container.

## Virtual environment

Many python projects require some sort of upstream dependency such as package and library. It may happen that your underlying operating system and your project both require different version of same library, If you install version that your project requires, you may break some part of your OS that was dependent on older version.

To solve this issues, it is recommended to create and manage virtual environment for each project separately. This gives you ability to install packages that are independend from each other.

Virtualenvwrapper is popular tool for managing these envrionments, it can be installed through Python package manager from your main (system) environment.

```
pip install virtualenvwrapper
```

After you installed the package, you need to update your shell's configuration, in case of zsh, you need to add following lines to `.zshrc`.

```bash
# Virtualenvwrapper configuration
export WORKON_HOME=$HOME/.virtualenvs
source $HOME/.local/bin/virtualenvwrapper.sh
```

Once changed, don't forget to source the new configuration for changes to take effect.

```bash
. ~/.zshrc
```

Finally, create a sample virtual environment and install some packages.

```bash
mkvirtualenv vmware-avi
created virtual environment CPython3.8.5.final.0-64 in 234ms
  creator CPython3Posix(dest=/home/maros/.virtualenvs/vmware-avi, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/maros/.local/share/virtualenv)
    added seed packages: pip==21.0.1, setuptools==54.2.0, wheel==0.36.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
virtualenvwrapper.user_scripts creating /home/maros/.virtualenvs/vmware-avi/bin/predeactivate
virtualenvwrapper.user_scripts creating /home/maros/.virtualenvs/vmware-avi/bin/postdeactivate
virtualenvwrapper.user_scripts creating /home/maros/.virtualenvs/vmware-avi/bin/preactivate
virtualenvwrapper.user_scripts creating /home/maros/.virtualenvs/vmware-avi/bin/postactivate
virtualenvwrapper.user_scripts creating /home/maros/.virtualenvs/vmware-avi/bin/get_env_details

# Verify installed packages in this virtual environment
pip list
Package    Version
---------- -------
pip        21.0.1
setuptools 54.2.0
wheel      0.36.2

# Install package in this environment
pip install requests
Collecting requests
  Using cached requests-2.25.1-py2.py3-none-any.whl (61 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
Collecting idna<3,>=2.5
  Using cached idna-2.10-py2.py3-none-any.whl (58 kB)
Collecting chardet<5,>=3.0.2
  Using cached chardet-4.0.0-py2.py3-none-any.whl (178 kB)
Collecting urllib3<1.27,>=1.21.1
  Using cached urllib3-1.26.4-py2.py3-none-any.whl (153 kB)
Installing collected packages: urllib3, idna, chardet, certifi, requests
Successfully installed certifi-2020.12.5 chardet-4.0.0 idna-2.10 requests-2.25.1 urllib3-1.26.4
```

When you are done with the project, you can deactivate the environment.

```bash
deactivate
```


## Code Linting

Linting is very important aspect of writing a clean, readable and efficient code. It helps you identify common errors, formatting issues, best practices. Using a linter is not mandatory but it is highly recommended.

Pylint is very popular linter, and it can be installed using Python package manager.

```bash
pip install pylint
```

Once installed you can check your existing code. For example here is an example from different project

```bash
pylint ../vmware-vra/recipes/vra_requests.py
************* Module vra_requests
/home/maros/code/maroskukan/vmware-vra/recipes/vra_requests.py:8:51: C0303: Trailing whitespace (trailing-whitespace)
/home/maros/code/maroskukan/vmware-vra/recipes/vra_requests.py:33:9: C0303: Trailing whitespace (trailing-whitespace)
/home/maros/code/maroskukan/vmware-vra/recipes/vra_requests.py:41:75: C0303: Trailing whitespace (trailing-whitespace)
/home/maros/code/maroskukan/vmware-vra/recipes/vra_requests.py:91:0: C0304: Final newline missing (missing-final-newline)
/home/maros/code/maroskukan/vmware-vra/recipes/vra_requests.py:1:0: C0114: Missing module docstring (missing-module-docstring)
/home/maros/code/maroskukan/vmware-vra/recipes/vra_requests.py:58:4: C0103: Variable name "pt" doesn't conform to snake_case naming style (invalid-name)
/home/maros/code/maroskukan/vmware-vra/recipes/vra_requests.py:74:0: C0116: Missing function or method docstring (missing-function-docstring)
/home/maros/code/maroskukan/vmware-vra/recipes/vra_requests.py:3:0: C0411: standard import "from os import environ" should be placed before "from prettytable import PrettyTable" (wrong-import-order)

-----------------------------------
Your code has been rated at 7.24/10
```

After fixing the issues reported by pylint run the check again.

```bash
pylint ../vmware-vra/recipes/vra_requests.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 7.24/10, +2.76)
```