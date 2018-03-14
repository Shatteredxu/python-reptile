# -*- coding = utf8 -*-
import matplotlib.pyplot  as plt
from wordcloud import WordCloud,ImageColorGenerator
import jieba
import matplotlib as mpl
from pyecharts import Geo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

mpl.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.labelsize"]=16
plt.rcParams["xtick.labelsize"]=14
plt.rcParams["ytick.labelsize"]=14
plt.rcParams["legend.fontsize"]=12
plt.rcParams["figure.figsize"]=[15,15]

# 数据预览
data = pd.read_csv(r'D:\LaGouDataMatlab.csv',encoding='gbk')

# data["学历要求"].value_counts().plot(kind='barh',rot=0)
# plt.show()

# data['工作要求'].value_counts().plot(kind='bar',rot=10,color='palegreen')
# plt.show()

# # 词云展示
# final = ''
# stopWords = ['python','工程师','Python','-',"(",")","/","()"]
# # print(data.shape[0])
# for n in range(data.shape[0]):
#   word_list = list(jieba.cut(data["职位名称"][n]))
#   for word in word_list:
#     if word not in stopWords:
#       final = final+word+" "
# print(final)
# image = plt.imread("3.png")
# grapy = np.array(image)
# wc = WordCloud( font_path=r"C:\Windows\Fonts\simfang.ttf", width=1000, height=1000).generate(final)
# image_color = ImageColorGenerator(image)
#
# plt.imshow(wc)
# plt.axis("off")
# plt.show()
# wc.to_file("1.png")
# explode = np.linspace(0,1.5,num=data['城市'].value_counts().shape[0])
# sizes = [15,30,45,10]
# data['城市'].value_counts().plot(kind='pie',autopct='%1.2f%%',explode=explode)
# plt.axis('equal')
# plt.savefig("20.jpg")
# plt.show()