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

### request

- Simple API - each HTTP verb is a method name
- Makes working with parameters, headers, and cookies easier
- Automatically decodes returned content
- Automatically parses JSON content when detected
- Handles redirects, timeouts, and errors
- Advanced features like authentication and sessions

### json

Parsing functions:
- obj = load(file)
- obj = loads(string)

Serialization functions:
- dump(obj, file)
- str = dumps(obj)

Serializing Python Data to JSON

| Python Object           | JSON Representation |
| ----------------------- | ------------------- |
| dict                    | object              |
| list, tuple             | array               |
| str                     | string              |
| int, long, float, Enums | number              |
| True                    | true                |
| False                   | false               |
| None                    | null                |

Parsing JSON into Python

| JSON Data             | Python Object |
| --------------------- | ------------- |
| object                | dict          |
| array                 | list          |
| string                | str           |
| Integer number        | int           |
| Floating point number | float         |
| true, false           | True, False   |
| null                  | None          |

### xml

There are two general methods working with XML

- SAX (Simple API for XML)
- DOM (Document Object Model)

#### Simple API for XML

SAX Parsing Model

- Reads entire document start to finish, sequentially
- Generates events as XML content is encoutered
- Your app defines a class to handle content events

Advantages

- Memory efficient - does not need to load entire doc
- Fast - your app only gets events it cares about
- Easy to implement, simple API

Drawbacks

- No random access to doc content
- Context is not passed to parser
- Cannot modify the XML file

SAX API

```python
import xml.sax

xml.sax.parse(file, handler)
xml.sax.parseString(string, handler)

class MyContentHandler(xml.saxContentHandler)
   def __init__(self):
     # member variables go here
   def startDocument(self):
     # Processing starting
   def startElement(self, tagName, attrs):
     # opening tag and attrs have been parsed
   def characters(self, text):
     # member variables go here
```

#### Document Object Model API

- Access any part of an XML structure at random
- Modify the XML content
- Represents the XML as a hierarchical tree structure

*xml.dom.minidom is a lightweight implementation*

```python
import xml.dom.minidom

domtree = xml.dom.minidom.parseString(str)

elem.getElementById(id)
elem.getElementByTagName(tagname)

elem.getAttribute(attrName)
elem.setAttribute(attrName, val)

newElem = document.createElement(tagName)
newElem = document.createTextNode(strOfText)
elem.appendChild(newElem)
```

#### ElementTree API

- Focuses on being simpler and more efficient than DOM
- Elements are treated like lists
- Attributes are treated like dictionaries
- Searching for content in XML is streaighforwarded
  - elem.findall(queryExpression)

