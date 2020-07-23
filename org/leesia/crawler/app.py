import re

text = '''
<a class="btn btn2" href="//shu2.resgain.net/name_list.html" title="	司姓名字大全共有司姓名字9457
个">司姓名字大全</a>
'''
pattern = '<a class="btn btn2" href="//(.+?\.html)" title=".*?\n个">([\u4E00-\u9FA5]+)</a>'
match_obj = re.findall(pattern, text)
if match_obj:
    print(match_obj)
    print(match_obj[0][1])
