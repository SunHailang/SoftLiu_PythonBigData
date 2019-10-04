
import requests

import re

headers={
    'Host': 'www.baidu.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.baidu.com/',
    'Sec-Fetch-Mode': 'no-cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
url = 'https://www.baidu.com/'
#html = requests.get(url, headers=headers, verify=False).content
#strData = html.decode('utf-8')
# print(strData)
# print(html)
'''
fo = open('baidu.html', 'w', encoding='utf-8')
fo.write(strData)
fo.close()
'''
'''
re.compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

语法格式为：

re.compile(pattern[, flags])
'''
fo = open('baidu.html', 'r', encoding='utf-8')
strData = fo.read()
pattern = re.compile(r'((http|https)://.*?(png|gif))')
# pattern1 = re.compile(r'')

data = re.findall(pattern, strData)
for item in data:
    print(item[0])


