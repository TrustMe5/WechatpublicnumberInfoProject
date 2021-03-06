#coding: utf-8
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from Wechatproject.items import WechatprojectItem
from bs4 import BeautifulSoup
from scrapy.http import Request
import pandas as pd
import numpy as np
import xlrd
  
class WechatSpider(BaseSpider):
    #############################################################################################
    '''微信搜索程序'''
    name = "Wechatproject"
    data=pd.read_excel("data.xlsx",index_col=None,header=0)
    data.columns=['1','2','3','4']
    #data=data.rename(columns={col_name:'new_name'})
    #data=data[data.D.notnull()] 

    start_urls = []
    print 'len(data)',len(data['4'])
    print "data['4'][0]:",data['4'][0]
    i=0
    for weixinid in data['4']:
        if weixinid is not None:
            print 'weixinid:',weixinid
            start_urls.append("http://weixin.sogou.com/weixin?type=1&query=%s&page=1"%weixinid)


    def parse(self, response):
        print response.body
        sel = Selector(response)
        site = sel.xpath('//div[@id="sogou_vr_11002301_box_0"]')
        #soup=BeautifulSoup(response.body)
        #tag=soup.find("div",attrs={"id":"sogou_vr_11002301_box_0"})
        #for site in sites:
        item = WechatprojectItem()
        #username = site.xpath('div[@class="txt-box"]/h3/em/text()').extract() # 其中在item.py中定义了title = Field()
        #item["username"]="".join(username)
        link = site.xpath("@href").extract() # 其中在item.py中定义了link = Field()
        item["link"] = "".join(link) # 其中在item.py中定义了link = Field()
        next_url = item["link"]
        yield Request(url=next_url, meta={"item":item}, callback=self.parse2) ## 抓取当前页数和二级页面数据

    def parse2(self, response):
        soup = BeautifulSoup(response.body)
        weixinnametag=soup.find("strong",attrs={"class":"profile_nickname"})
        weixinname=weixinnametag.get_text()
        print "weixinname:",weixinname
        introtag=soup.find("div",attrs={"class":"profile_desc_value"})
        intro ="".join(introtag.get_text()) 

        #content='haha'
        # print content
        # item = WechatprojectItem()
        item = response.meta['item'] 
        item["username"]=weixinname
        item["intro"] =intro
        return item
