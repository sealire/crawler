import re
import urllib.request
import urllib.error


'''
    抓取京东图片
'''


def crawl(url, page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    request = urllib.request.Request("https://list.jd.com/list.html?cat=9987,653,655&page=1", headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    html = str(html)

    pattern = '<ul class="gl-warp clearfix" data-tpl="3">.+?<div id="J_scroll_loading" class="notice-loading-more">'
    result = re.compile(pattern).findall(html)
    result = result[0]

    pattern = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)" data-lazy-img="done'
    images = re.compile(pattern).findall(result)

    x = 1
    for imageUrl in images:
        imageName = './jd_imgs/' + str(page) + '_' + str(x) + '.jpg'
        imageUrl = 'http://' + imageUrl

        try:
            urllib.request.urlretrieve(imageUrl, filename=imageName)
        except urllib.error.URLError as e:
            print(e.reason)
            x += 1
        x += 1


for i in range(1, 2):
    print('page: ' + str(i))
    u = 'https://list.jd.com/list.html?cat=9987,653,655&page=' + str(i)
    crawl(u, i)
