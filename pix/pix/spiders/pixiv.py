import json

import scrapy
from scrapy.selector import Selector

from pix.items import PixItem


class PixivSpider(scrapy.Spider):
    name = 'pixiv'
    allowed_domains = ['www.pixiv.net']
    start_urls = ['https://www.pixiv.net/ranking.php?']
    def start_requests(self):
        for i in range(1, 2):
            url = f"https://www.pixiv.net/ranking.php?p={i}&format=json"
            yield scrapy.Request(url)
    def parse(self, response):
        text = response.text
        dump =json.loads(text)
        for m in dump['contents']:
            image_url = m["url"]
            yield {'image_urls': [image_url]}