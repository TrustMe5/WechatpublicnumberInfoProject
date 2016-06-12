# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# class WechatprojectPipeline(object):
#     def process_item(self, item, spider):
#         return item



# # MySQL Database
# from twisted.enterprise import adbapi  # import twisted package
# class WechatprojectPipeline(object):
#     # connnect databases
#     def __init__(self):
#         self.dbpool = adbapi.ConnectionPool("MySQLdb",
#                                             host = "localhost",
#                                             db = "testwechat", # you must build database named testwechat
#                                             user = "root",
#                                             passwd = "fireling",
#                                             charset = "utf8")
#     # pipeline default function
#     def process_item(self, item, spider):
#         query = self.dbpool.runInteraction(self._conditional_insert, item)
#         return item
#     # insert the data to databases
#     def _conditional_insert(self, tx, item): # item dictionary
#         # you must build table named result in database testwechat
#         tx.execute("insert into result values (%s, %s, %s)", (item["title"], item["link"], item["content"]))


# MongoDB Database
#import pymongo
#class WechatprojectPipeline(object):
#    # connnect databases
#    def __init__(self):
#        connection = pymongo.Connection(host = "localhost", port = 27017)
#        db = connection["testwechat"] # you need no build database named testdouban
#        # db.authenticate(name = "root", password = "fireling") # no name and password for localhost
#        self.posts = db["result"] # you need not build collection named book
#    # pipeline default function
#    def process_item(self, item, spider):
#        self.posts.insert(dict(item)) # convert json to dict
#        return item
#

# # Json File
#import json
#import pandas as pd
#import numpy as np
import csv
import sys
reload(sys) 
sys.setdefaultencoding( "utf-8"  )
class WechatprojectPipeline(object):
    def __init__(self):
        self.file =open('processing.csv','a')
    def process_item(self, item, spider):
        open_file_object=csv.writer(self.file)
        open_file_object.writerow([item["username"],item["intro"],item["link"]])
     #   line = json.dumps(dict(item))+'\n'
     #   title=item['title']
     #   link=item['link']
     #   content=item['content']
     #   pd.read_excel('data1.xlsx').columes=['1','2','3','4']
     #   self.file.write(line.decode("unicode_escape"))
        return item


#############################################################################################
# '''if you want to download images'''
# from scrapy.http.request import Request
# from scrapy.contrib.pipeline.images import ImagesPipeline
# class MyImagesPipeline(ImagesPipeline):
#     #@TODO
#     def get_media_requests(self, item, info):
#         for image_url in item['image_urls']: # item['image_urls'] contains the image urls
#             # yield Request(image_url)
#             yield Request(image_url, meta={'name': item['name']}) # item['name'] contains the images name
#     def item_completed(self, results, item, info):
#         return super(MyImagesPipeline, self).item_completed(results, item, info)
#     def file_path(self, request, response=None, info=None):
#         f_path = super(MyImagesPipeline, self).file_path(request, response, info)
#         f_path = f_path.replace('full', request.meta['name'])
#         return f_path
#         ##########################################################
#         # import hashlib
#         # image_guid = hashlib.sha1(request.url).hexdigest()  # change to request.url after deprecation
#         # return '%s/%s.jpg' % (request.meta['name'], image_guid)
#     pass
# # from scrapy.contrib.pipeline.media import MediaPipeline
# # class MyMediaPipeline(MediaPipeline):
# #     #@TODO
# #     pass

