# Python Cookbook
- [Python Cookbook](#python-cookbook)
  - [Introduction](#introduction)
    - [Use Cases](#use-cases)
    - [Characteristics](#characteristics)
  - [Documentation](#documentation)
  - [Environment](#environment)
    - [Local environment](#local-environment)
    - [Remote environment](#remote-environment)

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
- [Python Playground](https://www.katacoda.com/courses/python/playground)

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

### Remote environment

If you do not want to install any binaries on your system, you can take advantage of [Katacoda](https://www.katacoda.com/) which provides an online [Python Playground](https://www.katacoda.com/courses/python/playground) inside what looks like a docker container.



