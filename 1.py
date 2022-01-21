#!/usr/bin/python
# -*- coding: utf-8 -*-

#Conversão de hexadecimal para base64

import base64

str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

ascii_str = str.decode("hex") 
#transforma de hexadecimal para ASCII

base64_str = base64.b64encode(ascii_str)
#transforma de ASCII para base64

print base64_str
#imprime o resultado 
