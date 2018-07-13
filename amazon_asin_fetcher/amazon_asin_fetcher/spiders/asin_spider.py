# *-* coding: utf-8 *-*
"""
Created on: 5-Jul-2018

@author: Ai
"""
import scrapy
from googletrans import Translator


class ASINSpider(scrapy.Spider):
    name = "asin"

    def __init__(self, store=None, key=None, *args, **kwargs):
        super(ASINSpider, self).__init__(*args, **kwargs)
        if not store:
            raise Exception('store is required')

        self.start_urls = ['https://www.{0}/s/?keywords={1}'.format(store, key)]

    def parse(self, response):
        for item in response.css('li.s-result-item'):
            if item.css('h2::attr(data-attribute)').extract_first() is not None:
                gt = Translator()
                yield {
                        'ASIN': item.css('li::attr(data-asin)').extract_first(),
                        'Product': gt.translate(item.css('h2::attr(data-attribute)').extract_first()).text
                        }

        next_page = response.css('a[id="pagnNextLink"]::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
