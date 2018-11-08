"""
实现拼音转汉字的动态规划算法
使用动态规划的算法，需要在某一列保存上一列到这一列某个值的最短路径，以及最短路径的上一列节点
数据结构：两个矩阵，一个矩阵是起点到每一列每个值的最大值，一个矩阵是该列最大值对应的上一类的节点行号
矩阵维度：根据拼音串的长度确定矩阵的列数，根据所有拼音串下的最大字符个数确定行数
"""
import os
import numpy as np

def pinyin2hanzi(input):
    file_path1 = os.path.join(os.getcwd() + '/../dic_data/dic1.txt')
    file_path2 = os.path.join(os.getcwd() + '/../dic_data/dic4.txt')

    with open(file_path1, 'r', encoding='gbk') as file1, open(file_path2, 'r', encoding='gbk') as file2:
        dic1 = eval(file1.read())
        dic4 = eval(file2.read())

    hanzi = []
    for line in input:
        words = line.split(' ')
        if '\n' in words[-1]:
            words[-1] = words[-1].replace('\n', '')
        column = len(words) #得到矩阵的列
        row = max(len(dic1[i]) for i in words)
        matrix1 = np.zeros((row, column))
        matrix1[:, 0] = 1
        matrix2 = np.zeros((row, column))
        length = len(words) - 1
        for i in range(length):
            column_pre = dic1[words[i]] #前一列拼音下的所有汉字
            column_next = dic1[words[i+1]]  #后一列拼音下的所有汉字

            length1 = len(column_pre)
            length2 = len(column_next)
            for j in range(length2):
                max_value = 0
                pre_index = 0
                for k in range(length1):
                    key = column_pre[k] + column_next[j]
                    value = dic4[key] * matrix1[k, i]
                    if max_value < value:
                        max_value = value
                        pre_index = k
                matrix1[j, i+1] = max_value
                matrix2[j, i+1] = pre_index









if __name__ == '__main__':
    # input_file = r'C:\Users\Administrator\PycharmProjects\PinYin\input_data\input.txt'
    # output_file = r'C:\Users\Administrator\PycharmProjects\PinYin\output_data\output.txt'
    #
    # with open(input_file, 'r') as file1: #open(output_file, 'w', encoding='gbk') as file2:
    #     input = file1.readlines()
    #     pinyin2hanzi(input)

    matrix = np.zeros((3, 4))
    matrix[:, 0] = 1
    print(matrix[1, 0])
