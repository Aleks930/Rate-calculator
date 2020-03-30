import json
from urllib import request
count = 0

url = "http://py4e-data.dr-chuck.net/comments_303092.json"
print ("retrieving URL. Stand by.")
uh = request.urlopen(url)
data= uh.read()

info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number
print (count)

#Sample Execution

#$ python solution.py
#Enter location: hhttp://py4e-data.dr-chuck.net/comments_303092.json
#Retrieving http://py4e-data.dr-chuck.net/comments_303092.json
#Retrieved 2582 characters
#Count: 50
#Sum: 2...
