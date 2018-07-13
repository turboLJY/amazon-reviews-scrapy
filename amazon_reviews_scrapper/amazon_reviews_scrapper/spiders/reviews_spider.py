# *-* coding: utf-8 *-*
"""
Created on: 5-Jul-2018

@author: Ai
"""
import scrapy
from googletrans import Translator


class AmazonReviewsSpider(scrapy.Spider):
    name = 'amazon-reviews-spider'

    def __init__(self, store=None, product_id=None, *args, **kwargs):
        super(AmazonReviewsSpider, self).__init__(*args, **kwargs)
        self.product_id = product_id
        self.store = store
        if not self.product_id:
            raise Exception("product_id is required")
        if not self.store:
            raise Exception("store is required")

        self.start_urls = ['https://www.{0}/product-reviews/{1}/ref=dpx_acr_txt?showViewpoints=1'.format(self.store, self.product_id)]

    def parse(self, response):
        for item in response.css('.a-section.review'):
            if item.css('div::attr(data-hook)').extract_first() == 'review':
                gt = Translator()
                yield {
                        'Store': self.store,
                        'Product_ID': self.product_id,
                        'Review_ID': item.css('div.a-section.celwidget::attr(id)').extract_first().split('-')[1],
                        'Date': gt.translate(item.css('[data-hook="review-date"]::text').extract_first()).text,
                        'Stars': gt.translate(item.css('a::attr(title)').extract_first()).text,
                        'Review_Title': gt.translate(item.css('[data-hook="review-title"]::text').extract_first()).text,
                        'Author': item.css('[data-hook="review-author"]::text').extract_first(),
                        'Review': gt.translate(' '.join(item.css('span.review-text::text').extract())).text,
                        'Helpful_Count': gt.translate(item.css('div.a-row.a-spacing-base > span::text').extract_first()).text
                        }

        next_page = response.css('.a-last > a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
