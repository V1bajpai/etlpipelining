from scrapy.crawler import CrawlerProcess

from dataextraction.dataextraction.spiders.blackcoffer_spider import Blackcoffer


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(Blackcoffer)
    process.start()
