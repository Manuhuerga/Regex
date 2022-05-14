#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

phoneRegex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo = phoneRegex.search("My phone number is 415-555-4242.")

print(mo)
print(mo.group())

################################################################
print("#" * 15)

phoneRegex = re.compile(r"(\d{3})-(\d{3}-\d{4})")
po = phoneRegex.search("My phone number is 415-555-4242.")

print(po.group(0))
print(po.group(1))
print(po.group(2))
print(po.groups())
areaCode, mainNumber = po.groups()
################################################################
print("#" * 15)

phoneNumRegex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("Mi número de teléfono es (415) 555-4242.")
print(mo.groups())

################################################################
print("#" * 15)
# Devuelve el primer match, si encuentra batman o superman devuelve
# el que encontro primero
heroRegex = re.compile(r"Batman | Superman")
mo1 = heroRegex.search("Batman y Superman")
print(mo1.group())

#################################################################\
print("#" * 15)