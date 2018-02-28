# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request.form import FormRequest


class DatalistSpider(scrapy.Spider):
    name = 'datalist'
    allowed_domains = ['wellsfargo.com']
    start_urls = ['https://www.wellsfargo.com/savings-cds/rates/']

    def parse(self, response):

        return [FormRequest.from_response(response,
                    formdata={'zipCodeSelector':'10004'}, method='POST',
                    callback=self.after_login)]


    def after_login(self, response):
        scrapy.Request(url='https://www.wellsfargo.com/savings-cds/rates/')
        yield {
            'product_name' : response.css('.subhead h3::text').extract_first()
        }
