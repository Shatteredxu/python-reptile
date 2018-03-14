# -*- coding:utf-8 -*-
import  requests
from lxml import etree
import json
from lagousql import *
import random,time
import pandas as pd
class laGou:
  # 初始化
  def __init__(self):
    self.url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0"
    header = {'Host': 'www.lagou.com',
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
              'Accept': 'application/json, text/javascript, */*; q=0.01',
              'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
              'Accept-Encoding': 'gzip, deflate, br',
              'Referer': 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'X-Requested-With': 'XMLHttpRequest',
              'X-Anit-Forge-Token': 'None',
              'X-Anit-Forge-Code': '0',
              'Content-Length':'26',
              'Cookie': 'gsScrollPos - 594 = 0;_ga = GA1.2.1763266351.1514965715;user_trace_token = 20180103154835 - 807219e8 - f05a - 11e7 - ba74 - 525400f775ce;LGUID = 20180103154835 - 8072227e - f05a - 11e7 - ba74 - 525400f775ce;_gid = GA1.2.1620992646.1520753677;Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6 = 1520753677;X_HTTP_TOKEN = e2c2ff7dadb1f63364241194d87b4adc;_putrc = 3A1FB4308F498309;JSESSIONID = ABAAABAAADEAAFI4736209D8C7E23A4F058AB489EB85269;login = true;unick = % E5 % BE % 90 % E4 % BC % 9F % E6 % 9D % B0;showExpriedIndex = 1;showExpriedCompanyHome = 1;showExpriedMyPublish = 1;hasDeliver = 0;gate_login_token = 05c020c7042c891db35d22571a72e63405f828b6c3229f29;index_location_city = % E5 % 85 % A8 % E5 % 9B % BD;hideSliderBanner20180305WithTopBannerC = 1;TG - TRACK - CODE = index_hotsearch;Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6 = 1520755409;LGRID = 20180311160326 - ad64f33c - 2502 - 11e8 - b1ab - 5254005c3644;SEARCH_ID = 09521d0c3dc743f9a6a3ab451a5a8ea2',
              'Connection': 'keep-alive',
              'Pragma': 'no-cache',
              'Cache-Control': 'no-cache'}
    self.headers = header
    # 请求页面，存储数据
  def loadPage(self,pn = None,title=None):
    if pn :
      params = {'first': 'false', 'pn': pn,'kd':title}
      req = requests.post(self.url,data=params,headers=self.headers)
      hjson = json.loads(req.text)
      arr = hjson["content"]["positionResult"]["result"]
      dict=[]
      for v in arr:
        # 储存在数据库中
        # storageData(v["positionName"],v["workYear"],v["education"],
        #             v["salary"],v["companyFullName"],v["city"],v["stationname"],
        #             v["industryField"],v["companySize"]
        #            )
        # 保存在csv文件中
        # pd.DataFrame(pd.)
        #   print(v)
        list={"positionName":v["positionName"],"workYear":v["workYear"],"education":v["education"],
              "salary":v["salary"],"companyFullName":v["companyFullName"],"city":v["city"],
              "stationname":v["stationname"], "industryField":v["industryField"],"companySize":v["companySize"]}
        dict.append(list)
        # 存储到csv文件中去
      data = pd.DataFrame(dict)
      data.to_csv(r'D:\LaGouDataMatlab.csv', header=False, index=False, mode='a+')
  def start(self):
    for pn in range(30):
      self.loadPage(pn,title='python')
      time.sleep(random.randint(2, 5))

if __name__ == "__main__":
  lg = laGou()
  lg.start()


