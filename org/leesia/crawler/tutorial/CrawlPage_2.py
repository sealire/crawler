import urllib.request

'''
    抓取网页
'''

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
request = urllib.request.Request("http://zhao.resgain.net/name_list.html", headers=headers)

response = urllib.request.urlopen(request)

data = response.read()

print(data)

localFile = open("./page.html", "wb")
localFile.write(data)
localFile.close()
