# Pluralsight Project Audition
Pluralsight Project Audition Sample for [Eduardo Freitas](https://edfreitas.me)

## Purpose of the project
This project will provide you a step-by-step guide to create a Python script that is able to read fields from a PDF form document.

## Description of the project
This project will provide you a step-by-step guide to create a Python script that is able to read fields from a PDF form document.

## Verify locally
To test this script locally:
* Open up a terminal at the project root folder
* You must use Python 3.6.X or above
* Run command `python forms.py`

## Task 1: Install the `PyPDF2` library
The PDF file format is a versatile document format. It is one of the world’s most used file formats along with Microsoft Excel and Word. 

The PDF file format is versatile, because it supports various types of content, such as scanned documents, standard text printed content and also content with fields.

In this case, we will focus on how to read PDF forms, which corresponds to content with fields that are part of a PDF file.

To be able to read PDF form documents, we need to install the PyPDF2 library, which can be installed from the command prompt or built-in terminal within VS Code, using the following command.

```
pip install PyPDF2
```

With some Python 3.X installations, pip3 can also be used instead of pip. Both do the same job. Once the library has been installed, we can start writing our script.

## Task 2: Import the required modules
Let’s start by importing the modules and libraries that our script will require, which we can see in the listing below.

```
import os
import sys

import PyPDF2
from collections import OrderedDict
```

We will be using an ordered dictionary `OrderedDict`, to return the list of fields read from a PDF form document. We can read any fields within a PDF form document, by using the `readfields` function.


## Task 3: Read field attributes
In order to read a PDF form, we start by specifying the [AcroForm](https://www.smartdoctech.com/pdf/FormsAPIReference.pdf) (Adobe Acrobat Form) field attributes that are used within PDF form documents.

```
fa = {'/FT': 'Field Type', '/Parent': 'Parent', 
    '/T': 'Field Name', '/TU': 'Alternate Field Name',
    '/TM': 'Mapping Name', '/Ff': 'Field Flags', 
    '/V': 'Value', '/DV': 'Default Value'}
```

These attributes are checked whenever the `readfields` function runs into a potential field and needs to verify the type of field it is and whether it has any value that can be read.

## Task 4: Check the document form `/Root`
The next step in PDF form reading process is to find the PDF document root (`/Root`) and check whether it contains a (`/AcroForm`) tag.

```
if res is None:
    res = OrderedDict()
    items = obj.trailer["/Root"]
    if "/AcroForm" in items:
        t = items["/AcroForm"]
    else:
        return None
if t is None:
    return res
```

## Task 5: Identify the fields on the form

If the PDF document contains a form, then a tree object with the potential fields is returned, which is then inspected. This is done with the following code.

```
obj._checkKids(t, res, fo)
for attr in fa:
    if attr in t:
        obj._buildField(t, res, fo, fa)
        break
if "/Fields" in t:
    flds = t["/Fields"]
    for f in flds:
        fld = f.getObject()
        obj._buildField(fld, res, fo, fa)
```

## Task 6: Return the fields on the form
The fields that are identified as PDF form fields are returned in an ordered dictionary, which contains each field with its respective value, as a set of key-value pairs. 

```
return res
```

This is what the `readfields` function returns.

## Task 7: Wrapping up the `readfields` function 

So, by calling the readfields function we can read the PDF form fields of any particular PDF that contains a form, which follows the [AcroForm](https://www.smartdoctech.com/pdf/FormsAPIReference.pdf) specification.

## Task 8: Wrapping up the `readfields` function
With the `readfields` ready need to first open the PDF file and read its content—which we can do with the following code.

```
def getfields(infile):
    infile = PyPDF2.PdfFileReader(open(infile, 'rb'))
    fields = readfields(infile)
    return OrderedDict((k, v.get('/V', '')) for k, v in fields.items())
```

This function essentially opens the PDF file (infile) in read-only binary mode (`rb`) and reads its full content by calling the `PdfFileReader` method from the `PyPDF2` library.

Once that full content has been read, it is passed to the `readfields` function, which checks if there’s a form embedded within the PDF and if so, extracts each of the fields contained within. 

Those fields are then returned in a new ordered dictionary, as key-value pairs, such as:

```
OrderedDict([('Field1', '0001'), ('Field2', '0002'), ('Field3', '0003')])
```
