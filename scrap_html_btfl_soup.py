# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib import request
from bs4 import BeautifulSoup
html=request.urlopen('http://py4e-data.dr-chuck.net/comments_303089.html').read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags=soup('span')
sum=0
for tag in tags:
    sum=sum+int(tag.contents[0])
print(sum)
