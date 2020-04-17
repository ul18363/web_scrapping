# -*- coding: utf-8 -*-
"""
Translates JavaScript to Python code. Js2Py is able to translate and execute virtually any JavaScript code.

Js2Py is written in pure python and does not have any dependencies. Basically an implementation of JavaScript core in pure python.
import js2py

f = js2py.eval_js( “function $(name) {return name.length}” )

f(“Hello world”)

# returns 11
"""
import js2py

f = js2py.eval_js( "function $(name) {return name.length}" )

print(f("Hello world"))

# returns 11