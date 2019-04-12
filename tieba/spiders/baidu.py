# -*- coding: utf-8 -*-
import scrapy
from tieba.items import TiebaItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=%E6%B7%B1%E5%9C%B3']
    url_set = set()

    def parse(self, response):
        Tiezi = response.xpath('//div[contains(@class,"threadlist_title")]')
        pre = 'http://tieba.baidu.com'
        i = 0
        for post in Tiezi:
            if i>2:
                item = TiebaItem()
                name = post.xpath('./a/@title').extract()[0]
                url = pre + post.xpath('./a/@href').extract()[0]
                item['name'] = name
                item['url'] = url
                yield item
            i += 1
        urls = response.xpath('//a[contains(@class,"pagination-item")]/@href').extract()
        i = 0
        for u in urls:
            if i>1:
                break
            u = 'http:' + u
            if u in BaiduSpider.url_set:
                pass
            else:
                BaiduSpider.url_set.add(u)
                yield self.make_requests_from_url(u)
            i += 1

