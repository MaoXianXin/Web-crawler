from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# The entry of the Web
URL = "http://www.w3cschool.cn/java/java-if-else-switch.html"

# read Web data into html
html = urlopen(URL).read()

bsObj = BeautifulSoup(html,"html.parser")

# select which link you need
JavaLinks = bsObj.findAll("a",href=re.compile("^(/java/java)"),text=re.compile("^(Java)"))

# record the number of link
count = 0

for link in JavaLinks:
    string1 = link['href']
	
	# the destination where you want to store you WebPage
    DES = "F:\\WebPage\\" + string1.split('/',string1.count('/'))[2]
    # print(DES)
	
    url = "http://www.w3cschool.cn" + link['href']
    # print(url)
    count = count + 1
    print(count)
	
	# excute storage opreation
    urlretrieve(url,DES)