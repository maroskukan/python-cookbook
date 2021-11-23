# Python: XML, JSON and the Web

Course notes from Python:XML, JSON and the Web by Joe Marini.

## Overview

### XML

- XML stands for Extensible Markup Langugage and related technologies
- Similar to HTML with some changes to better suit general data
- Rich and expressive but more complex than JSON
- Rules for XML formatting are more strict
- Usually used for complex, document-like data
  - Examples: Andorid apps reasources, RSS, and ATOM blog feeds
- [https://www.w3.org/XML](https://www.w3.org/XML)

#### Formatting Rules

- XML documents must always have a single root tag
- XML documents can have an optional document declaration
- Empty tags must have a closing slash: `<tag />`
- Attributes must have values that are enclosed in quotes
- Tags must be properly nested within each other
- Tags and attributes starting with "xml" are reserved


### JSON

- JSON stands for JavaScript Object Notation
- Very concise format for serializing object data
- Derived from JavaScript but supported by most modern languages
- Compact and easy to read, write and process
- [https://www.json.org](https:/www.json.org)

#### Formatting Rules

- **Number** - signed decimal number, no Integer/Float distinction
- **String** - Unicode or escaped characters inside double quotes
- **Boolean** - True or false value
- **Null** - Null value
- **Array** - List of ordered values
- **Object** - Collection of key-value pairs, keys are strings


## Python Web related modules and tools

- [urllib](https://docs.python.org/3/library/urllib.html)
- [http](https://docs.python.org/3/library/http.html)
- [json](https://docs.python.org/3/library/json.html)
- [xml](https://docs.python.org/3/library/xml.html)
- [lxml](https://lxml.de)
- [requests](https://docs.python-requests.org/en/master/)
- [httpib.org](https://httpbin.org)

### urllib

Contains modules for working with URLs:
- urllib.request
- urllib.error
- urllib.parse
- urllib.robotparser

Im summary, urllib is simpe to use but does have some limitations such as:
- Only supports a subset of HTTP by default
- Does not automatically decode returned data
- Common features, such as cookies or authentication require more modules
- Difficult to implement advanced features such as timeouts
- Processing returned data, such as JSON is cumbersome
