import scrapy
from scrapy.crawler import CrawlerProcess
import xlsxwriter

from ..items import DataextractionItem


class Blackcoffer(scrapy.Spider):
    name = 'coffer'

    start_urls = [line.strip() for line in open('Input.csv', encoding="cp437", errors='ignore').readlines()]
    # start_urls = [
    #     'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/'
    # ]
    print('start_urls: ',start_urls)

    def parse(self, response, **kwargs):
        items = DataextractionItem()
        # print('start_urls= ',self.start_urls)
        items['url'] = response.request.url
        items['title'] = response.css('title::text').extract()
        items['text'] = response.xpath('//p/text() | //p/strong/text()').extract()
        yield items