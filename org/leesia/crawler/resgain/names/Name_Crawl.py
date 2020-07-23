import re
import urllib.request
import urllib.error
import time

'''
    抓取名字大全名字
'''


def convertTime(start, end):
    start = int(round(start * 1000))
    end = int(round(end * 1000))

    t = end - start

    day = int(t / 86400000)
    t = t % 86400000
    hour = int(t / 3600000)
    t = t % 3600000
    minute = int(t / 60000)
    t = t % 60000
    second = int(t / 1000)
    mill = t % 1000

    text = ''
    if day > 0:
        text += str(day) + '天'
    if hour > 0:
        text += str(hour) + '小时'
    if minute > 0:
        text += str(minute) + '分'
    if second > 0:
        text += str(second) + '秒'
    if mill > 0:
        text += str(mill) + '毫秒'

    return text


def getFirstPages(url):

    start = time.time()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    html = str(html)
    print(html)

    pattern = '<a class="btn btn2" href="//(.+?\.html)" title=".+?\n">([\u4E00-\u9FA5]+)</a>'
    pages = re.findall(pattern, html)

    end = time.time()

    print(pages)
    print('从：' + url + '解析全部姓氏首页，耗时: ' + convertTime(start, end))

    return pages


def crawlEachPage(url, lastName):
    start = time.time()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    html = str(html)

    pattern = '<a class="biaobai" href="/biaobai\.rhtml\?name=([\u4E00-\u9FA5]+)" target="_blank">'
    names = re.findall(pattern, html)
    if not names or len(names) == 0:
        return 0

    nameFile = open('./names/' + lastName + '.txt', 'a')
    for name in names:
        nameFile.write(str(name) + '\n')
    nameFile.close()

    end = time.time()

    print(url + '：' + lastName + '，耗时: ' + convertTime(start, end))

    return len(names)


def crawlLastName(url, lastName):
    nameFile = open('./names/' + lastName + '.txt', 'w+')
    nameFile.write("")
    nameFile.close()

    num = crawlEachPage(url, lastName)
    index = 1

    while num > 0:
        index += 1
        each_url = url.replace(".html", "_" + str(index) + '.html')
        try:
            num = crawlEachPage(each_url, lastName)
        except urllib.error.URLError as e:
            print(e.reason)
            num = 0


def crawlAllName(url):
    lastNameFirstPages = getFirstPages(url)
    if not lastNameFirstPages or len(lastNameFirstPages) == 0:
        return

    for firstPage in lastNameFirstPages:
        url = 'http://' + firstPage[0]
        lastName = getLastName(firstPage[1])
        crawlLastName(url, lastName)


def getLastName(text):
    index = text.find('姓')
    return text[0:index + 1]


link = 'http://www.resgain.net/xmdq.html'
crawlAllName(link)
