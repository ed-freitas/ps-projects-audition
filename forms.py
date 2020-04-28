import os
import sys

import PyPDF2
from collections import OrderedDict

def readfields(obj, t=None, res=None, fo=None):
    fa = {'/FT': 'Field Type', 
    '/Parent': 'Parent', 
    '/T': 'Field Name', 
    '/TU': 'Alternate Field Name',
    '/TM': 'Mapping Name', 
    '/Ff': 'Field Flags', 
    '/V': 'Value', 
    '/DV': 'Default Value'}

    if res is None:
        res = OrderedDict()
        items = obj.trailer["/Root"]
        if "/AcroForm" in items:
            t = items["/AcroForm"]
        else:
            return None
    if t is None:
        return res
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
    return res

def getfields(infile):
    infile = PyPDF2.PdfFileReader(open(infile, 'rb'))
    fields = readfields(infile)
    return OrderedDict((k, v.get('/V', '')) for k, v in fields.items())

def run(args):
    try: 
        if len(args) == 2:
            pdf_file_name = args[1]
            items = getfields(pdf_file_name)
            print(items)
    except BaseException as msg:
        print('An error occured... :( ' + str(msg))

if __name__ == '__main__':
    run(sys.argv)