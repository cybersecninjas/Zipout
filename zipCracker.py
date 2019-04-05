##Import zipfile

import  zipfile

##initialize the protected zipfile

file_Name = "help.zip"

##initialize your payloads

dictionary = "rockyou.txt"

password = ' '

file_to_open = zipfile.ZipFile(help.zip)
with open(dictionary, 'r') as f:
	for line in f.readlines():
		try:
			file_to_open.extractall(pwd=password)
			password = 'password found: %s' % password
			print password
		except:
			pass

