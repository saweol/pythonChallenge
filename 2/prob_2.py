#-*- coding: utf-8 -*-
'''
pythonchallenge problem_2
http://www.pythonchallenge.com/pc/def/map.html
image : K -> M, O -> Q, E -> G
- General tips 
Use the hints. They are helpful, most of the times.
Investigate the data given to you.
Avoid looking for spoilers.
'''

question = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
decode = ""
dec_max = 122
dec_min = 96


for x in question:
	if x == " " or x == "." or x == "\'":
		decode = decode + x
		continue
	else:
		data = chr(ord(x)+2)
		if ord(data) > dec_max:
			data = chr(dec_min + (ord(data) - dec_max))
		decode = decode + data


print decode

