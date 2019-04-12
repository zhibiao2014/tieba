# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import json
import pymysql
from tieba.ext.DataBaseHandle import DataBaseHandle

class TiebaPipeline(object):
    def process_item(self, item, spider):
        r = redis.Redis(host='127.0.0.1',port=6379,db=0)
        # r.lpush('urls',item['url'])
        # db = pymysql.connect("my3766615.xincache2.cn","my3766615","biao2016","my3766615")
        # db = pymysql.connect("127.0.0.1","root","123456","my3766615")
        # cursor = db.cursor()
        # cursor.execute('select * from wp_users where ID = 1')
        # data = cursor.fetchall()
        # print(data)
        # cursor.close()
        # db.close()
        res = self.has_iset(item['url'])
        print(res)
        if not(res):
            r.lpush('urls',item['url'])

        return item

    def has_iset(self,url):
        db = DataBaseHandle("my3766615.xincache2.cn","my3766615","biao2016","my3766615",3306)
        res = db.selectDb('select * from wp_posts where url = '+url)
        return res

class DiscuzPipeline(object):
    def process_item(self, item, spider):
        r = redis.Redis(host='127.0.0.1',port=6379,db=0)
        # r.lpush('urls',item['url'])
        # db = pymysql.connect("my3766615.xincache2.cn","my3766615","biao2016","my3766615")
        # db = pymysql.connect("127.0.0.1","root","123456","my3766615")
        # cursor = db.cursor()
        # cursor.execute('select * from wp_users where ID = 1')
        # data = cursor.fetchall()
        # print(data)
        # cursor.close()
        # db.close()
