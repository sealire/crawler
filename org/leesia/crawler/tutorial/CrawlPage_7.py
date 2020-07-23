import urllib.request
import urllib.error

'''
    打印异常信息
'''

try:
    urllib.request.urlopen('http://www.resgain.net/xmdq.html')
except urllib.error.HTTPError as e:
    print('http error')
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    print('url error')
    print(e.code)
    print(e.reason)
