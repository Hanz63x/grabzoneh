import requests
import re
import sys

url = "http://www.zone-h.org/archive/notifier="

urll = "http://zone-h.org/archive/published=0"

url2 = "http://www.defacers.org/onhold!"

url4 = "http://www.defacers.org/gold!"

my_cook = {
	"ZHE" : "e9ad66a105864309c4d70bbbcf8016cf",

	"PHPSESSID" : "5us4rl6a68hn0f9n0bbnqlfqc6"

	}
def zonehh():

	print("""

	    |---| Grabb Sites From Zone-h EDITED BY ./Hanz|--|

		[1] Grabb Sites By Notifier [ new ]

		[2] Grabb Sites By Onhold
		
		[3] Archive special [ New ]
		
		[4] Archive [ new ]
		""")

	sec = int(input("Choose Section: "))

	if sec == 1:

		notf = input("Entre notifier: ")

		op = open(notf,"r").read().splitlines()
		for n in op :
			for i in range(1,51):
				n = n.rstrip()
				dz = requests.get(url + n +"/page=" + str(i), cookies=my_cook)

				dzz = dz.content.decode('utf-8')
				print(url + notf +"/page=" + str(i))
				if '<html><body>-<script type="text/javascript"' in str(dzz) :
					print("Change Cookies Please")

					sys.exit()

				elif '<input type="text" name="captcha" value=""><input type="submit">' in str(dzz) :
					input("Entre captcha In Your Browser Of Site [zone-h.org] and click Enter")

					sys.exit()	

				else:
					Hunt_urls = re.findall('<td>(.*)\n							</td>', str(dzz))
					for xxx in Hunt_urls :
						if '/' in xxx :
							xxx = xxx.split('/')[0]
						if '.co...' in xxx :
							xxx = xxx.replace('.co...','.com')
						if '.' in xxx[-1] :
							xxx = xxx.replace('.','')
						print('http://'+xxx)
						with open('attacker.txt','a') as att :
							att.write('http://'+xxx+'\n')
							att.close()

					

	elif sec == 2:

		print(":* __Grabb Sites By Onhold__ ^_^")

		for qwd in range(1, 100):

			rb = requests.get("http://zone-h.org/archive/published=0" + "/page=" + str(qwd) , cookies=my_cook)

			dzq = rb.content.decode('utf-8')

			if '<html><body>-<script type="text/javascript"' in str(dzq):
				print("Change Cookies Plz")
				sys.exit()

				
			elif "captcha" in str(dzq):
				input("Entre captcha In Your Browser Of Site [zone-h.org] and click Enter")
			else:
				Hunt_urlss = re.findall('<td>(.*)\n							</td>', str(dzq))
				for ur in Hunt_urlss :
					if '/' in ur :
						ur = ur.split('/')[0]
					if 'co...' in ur :
						ur = ur.replace('co...','com')
					print(ur)
					with open('result.txt','a') as file :
						file.write('http://'+ur+'\n')
						file.close()
	elif sec == 3 :
		for number in range(1,50) :
			urll = "http://www.zone-h.org/archive/special=1/page="+str(number)
			reques = requests.get(urll, cookies=my_cook).content
			rqu = reques.decode('utf-8')
			if "captcha" in str(rqu) :
				input("Entre captcha In Your Browser Of Site [zone-h.org] and click Enter")
			elif '<html><body>-<script type="text/javascript' in str(rqu) :
				print("Lol Cookies Man ")
			else :
				ref = re.findall('<td>(.*)\n							</td>',str(rqu))
				for arch in ref :
					if '/' in arch :
						arch = arch.split('/')[0]
					if '.co...' in arch :
						arch = arch.replace('.co...','.com')
					if '...' in arch :
						arch = arch.replace('...','')
					if '.' in arch[-1] :
						arch = arch.replace('.','')
					print('http://'+arch)
					with open('special.txt','a') as fil :
						fil.write('http://'+arch+'\n')
						fil.close()
	elif sec == 4 :
		for number in range(1,50) :
			urll = "https://zone-h.org/archive/published=0/page="+str(number)
			reques = requests.get(urll, cookies=my_cook).content
			rqu = reques.decode('utf-8')
			if "captcha" in str(rqu) :
				input("Entre captcha In Your Browser Of Site [zone-h.org] and click Enter")
			elif '<html><body>-<script type="text/javascript' in str(rqu) :
				print("Lol Cookies Man ")
			else :
				ref = re.findall('<td>(.*)\n							</td>',str(rqu))
				for arch in ref :
					if '/' in arch :
						arch = arch.split('/')[0]
					if '.co...' in arch :
						arch = arch.replace('.co...','.com')
					if '...' in arch :
						arch = arch.replace('...','')
					if '.' in arch[-1] :
						arch = arch.replace('.','')
					print('http://'+arch)
					with open('archive.txt','a') as fil :
						fil.write('http://'+arch+'\n')
						fil.close()
	else:

		print("Fuck You Men")
zonehh()
