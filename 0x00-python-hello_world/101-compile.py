#!/usr/bin/python3
import os
import py_compile

pyfile = os.getenv('PYFILE')
if pyfile:
    output_file = pyfile + "c"
    py_compile.compile(pyfile, cfile=output_file)
