import urllib.request

'''
    打印日志
'''

httphd = urllib.request.HTTPHandler(debuglevel=1)
httpshd = urllib.request.HTTPSHandler(debuglevel=1)

opener = urllib.request.build_opener(httphd, httpshd)
urllib.request.install_opener(opener)

data = urllib.request.urlopen("http://www.baidu.com")
