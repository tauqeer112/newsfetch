# -*- coding: utf-8 -*-
import scrapy


class NewsfetchItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()


class ThehinduSpider(scrapy.Spider):
    name = "thehindu"
    allowed_domains = ["www.thehindu.com"]
    start_urls = ['http://www.thehindu.com/']

    def parse(self, response):
        list = []
        list1 = (response.xpath('//h1/a[@href]'))
        list2 = (response.xpath('//h2/a[@href]'))
        list3 = (response.xpath('//h3/a[@href]'))
        try:
            for li in list1:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list:
                    if (len(headline) > 20):
                        list.append(headline)
                        thehinduitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield thehinduitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print("\n\n")
            for li in list2:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list:
                    if (len(headline) > 20):
                        list.append(headline)
                        thehinduitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield thehinduitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print("\n\n")

            for li in list3:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list:
                    if (len(headline) > 20):
                        list.append(headline)
                        thehinduitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield thehinduitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print("\n\n")
        except Exception as ex:
            print(ex)
            print(list)
