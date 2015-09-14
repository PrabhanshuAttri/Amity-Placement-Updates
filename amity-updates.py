from bs4 import BeautifulSoup
import time
import urllib2
import subprocess
from  R2D2 import *

def checkUpdates(url):
	value = url.split("=",1)[1]
	url = url.split("Popup",1)[0]
	print
	print '$',str(value), url
	flag = 0
	while True:
		print
		log('accessing amity.edu ',1)
		try:		
			data = urllib2.urlopen(url).read()
		except urllib2.HTTPError, err:
			if err.code == 404:
				print "{0} of {1}: 404: Page not found! | {2}".format(n+1,len(menu),url)
			elif err.code == 403:
				print "{0} of {1}: 403: Access denied! | {2}".format(n+1,len(menu),url)
			else:
				print "{0} of {1}: Something happened! Error code: {2} | {3}".format(n+1,len(menu),err.code,url)
		except urllib2.URLError, err:
			print "{0} of {1}: Some other error happened: {2} | {3}".format(n+1,len(menu),err.reason,url)
		soup = BeautifulSoup(data)
		marquee = soup.findAll('marquee')
		for i in marquee:
			links = i.findAll('a')
			#print links
			for j in links:
				message = ''
				print j['href'],
				idnumber = j['href'].replace('Popup.asp?Eid=','')
				print idnumber,
				if j.string is None:
					message = j.find('strong').string
					print j.find('strong').string
				else:
					message = j.string
					print j.string
				if int(idnumber) > int(value):
					flag = 1
					print idnumber, value
					subprocess.Popen(['notify-send', message])
		
		if flag == 1:
			return

def main():	
	print 'Do... or do not, there is no try'
	
	#enter the last update (every update after this will be notified to you)
	url = "http://amity.edu/placement/Popup.asp?Eid=1262" 
	checkUpdates(url)


	

if __name__ == "__main__":
  main()
