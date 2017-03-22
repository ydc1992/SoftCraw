# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http.request import Request
import urlparse,scrapy

class Softitem(scrapy.Item):
    file_urls = scrapy.Field()

class DeepSpider(CrawlSpider):
    name = "Deep"

    def __init__(self,rule):
        self.rule = rule
        self.allow_domains = rule.allow_domains.split(",")
        self.start_urls = rule.start_urls.split(",")

        rule_list = []
        a = rule.extract_from
        rule_list.append(
                Rule(LxmlLinkExtractor(allow=a), callback='parse_item')
                     )
        self.rules = tuple(rule_list)
        super(DeepSpider, self).__init__()

    def parse_item(self, response):
        m_xpath = self.rule.download_xpath.split(";")

        download_url = response.xpath(m_xpath[0]).extract()
        for u in download_url:
            yield Request(urlparse.urljoin(response.url,u),callback=self.parse_downurl,meta={"xpath":m_xpath})

    def parse_downurl(self,response):
        try:
            xpath = response.meta["xpath"]
            downurl = response.xpath(xpath[1]).extract()
            item = Softitem()
            item['file_urls']=[downurl[0],]
            return item
        except Exception,e:
            print e