'''
@author: Sangram Barge
Created on Sun Nov 15 14:13 2015
@location: Pune, India
'''

from bs4 import BeautifulSoup 
import urllib2 
var_file = urllib2.urlopen("http://www.imdb.com/chart/top")
MAIN_URL="http://www.imdb.com/"
var_html= var_file.read()
var_file.close() 


soup = BeautifulSoup(var_html, "lxml") 
with open('imdb.txt','w') as f:
	for item in soup.find_all(class_='lister-list'): 
		for link in item.find_all('a'): 
			complete_link = MAIN_URL + link.get('href')
			print(complete_link)
			f.write(complete_link+ '\n')
			
			
