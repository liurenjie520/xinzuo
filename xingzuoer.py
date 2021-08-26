# -*- coding: utf-8 -*-
"""
Created on 2019/1/18 16:41
@Author: Johnson
@Email:593956670@qq.com
@File: 星座.py
"""
import datetime

import requests
from lxml.html import etree
import json
import time        # 导入模块
from datetime import date, timedelta

# 星座运势







def tody():
   requests.packages.urllib3.disable_warnings()
   now_time = datetime.datetime.now()
   d = datetime.datetime.now().strftime('%Y%m%d')
   response = requests.get('https://www.xzw.com/fortune/capricorn/%s.html' % d, verify=False)
   if not response.status_code == 200:
      print('星座运势请求错误：' + str(response.status_code))
   sel = etree.HTML(response.text)
   today1 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[0]
   today2 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[1]
   today3 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[2]
   today4 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[3]
   today5 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[4]
   jiankanzhishu = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[0]  #健康指数：-商谈指数：-幸运颜色：-幸运数字：速配星座：短评：
   luckcoler = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[2]
   lucknum = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[3]
   supei = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[4]
   duanpin= sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[5]

   s1="健康指数:"+jiankanzhishu+"\n幸运颜色:"+luckcoler+"\n幸运数字:"+lucknum+"\n速配星座:"+supei+"\n短评:"+duanpin+"\n综合运势:\n"+today1+"\n爱情运势:\n"+today2+"\n事业运势:\n"+today3+"\n财富运势:\n"+today4+"\n健康运势:\n"+today5+"\n"
   return s1



def tomorrow():
   tomorrow = (date.today() + timedelta(days=1)).strftime("%Y%m%d")
   # print(tomorrow)
   requests.packages.urllib3.disable_warnings()
   response = requests.get('https://www.xzw.com/fortune/capricorn/%s.html' % tomorrow, verify=False)
   # print(response.text)
   if not response.status_code == 200:
      print('星座运势请求错误：' + str(response.status_code))
   sel = etree.HTML(response.text)
   today1 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[0]
   today2 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[1]
   today3 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[2]
   today4 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[3]
   today5 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[4]
   jiankanzhishu = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[0]  #健康指数：-商谈指数：-幸运颜色：-幸运数字：速配星座：短评：
   luckcoler = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[2]
   lucknum = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[3]
   supei = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[4]
   duanpin= sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[5]

   tm20="健康指数:"+jiankanzhishu+"  幸运颜色:"+luckcoler+"  幸运数字:"+lucknum+"  速配星座:"+supei+"  短评:"+duanpin
   tm21="『综合运势:"+today1+"』  『爱情运势:"+today2+"』  『事业运势:"+today3+"』  『财富运势:"+today4+"』  『健康运势:"+today5+"』"

   requests.packages.urllib3.disable_warnings()
   now_time = datetime.datetime.now()
   d = datetime.datetime.now().strftime('%Y%m%d')
   response = requests.get('https://www.xzw.com/fortune/capricorn/%s.html' % d, verify=False)
   if not response.status_code == 200:
      print('星座运势请求错误：' + str(response.status_code))
   sel = etree.HTML(response.text)
   today1 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[0]
   today2 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[1]
   today3 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[2]
   today4 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[3]
   today5 = sel.xpath('//div[@class="c_box"]/div[@class="c_cont"]/p/span/text()')[4]
   jiankanzhishu = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[0]  # 健康指数：-商谈指数：-幸运颜色：-幸运数字：速配星座：短评：
   luckcoler = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[2]
   lucknum = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[3]
   supei = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[4]
   duanpin = sel.xpath('//div[@class ="c_main"]/dl/dd/ul/li/text()')[5]

   am20="健康指数:"+jiankanzhishu+"  幸运颜色:"+luckcoler+"  幸运数字:"+lucknum+"  速配星座:"+supei+"  短评:"+duanpin
   am21="『综合运势:"+today1+"』  『爱情运势:"+today2+"』  『事业运势:"+today3+"』  『财富运势:"+today4+"』  『健康运势:"+today5+"』"



   last = "[('" + d+ "','" + am21 + "','" + am20 + "'),('" + tomorrow+ "','" + tm21 + "','" + tm20 + "')]"
   dicee = eval(last)
   return dicee



#
# def zz():
#    now_time = datetime.datetime.now()
#    d = datetime.datetime.now().strftime('%Y%m%d')
#    # d=str(d)
#    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y%m%d")
#    # tomorrow=str(tomorrow)
#    # tody233=tody()
#    # tomorrow233=tomorrow()
#    sttt="[('"+d+"','"+str(tody())+"'),('"+tomorrow+"','"+str(tomorrow())+"')]"
#    print(sttt)
#    return sttt

if __name__ == '__main__':
    print(tomorrow())
