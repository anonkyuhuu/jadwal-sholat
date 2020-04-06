import requests, sys, re, os

city = input('Your City : ')
os.system('clear')
banner ="""
   _____
  /  '  \     [ PRAYER SCHEDULE ]
 |   |   |
 |- -•  -|     Author  : sCuby07
 |       |   |==================|
  \__'__/         Version 0.1"""

try:
	print(banner)
	x = requests.get('http://muslimsalat.com/%s'%(city)).text
	s = re.search('"title":"(.*?)"', x).group(1)
	z = r'{"date_for":"(.*?)","fajr":"(.*?)","shurooq":"(.*?)","dhuhr":"(.*?)","asr":"(.*?)","maghrib":"(.*?)","isha":"(.*?)"}'
	a = re.search(z, x)
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
except KeyboardInterrupt:
	pass
except:
	print('Your City Not Found')
