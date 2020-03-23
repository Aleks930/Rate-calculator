#In this assignment you will write a Python program that expands on https://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position from the top and follow that link, repeat the process a number of times, and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1
tags = soup('a')
url = tags[position].get('href', None)
n = 0
while n < count:
    n = n + 1
    print('Retrieving:', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url = tags[position].get('href', None)
