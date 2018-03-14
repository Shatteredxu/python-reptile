# python-reptile 爬虫项目
## lagou文件夹为爬取拉钩网的岗位信息以及分析
### lagou.py文件为爬虫代码
利用request库请求，json模块解析数据拿到我们想要的数据
pymysql链接mysql作数据存储，同时存储在csv文件中
可以通过更改lagou.py中的title来更改其他职位，这里用的是python
### analysis.py为数据分析代码
利用pandas 做数据统计分析
matplotlib生成统计图像，然后存储为文件，
效果如下
![城市分布](https://github.com/Shatteredxu/python-reptile/blob/master/城市分布.jpg)
![经验要求](https://github.com/Shatteredxu/python-reptile/blob/master/经验要求.png)
![学历要求](https://github.com/Shatteredxu/python-reptile/blob/master/学历要求.png)
![职位名称](https://github.com/Shatteredxu/python-reptile/blob/master/职位名称.png)
lagou.py文件为sql语句文件，通过调用这个文件中的sql语句来实现mysql的存储，
以下为表结构以及表中的数据
![表结构](https://github.com/Shatteredxu/python-reptile/blob/master/表结构.png)
![存储数据](https://github.com/Shatteredxu/python-reptile/blob/master/存储数据.png)
