import urllib.request

'''
    抓取网页
'''

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

file = urllib.request.urlretrieve("http://www.resgain.net/xmdq.html", "./page.html")
urllib.request.urlcleanup()
