import scrapy
import data_base as db

# print(__name__)
db.close_conection_to_db()
db.connect_to_db()


class PeludSpider(scrapy.Spider):
    name = 'peludspider'
    start_urls = ['http://www.stampar.hr/hr/peludna-grad/1',
                  'http://www.stampar.hr/hr/peludna-grad/16',
                  'http://www.stampar.hr/hr/peludna-grad/7', ]

    def parse(self, response):
        for data in response.css('div.mjerenje'):
            stats = {}
            vrijednost = data.xpath('.//div[@class="clearfix vrijednost"]/text()').get()
            if vrijednost:
                try:
                    stats['grad'] = response.css('title::text').get().split()[2]
                    stats['vrijednost'] = vrijednost
                    stats['naziv'] = data.xpath('.//div[@class="clearfix naziv"]/a/text()').get()
                    stats['datum'] = data.xpath('.//div[@class="clearfix datum-resp visible-phone"]/text()').get()
                    db.add_pelud_data(**stats)
                except:
                    print('Vrijednosti nisu dohvačene!')




