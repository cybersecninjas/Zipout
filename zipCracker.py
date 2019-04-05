import os
import sys
import zipfile
import threading

def helper():
	'''Print Help Message to user.'''
	print '[!] This is help message. Provide the application with the following parameters:'
	print '[+] Please follow the order provided (zip file then wordlist)'
	print '\t[-] %s file.zip wordlist.txt' % sys.argv[0]

def cracker(password,file_to_open):
	'''Test if a password can crack a zip file.'''
	try:
		file_to_open.extractall(pwd=password)
		victory_message = '\n[!] Password found: %s \n' % password
		print victory_message
		os._exit(0)
	except Exception as err:
		pass

# Check if parameters are enough before starting
if len(sys.argv) < 3 :
	helper()
	sys.exit()
else:
	file_to_crack = sys.argv[1]
	dictionary = sys.argv[2]


# Check if Zip file can be accessed
try:
	file_to_open = zipfile.ZipFile(file_to_crack)
except IOError:
	print '[!] An Error Ocured While reading the provided Zip File: %s' % file_to_crack
	sys.exit()
except zipfile.BadZipfile:
	print '[!] You provided a bad Zip file: %s' % file_to_crack
	sys.exit()


# Alert User Cracking started
print '[+] Zip Cracking Process started:'
print '\t[-] Cracking File : %s' % file_to_crack
print '\t[-] Using Wordlist : %s' % dictionary


# Test each word in the passwordlist
try:
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			try_cracking = threading.Thread(target=cracker, args=(line.strip(),file_to_open))
			try_cracking.start()
			try_cracking.join()
except IOError as err:
	print '[!] An Error Ocured While reading the provided dictionary file: %s' % dictionary
	sys.exit()
else:
	print '[!] Something went wrong while starting the bruteforce: %s' % dictionary
	sys.exit()
