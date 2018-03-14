import pymysql

# 配置数据库
connection = pymysql.connect(
  host='localhost',
  user='root',
  password='root',
  db='lagou',
  charset='utf8',
)
# 获取游标
# 编写sql函数
def storageData(job,workYear,education,salary,companyFullName,city,stationname,industryField,companySize):
  print(job)
  with connection.cursor() as cursor:
    sql=" INSERT INTO  `lagou`(job,workYear,education,salary,companyFullName,city,stationname,industryField,companySize) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,(job,workYear,education,salary,companyFullName,city,stationname,industryField,companySize))
    connection.commit()
