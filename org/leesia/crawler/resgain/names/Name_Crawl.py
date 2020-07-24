import re
import requests
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


def openPage(url):
    print('open page: ' + url)
    start = time.time()

    text = requests.get(url, timeout=120, headers={"Connection": "close"}).text

    end = time.time()
    print('open page: ' + url + ', done, 耗时: ' + convertTime(start, end))

    return text


def getFirstPages(url):

    start = time.time()

    html = openPage(url)

    pattern = '<a class="btn btn2" href="//(.+?\.html)" title=".+?\n">([\u4E00-\u9FA5]+)</a>'
    pages = re.findall(pattern, html)

    end = time.time()

    print('从：' + url + '解析全部姓氏首页，耗时: ' + convertTime(start, end))
    print("")

    return pages


def crawlEachPage(url, lastName):
    start = time.time()

    html = openPage(url)

    pattern = '<a class="biaobai" href="/biaobai\.rhtml\?name=([\u4E00-\u9FA5]+)" target="_blank">'
    names = re.findall(pattern, html)
    if not names or len(names) == 0:
        return 0

    nameFile = open('./names/' + lastName + '.txt', 'a')
    for name in names:
        nameFile.write(str(name) + '\n')
    nameFile.close()

    end = time.time()

    print('解析：' + url + '：' + lastName + '，耗时: ' + convertTime(start, end))
    print("")

    return len(names)


def crawlLastName(url, lastName):
    nameFile = open('./names/' + lastName + '.txt', 'w+')
    nameFile.write("")
    nameFile.close()

    error = False

    num = crawlEachPage(url, lastName)
    index = 1

    while num > 0 and not error:
        index += 1
        each_url = url.replace(".html", "_" + str(index) + '.html')
        try:
            num = crawlEachPage(each_url, lastName)
        except Exception as e:
            print(e)
            print(lastName + ' error')
            num = 0
            error = True
    return error


def crawlAllName(url):
    lastNameFirstPages = getFirstPages(url)
    if not lastNameFirstPages or len(lastNameFirstPages) == 0:
        return

    doneNames = readDoneNames()
    print("已完成：" + str(doneNames))
    print("")

    for firstPage in lastNameFirstPages:
        url = 'http://' + firstPage[0]
        lastName = getLastName(firstPage[1])
        if lastName not in doneNames:
            start = time.time()

            error = crawlLastName(url, lastName)

            if not error:
                nameFile = open('./names.txt', 'a+')
                nameFile.write(lastName + "\n")
                nameFile.close()

            end = time.time()
            print(lastName + '，耗时: ' + convertTime(start, end))
            print('')


def getLastName(text):
    index = text.find('姓')
    return text[0:index]


def readDoneNames():
    nameFile = open('./names.txt', 'r+')
    data = nameFile.readlines()
    nameFile.close()

    names = []
    for name in data:
        names.append(name.replace('\n', ''))

    return names


link = 'http://www.resgain.net/xmdq.html'
crawlAllName(link)
