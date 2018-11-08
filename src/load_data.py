"""
读取txt中的json新闻语料
title: 新闻标题
html: 新闻正文
time: 新闻时间
url: 原文所在url
time和url均可以过滤掉
使用str将json数据转换为dic
将dic写入文件
fw = open("test.txt",'w+')
fw.write(str(dic))      #把字典转化为str
fw.close()

"""
import re
import os
from src import Chinese_range


# test
# pattern = r' +|,|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)' \
#           r'|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）|《|》|：|“|”|？+|/|（|）'
# data = '你们好，我是     你们的好朋友!哈哈哈'
# result_list = re.split(pattern, data)
# print(result_list)
#
# with open(r'D:\人工智能\46540423_1_拼音输入法作业\拼音输入法作业\sina_news_gbk\2016-02.txt', 'r', encoding='gbk') as file:
#     content = file.readlines()
#     count = 0
#     for line in content:
#         count = count + 1
#         dic = eval(line)    #将str转为dic
#         print(dic['title'], ' ', dic['html'])
#         if count == 10:
#             break

def load_train_data(file_path):
    #用来分割句子，第一个是空格，以一个或多个空格分割字符串
    pattern = r' +|,|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)' \
              r'|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）|《|》|：|“|”|？+|/|（|）' \
              r'|[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'

    train_data = []
    with open(file_path, 'r', encoding='gbk') as file:
        content = file.readlines()
        for line in content:
            dic = eval(line)
            str1 = dic['title'] + ' ' + dic['html']   #过滤掉time和url
            str1 = ' '.join(re.split(pattern, str1))
            # str1 = str1 + '\n'
            train_data.append(str1)

    Chinese_range.dic3(train_data=train_data)
    print(file_path, '训练成功')




if __name__ == '__main__':
    file_prefix = r'D:\人工智能\46540423_1_拼音输入法作业\拼音输入法作业\sina_news_gbk'
    file_date = r'2016-'
    file_suffix = r'.txt'
    index = [2, 4, 5, 6, 7, 8, 9, 10, 11]

    for i in index:
        if i < 10:
            i = str(0) + str(i)
        file_path = file_prefix + '\\' + file_date + str(i) + file_suffix
        load_train_data(file_path)




