'''
准备创建多个dic
dic1:拼音-汉字list
dic2:汉字-以该汉字开头的二元组的个数
dic3:汉字二元组-个数
dic4:汉字二元组-概率
dic4可以通过dic3/dic2得到
最后的动态规划算法怎么使用到这些数据呢？
通过dic1找到前一个拼音和后一个拼音对应的汉字，将该汉字组合
通过dic4（汉字组合）的找到相应的概率
然后再使用动态规划的算法

'''

import os
import re
#
# print(os.getcwd())
#
# #设置相对路径
# file_path1 = os.path.join(os.getcwd() + '/../train_data/拼音汉字表.txt')
# file_path2 = os.path.join(os.path.dirname(__file__) + '/../train_data/一二级汉字表.txt')
# file_path3 = os.path.join(os.path.dirname(__file__) + '/../train_data/Chinese.txt')
#
# with open(file_path1, 'r', encoding='gbk') as file1, open(file_path2, 'r', encoding='gbk') as file2, \
#         open(file_path3, 'w', encoding='utf-8') as file3:
#     lines = file1.readlines()
#     content = file2.read()
#     # print(len(content)) 6763
#     # print(type(content)) str
#     content = list(content)
#     for line in lines:
#         line1 = line.split(' ')
#         a = line1[0]
#         length = len(line1)
#         for i in range(1, length):
#             if line1[i] in content:
#                 a = a + ' ' + line1[i]
#         a = a + '\n'
#         print(a)
#         # file3.write(a)

def dic1():
    dic = {}
    #设置相对路径
    file_path1 = os.path.join(os.getcwd() + '/../train_data/拼音汉字表.txt')
    file_path2 = os.path.join(os.getcwd() + '/../dic_data/dic1.txt')
    with open(file_path1, 'r', encoding='gbk') as file:
        lines = file.readlines()
        for line in lines:
            line_list = line.split(' ')
            dic[line_list[0]] = line_list[1:]

    with open(file_path2, 'w', encoding='gbk') as file:
        content = str(dic)
        file.write(content)



def dic2():
    file_path1 = os.path.join(os.getcwd() + '/../dic_data/dic1.txt')
    file_path2 = os.path.join(os.getcwd() + '/../dic_data/dic2.txt')
    dic2 = {}

    with open(file_path1, 'r', encoding='gbk') as file:
        dic1 = eval(file.read())
        for key in dic1:
            # print(type(dic1[key]))   #list
            line = dic1[key]
            for i in line:
                if '\n' in i:
                    i = i.replace('\n', '')
                dic2[i] = 0

    with open(file_path2, 'w', encoding='gbk') as file:
        content = str(dic2)
        file.write(content)

#测试训练是否成功
def dic3():
    dic3 = {}
    file_path1 = r'C:\Users\Administrator\PycharmProjects\PinYin\train_data\train1.txt'
    file_path2 = os.path.join(os.getcwd() + '/../train_data/一二级汉字表.txt')
    file_path4 = os.path.join(os.getcwd() + '/../dic_data/dic2.txt')
    pattern = ' +|[a-zA-Z0-9]+'
    with open(file_path1, 'r', encoding='gbk') as file1, open(file_path2, 'r', encoding='gbk') as file2,\
            open(file_path4, 'r', encoding='gbk') as file4:
        dic2 = eval(file4.read())
        train_data = file1.readlines()
        chinese = file2.read()
        for data in train_data:
            datas = re.split(pattern, data)
            for part in datas:
                length = len(part)-1
                for i in range(length):
                    if part[i] in chinese and part[i+1] in chinese: #如果是要识别的字符
                        key = part[i] + part[i+1]
                        if key in dic3.keys():
                            dic3[key] = dic3[key] + 1
                        else:
                            dic3[key] = 1
                        dic2[part[i]] = dic2[part[i]] + 1   #以该汉字开头的词个数+1

    file_path3 = os.path.join(os.getcwd() + '/../dic_data/dic3.txt')
    with open(file_path3, 'w', encoding='gbk') as file1, open(file_path4, 'w', encoding='gbk') as file2:
        content1 = str(dic3)
        file1.write(content1)

        content2 = str(dic2)
        file2.write(content2)


#需要将训练语料传进来，并进行训练，train_data应该是list类型，每一个元素是一条训练的语料
def dic3(train_data):
    dic3_back = {}
    dic2_back = {}
    try:
        #先获得dic3
        file_path1 = os.path.join(os.getcwd() + '/../dic_data/dic3.txt')
        with open(file_path1, 'r', encoding='gbk') as file:
            dic3 = eval(file.read())

        #发生异常时，用于数据回滚
        dic3_back = dic3

        #训练数据
        file_path2 = os.path.join(os.getcwd() + '/../train_data/一二级汉字表.txt')
        file_path4 = os.path.join(os.getcwd() + '/../dic_data/dic2.txt')
        pattern = ' +|[a-zA-Z0-9]+'
        with open(file_path2, 'r', encoding='gbk') as file2, open(file_path4, 'r', encoding='gbk') as file4:
            dic2 = eval(file4.read())
            #数据备份，用以回滚
            dic2_back = dic2
            chinese = file2.read()
            for data in train_data:
                try:
                    datas = re.split(pattern, data)
                    for part in datas:
                        length = len(part)-1
                        for i in range(length):
                            if part[i] in chinese and part[i+1] in chinese: #如果是要识别的字符
                                key = part[i] + part[i+1]
                                if key in dic3.keys():
                                    dic3[key] = dic3[key] + 1
                                else:
                                    dic3[key] = 1
                                dic2[part[i]] = dic2[part[i]] + 1   #以该汉字开头的词个数+1
                except:
                    print(data)
                    continue

        #更新内容
        with open(file_path1, 'w', encoding='gbk') as file1, open(file_path4, 'w', encoding='gbk') as file2:
            content1 = str(dic3)
            file1.write(content1)

            content2 = str(dic2)
            file2.write(content2)
    except:
        #训练出错的话，数据回滚
        file_path1 = os.path.join(os.getcwd() + '/../dic_data/dic3.txt')
        file_path4 = os.path.join(os.getcwd() + '/../dic_data/dic2.txt')
        with open(file_path1, 'w', encoding='gbk') as file, open(file_path4, 'r', encoding='gbk') as file1:
            file.write(str(dic3_back))
            file1.write(str(dic2_back))
        print('训练出错')
    else:
        print('训练成功')


def dic4():
    file_path1 = os.path.join(os.getcwd() + '/../dic_data/dic2.txt')
    file_path2 = os.path.join(os.getcwd() + '/../dic_data/dic3.txt')
    file_path3 = os.path.join(os.getcwd() + '/../dic_data/dic4.txt')
    dic4 = {}

    with open(file_path1, 'r', encoding='gbk') as file1, open(file_path2, 'r', encoding='gbk') as file2:
        dic2 = eval(file1.read())
        dic3 = eval(file2.read())

        for key in dic3.keys():
            dic4[key] = round(float(dic3[key])/dic2[key[0]], 6) #p(wi|wi-1)，结果只保留6位小数

    with open(file_path3, 'w', encoding='gbk') as file:
        content = str(dic4)
        file.write(content)


#重新生成dic2和dic3，因为训练过程中可能会出错
def clear_dic2and3():
    dic2()
    file_path = os.path.join(os.getcwd() + '/../dic_data/dic3.txt')
    with open(file_path, 'w', encoding='gbk') as file:
        file.write('')
    print('dic2和dic3已经重新生成')


#测试文件写
def write_txt():
    file_path = r'C:\Users\Administrator\PycharmProjects\PinYin\train_data\text.txt'
    a = ''
    with open(file_path, 'r', encoding='gbk') as file:
        a = file.read()
        a = int(a)
    print(a)

    with open(file_path, 'w', encoding='gbk') as file:
        a = a + 1
        file.write(a)


if __name__ == '__main__':
    #test
    # line = '你们好 哈哈哈 test'
    # line_list = line.split(' ')
    # print(line_list[1:])

    # dic1()
    # dic2()
    # dic3()
    # dic4()

    #test
    # write_txt()
    # clear_dic2and3()
    # with open(r'C:\Users\Administrator\PycharmProjects\PinYin\dic_data\dic3.txt', 'r', encoding='gbk') as file:
    #     dic = eval(file.read())
    #     print(dic)

    #得到最终结果
    dic4()