import urllib.request

'''
    抓取网页
'''

file = urllib.request.urlopen("http://www.baidu.com")

data = file.read()
# datalines = file.readlines()
# dataline = file.readline()

# print(data)
print(data)
# print(dataline)

localFile = open("./page.html", "wb")
localFile.write(data)
localFile.close()

print(file.info())
print(file.getcode())
print(file.geturl())
print(urllib.request.quote("http://www.baidu.com"))
print(urllib.request.unquote("http%3A//www.baidu.com"))
