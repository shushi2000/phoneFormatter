#!/usr/bin/env python
#!coding: utf-8

# An implementation of this 
# https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch04s02.html

import re

phoneReg = re.compile(r'^(?:\+?1[-.●]?)?\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$')

def validAndFormatPhone(p):
    if p:
        p = str(p)
        phoneNumber = phoneReg.search(p)
        if phoneNumber:
            return phoneReg.sub(r'(\1)-\2-\3', p)
        else:
            return None
    else:
        return None

