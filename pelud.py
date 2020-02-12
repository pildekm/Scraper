import scrapy


# def start_request(self):
#     start_urls = ['http://www.stampar.hr/hr/peludna-grad/1', ]
#
#     return [scrapy.Request(url=url, callback=self.parse) for url in start_urls]
class PeludSpider(scrapy.Spider):
    name = 'peludspider'
    start_urls = ['http://www.stampar.hr/hr/peludna-grad/1',
                  'http://www.stampar.hr/hr/peludna-grad/16',
                  'http://www.stampar.hr/hr/peludna-grad/7', ]
    # start_urls = ['http://www.stampar.hr/hr/peludna-grad/7', ]


    def parse(self, response):
        for data in response.css('div.mjerenje'):
            vrijednost = data.xpath('.//div[@class="clearfix vrijednost"]/text()').get()
            if vrijednost:
                grad = response.css('title::text').get().split()[2]
                datum = data.xpath('.//div[@class="clearfix datum-resp visible-phone"]/text()').get()
                naziv = data.xpath('.//div[@class="clearfix naziv"]/a/text()').get()
                print(datum)
                print(vrijednost)
                print(naziv)
                print(grad)


