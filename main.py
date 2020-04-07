import requests, sys, re, os

os.system('clear')
banner ="""
   _____
  /  '  \     [ PRAYER SCHEDULE ]
 |   |   |
 |- -•  -|     Author  : sCuby07
 |       |   |===================|
  \__'__/         Version 0.3"""

def help():
	print(banner)
	exit('''
This tool only use python3
not supported python2 

Commands:
   python3 main.py {option} {city}

Options:
  --all       =  show all prayer schedule
  --fajr      =  show fajr time
  --shurooq   =  show shurooq time
  --dhuhr     =  show dhuhr time
  --asr       =  show asr time
  --maghrib   =  show maghrib time
  --isha      =  show isha time

City:
   Support All City in All Country

Exam Usage:
   python3 main.py -all Jakarta''')

def fajr_time():
        try:
                d = ""
                for i in sys.argv:
                        d += i + " "
                d = d.replace('main.py --fajr ', '')
                x = requests.get('http://muslimsalat.com/%s' %(d)).text
                z = r'{"date_for":"(.*?)","fajr":"(.*?)","shurooq":"(.*?)","dhuhr":"(.*?)","asr":"(.*?)","maghrib":"(.*?)","isha":"(.*?)"}'
                a = re.search(z, x)
                print(banner + '\n\nDate : %s\nAsr : %s'% (a.group(1),a.group(2)))
        except: help()

def shurooq_time():
        try:
                d = ""
                for i in sys.argv:
                        d += i + " "
                d = d.replace('main.py --shurooq ', '')
                x = requests.get('http://muslimsalat.com/%s' %(d)).text
                z = r'{"date_for":"(.*?)","fajr":"(.*?)","shurooq":"(.*?)","dhuhr":"(.*?)","asr":"(.*?)","maghrib":"(.*?)","isha":"(.*?)"}'
                a = re.search(z, x)
                print(banner + '\n\nDate : %s\nShurooq : %s'% (a.group(1),a.group(3)))
        except: help()

def maghrib_time():
        try:
                d = ""
                for i in sys.argv:
                        d += i + " "
                d = d.replace('main.py --maghrib ', '')
                x = requests.get('http://muslimsalat.com/%s' %(d)).text
                z = r'{"date_for":"(.*?)","fajr":"(.*?)","shurooq":"(.*?)","dhuhr":"(.*?)","asr":"(.*?)","maghrib":"(.*?)","isha":"(.*?)"}'
                a = re.search(z, x)
                print(banner + '\n\nDate : %s\nMaghrib : %s'% (a.group(1),a.group(6)))
        except: help()

def dhuhr_time():
	try:
		d = ""
		for i in sys.argv:
			d += i + " "
		d = d.replace('main.py --dhuhr ', '')
		x = requests.get('http://muslimsalat.com/%s' %(d)).text
		z = r'{"date_for":"(.*?)","fajr":"(.*?)","shurooq":"(.*?)","dhuhr":"(.*?)","asr":"(.*?)","maghrib":"(.*?)","isha":"(.*?)"}'
		a = re.search(z, x)
		print(banner + '\n\nDate : %s\nDhuhr : %s'% (a.group(1),a.group(4)))
	except: help()

def isha_time():
        try:
                d = ""
                for i in sys.argv:
                        d += i + " "
                d = d.replace('main.py --isha ', '')
                x = requests.get('http://muslimsalat.com/%s' %(d)).text
                z = r'{"date_for":"(.*?)","fajr":"(.*?)","shurooq":"(.*?)","dhuhr":"(.*?)","asr":"(.*?)","maghrib":"(.*?)","isha":"(.*?)"}'
                a = re.search(z, x)
                print(banner + '\n\nDate : %s\nIsha : %s'% (a.group(1),a.group(7)))
        except: help()

def asr_time():
	try:
		d = ""
		for i in sys.argv:
			d += i + " "
		d = d.replace('main.py --asr ', '')
		x = requests.get('http://muslimsalat.com/%s' %(d)).text
		z = r'{"date_for":"(.*?)","fajr":"(.*?)","shurooq":"(.*?)","dhuhr":"(.*?)","asr":"(.*?)","maghrib":"(.*?)","isha":"(.*?)"}'
		a = re.search(z, x)
		print(banner + '\n\nDate : %s\nAsr : %s'% (a.group(1),a.group(5)))
	except EOFError: pass


def all_time():
	try:
		d = ""
		for i in sys.argv:
			d += i + " "
		d = d.replace('main.py --all ','')
		x = requests.get('http://muslimsalat.com/%s' %(d)).text
		s = re.search('"title":"(.*?)"', x).group(1)
		z = r'{"date_for":"(.*?)","fajr":"(.*?)","shurooq":"(.*?)","dhuhr":"(.*?)","asr":"(.*?)","maghrib":"(.*?)","isha":"(.*?)"}'
		a = re.search(z, x)
		print(banner)
		if s == '':
			b = re.search('"query":"(.*?)"', x).group(1)
			b = b.replace(b[0], b[0].upper())
			print('\nCity : %s, Indonesia'% (b))
		else:
			print('\nCity : %s'% (s))
		print('''Date : %s
Fajr : %s
Shurooq : %s
Dhuhr : %s
Asr : %s
Maghrib : %s
Isha : %s'''%(a.group(1),a.group(2),a.group(3),a.group(4),a.group(5),a.group(6),a.group(7)))
	except EOFError: pass




if sys.argv[1] == '--all':
 all_time()
elif sys.argv[1] == '--fajr':
 fajr_time()
elif sys.argv[1] == '--shurooq':
 shurooq_time()
elif sys.argv[1] == '--dhuhr':
 dhuhr_time()
elif sys.argv[1] == '--asr':
 asr_time()
elif sys.argv[1] == '--maghrib':
 maghrib_time()
elif sys.argv[1] == '--isha':
 isha_time()
else:
 help()
