import urllib.request

'''
    设置GET请求参数，抓取网页
'''

keyword = "美"
keycode = urllib.request.quote(keyword)
url = "http://www.baidu.com/s?wd=" + keycode
request = urllib.request.Request(url)
data = urllib.request.urlopen(request).read()

localFile = open("./page.html", "wb")
localFile.write(data)
localFile.close()
