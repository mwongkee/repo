import urllib2
from xml.dom.minidom import parse, parseString
import unicodedata
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
infile = opener.open('http://en.wikipedia.org/wiki/List_of_culinary_fruits')
page = infile.read()
dom = parseString(page)


masterDiv = [node for node in dom.getElementsByTagName("div") if node.hasAttribute("id") and node.attributes["id"].value == "mw-content-text"]
innerDivs = [node for node in masterDiv[0].getElementsByTagName("div") if node.parentNode == masterDiv[0]]
f = open("outfile", "w")
for divNum in range(6,26+6) :
    fruitAnchors = [node for node in innerDivs[divNum].getElementsByTagName("a") if node.hasAttribute("class") and node.attributes["class"].value == "mw-redirect"]
    fruits = [node.childNodes[0].toxml() for node in fruitAnchors]
    for fruit in fruits:
        ascii_fruit = unicodedata.normalize('NFKD',fruit).encode('ascii','ignore')
        f.write( ascii_fruit.lower() + '\n')

f.close()