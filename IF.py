## 输入文献网址，获取文献题目，杂志名称，影响因子，发表日期
# V1 目前只适合 Nature 系列杂志，其他待测试，因为每个杂志的网站代码写法不一样；
# 昨晚看了关注的博主的一段话，我觉得很有道理，自己还是太懒了，而且也太笨了；
# 人生苦短，一切遵守 KISS 原则。持续构建一套自己都觉得很爽的灵活够用的渗透测试方法论，需要借用的借用，需要脚本化的脚本化，需要 Web 化的 Web 化，需要工程化的工程化，需要产品化的产品化，需要赚钱的赚钱，需要开源的开源。这里有一个关键点：团队作战，共同进步:-)
# KISS原则是英语 Keep It Simple, Stupid 的首字母缩略字，是一種歸納過的經驗原則。 KISS 原则是指在设计当中應當注重簡約的原则。
# 共勉

import requests,re
from bs4 import BeautifulSoup
url = 'https://www.nature.com/articles/s41587-020-0422-6' #NBT
url = 'https://www.nature.com/articles/s41587-020-0422-6' #NC
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
content = soup.prettify()
soup_match = re.search('datetime="(.*?)"', content) ## 非贪婪匹配
date = soup_match.group(1)
name = soup.find(class_ = 'c-article-info-details').get_text().split('\n')[1]
title = soup.find(class_ = 'c-article-title u-h1').get_text().split('\n')[0]

import pandas as pd
dt = pd.read_table('/Users/tongxueer/Documents/文献/IF_2019.txt', index_col = 1)
IF_dict = dt['Journal Impact Factor'].to_dict()
for x in IF_dict:
    match = re.search(name, x, flags=re.IGNORECASE)
    if match:
        IF = IF_dict[x]
        
print(title)        
print(name + ' | IF:' + IF  + ' | Date ' + date )
