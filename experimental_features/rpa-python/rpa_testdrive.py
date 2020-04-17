# -*- coding: utf-8 -*-

"""
    Library for Robotic Process Automation
    It seems to need from opencv and tesseract 
"""
import rpa as r
r.init()
r.url('https://www.google.com')
r.type('//*[@name="q"]', 'decentralization[enter]')
print(r.read('result-stats'))
r.snap('page', 'results.png')
r.close()