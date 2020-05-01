# Pluralsight Project Audition
Pluralsight Project Audition Sample for Ed Freitas

## Description of the project
This project will provide you a step-by-step guide to create a Python script that is able to read fields from a PDF form document.

The Python script that you will create will be called: `forms.py` (a working copy has been added to this repo: `forms-ready.py`).

## Verify locally
To test this script locally:
* Open up a terminal session at the project root folder.
* You must use Python 3.6.X or above.
* Run command `python forms.py opportunity.pdf`.

The sample PDF form document provided for this demo is called `opportunity.pdf`.

## Task 1: Install the `PyPDF2` library
The PDF file format is a versatile document format. It is one of the world’s most used file formats along with Microsoft Excel and Word. 

The PDF file format is versatile, because it supports various types of content, such as scanned documents, standard text printed content and also form content with fields.

In this case, we will focus on how to read PDF forms, which corresponds to content with fields that are part of a PDF form file.

To be able to read PDF form documents, we need to install the `PyPDF2` library, which can be installed from the command prompt or built-in terminal within [Visual Studio Code](https://code.visualstudio.com/), using the following command.

```
pip install PyPDF2
```

With some Python 3.X installations, `pip3` can also be used instead of `pip`. 

```
pip3 install PyPDF2
```

Both do the same job. Once the library has been installed, we can start.

## Task 2: Import the required modules
Let’s start by importing the modules and libraries that our script will require, which we can see in the listing below.

```
import os
import sys

import PyPDF2
from collections import OrderedDict
```

We will be using an ordered dictionary `OrderedDict`, to return the list of fields read from a PDF form document. We can read any fields within a PDF form document, by using the `readfields` function.

Submit tasks 1 and 2 by creating a `t1_2.py` file within your project folder, with the step described in this task.

### Testing Tasks 1 and 2:

You can test tasks 1 and 2 by running the following command from the terminal: 

```
python test.py t1_2.py
```

If tasks 1 and 2 have been completed successfully, nothing will be returned through the terminal prompt when executing `python test.py t1_2.py`.

If tasks 1 and 2 have not been completed successfully, the following error will be returned through the terminal prompt when executing `python test.py t1_2.py`.

```
Error: t1_2.py does not contain the expected input. Please check t1_2.txt
```

## Task 3: Read field attributes
In order to read a PDF form, we start by specifying the [AcroForm](https://www.smartdoctech.com/pdf/FormsAPIReference.pdf) (Adobe Acrobat Form) field attributes that are used within PDF form documents.

```
fa = {'/FT': 'Field Type', 
'/Parent': 'Parent', 
'/T': 'Field Name', 
'/TU': 'Alternate Field Name',
'/TM': 'Mapping Name', 
'/Ff': 'Field Flags', 
'/V': 'Value', 
'/DV': 'Default Value'}
```

These attributes are checked whenever the `readfields` function runs into a potential field and needs to verify the type of field it is and whether it has any value that can be read.

Make sure that you declare the `readfields` function before declaring the preceding attributes, i.e.:

```
def readfields(obj, t=None, res=None, fo=None):
```

Please add a blank line first (by pressing enter), before you add the code snippets above. Make sure proper identation is used.

Please also submit along the code from the previous task (contained within the `t1_2.py` file), along with the details of this task. Create a new file called `t3.py`.

### Testing Task 3:

You can test task 3 by running the following command from the terminal: 

```
python test.py t3.py
```

If task 3 has been completed successfully, nothing will be returned through the terminal prompt when executing `python test.py t3.py`.

If task 3 has not been completed successfully, the following error will be returned through the terminal prompt when executing `python test.py t3.py`.

```
Error: t3.py does not contain the expected input. Please check t3.txt
```

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

This code needs to be added to the `readfields` function (at the end of the function). Please add a blank line first (by pressing enter), before you add the code snippet above. Make sure proper identation is used.

You can continue where you left off on task 3. Create a file called `t4.py` which should contain the code of the previous tasks, plus this one.

### Testing Task 4:

You can test task 4 by running the following command from the terminal: 

```
python test.py t4.py
```

If task 4 has been completed successfully, nothing will be returned through the terminal prompt when executing `python test.py t4.py`.

If task 4 has not been completed successfully, the following error will be returned through the terminal prompt when executing `python test.py t4.py`.

```
Error: t4.py does not contain the expected input. Please check t4.txt
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

This code needs to be added to the `readfields` function (at the end of the function) to `t5.py` (which should contain all the existing code written up to now). Make sure proper identation is used.

### Testing Task 5:

You can test task 5 by running the following command from the terminal: 

```
python test.py t5.py
```

If task 5 has been completed successfully, nothing will be returned through the terminal prompt when executing `python test.py t5.py`.

If task 5 has not been completed successfully, the following error will be returned through the terminal prompt when executing `python test.py t5.py`.

```
Error: t5.py does not contain the expected input. Please check t5.txt
```

## Task 6: Return the fields on the form
The fields that are identified as PDF form fields are returned in an ordered dictionary `res`, which contains each field with its respective value, as a set of key-value pairs. 

```
return res
```

This code also needs to be added to the `readfields` function (at the end of the function) to `t6.py` (which should contain all the existing code written up to now). Make sure proper identation is used.

This is what the `readfields` function returns.

So, by calling the `readfields` function we can read the PDF form fields of any particular PDF that contains a form, which follows the [AcroForm](https://www.smartdoctech.com/pdf/FormsAPIReference.pdf) specification.

### Testing Task 6:

You can test task 6 by running the following command from the terminal: 

```
python test.py t6.py
```

If task 6 has been completed successfully, nothing will be returned through the terminal prompt when executing `python test.py t6.py`.

If task 6 has not been completed successfully, the following error will be returned through the terminal prompt when executing `python test.py t6.py`.

```
Error: t6.py does not contain the expected input. Please check t6.txt
```

## Task 7: The `getfields` function 

With the `readfields` ready, we need to first open the PDF file and read its content—which we can do with the following code.

```
def getfields(infile):
    infile = PyPDF2.PdfFileReader(open(infile, 'rb'))
    fields = readfields(infile)
    return OrderedDict((k, v.get('/V', '')) for k, v in fields.items())
```

Please add a blank line first (by pressing enter), before you add the code snippet above to `t7.py` (which should contain all the existing code written up to now). Make sure proper identation is used.

This function essentially opens the PDF file (infile) in read-only binary mode (`rb`) and reads its full content by calling the `PdfFileReader` method from the `PyPDF2` library.

Once that full content has been read, it is passed to the `readfields` function, which checks if there’s a form embedded within the PDF and if so, extracts each of the fields contained within. 

Those fields are then returned in a new ordered dictionary, as key-value pairs, such as:

```
OrderedDict([('Field1', '0001'), ('Field2', '0002'), ('Field3', '0003')])
```

### Testing Task 7:

You can test task 7 by running the following command from the terminal: 

```
python test.py t7.py
```

If task 7 has been completed successfully, nothing will be returned through the terminal prompt when executing `python test.py t7.py`.

If task 7 has not been completed successfully, the following error will be returned through the terminal prompt when executing `python test.py t7.py`.

```
Error: t7.py does not contain the expected input. Please check t7.txt
```

## Task 8: Calling the `getfields` function
The `getfields` function can be invoked from a `run` function as follows.

```
def run(args):
    try: 
        if len(args) == 2:
            pdf_file_name = args[1]
            items = getfields(pdf_file_name)
            print(items)
    except BaseException as msg:
        print('An error occured... :( ' + str(msg))
```

Please add a blank line first (by pressing enter), before you add the code snippet above to `t8.py` (which should contain all the existing code written up to now). Make sure proper identation is used.

Notice that the name of the PDF form document to extract the fields from (in our case `opportunity.pdf`) is represented by `args[1]`.

### Testing Task 8:

You can test task 8 by running the following command from the terminal: 

```
python test.py t8.py
```

If task 8 has been completed successfully, nothing will be returned through the terminal prompt when executing `python test.py t8.py`.

If task 8 has not been completed successfully, the following error will be returned through the terminal prompt when executing `python test.py t8.py`.

```
Error: t8.py does not contain the expected input. Please check t8.txt
```

## Task 9: Invoking the script
The `run` function and thus the script can be invoked as follows.

```
if __name__ == '__main__':
    run(sys.argv)
```

Please add a blank line first (by pressing enter), before you add the code snippet above to `t9.py` (which should contain all the existing code written up to now). Make sure proper identation is used.

Where `sys.argv` represents the name of the parameter (PDF form document: `opportunity.pdf`) passed to `forms.py` when running the script from the terminal:

`python forms.py opportunity.pdf`

To finalize, save all the changes done to the `forms.py` file.

You are now ready to execute the `forms.py` Python script.

### Testing Task 9:

You can test task 9 by running the following command from the terminal: 

```
python test.py t9.py
```

If task 9 has been completed successfully, nothing will be returned through the terminal prompt when executing `python test.py t9.py`.

If task 9 has not been completed successfully, the following error will be returned through the terminal prompt when executing `python test.py t9.py`.

```
Error: t9.py does not contain the expected input. Please check t9.txt
```

The end result of this exercise should be that the code contained within `t9.py` should be identical to the code within `forms-ready.py`.

## Testing the finished script:

If you have successfully tested all the tasks the `t9.py` file will contain all the code required. Copy the contents of `t9.py` to `forms.py` and then execute the following command:

```
python forms.py opportunity.pdf
```

You should see the following result:

```
OrderedDict([('opp5', 'New Customer'), ('opp4', 'Cool Customer '), ('opp9', '4/17/2020'), ('opp3', 'Test Opportunity'), ('opp11', 
'Prospecting'), ('opp6', 'Phone Inquiry')])
```
