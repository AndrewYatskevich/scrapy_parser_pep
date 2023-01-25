import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response, **kwargs):
        pep_docs = response.css('section[id=numerical-index] tbody tr')
        for pep_doc in pep_docs:
            pep_link = pep_doc.css('a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get().split(' – ')
        data = {
            'number': int(title[0].replace('PEP ', '')),
            'name': title[1],
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
