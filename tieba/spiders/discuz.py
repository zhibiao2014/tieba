# -*- coding: utf-8 -*-
import scrapy
import redis
from tieba.items import DiscuzItem


class DiscuzSpider(scrapy.Spider):
    name = 'discuz'
    allowed_domains = ['baidu.com']
    r = redis.Redis(host='127.0.0.1',port=6379,db=0)
    u = r.lpop('urls').decode('utf-8')
    start_urls = [u]
    url_set = set()

    def parse(self, response):
        Tiezi = response.xpath('//div[contains(@class,"l_post")]')
        i = 0
        for discuz in Tiezi:
            item = DiscuzItem()
            content = discuz.xpath('//div[contains(@class,"d_post_content j_d_post_content  clearfix")]').extract()[i]
            item['content'] = content
            item['url'] = self.u
            print(i)
            print(content)
            i += 1
            yield item
        urls = response.xpath('//li[contains(@class,"l_pager pager_theme_4 pb_list_pager")]').extract()
        print(urls)
