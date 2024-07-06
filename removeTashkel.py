#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:53:56 2024

@author: noob
"""

import re
def remove_tashkeel(text):
    tashkeel = u'\u0617-\u061A\u064B-\u0652'  # Range of Arabic diacritics
    pattern = "[" + tashkeel + "]"
    return re.sub(pattern, '', text)



with open("Q.txt", "r") as input_file:
    content = input_file.read()

content = remove_tashkeel(content)

with open("output.txt", "w") as output_file:
    output_file.write(content)