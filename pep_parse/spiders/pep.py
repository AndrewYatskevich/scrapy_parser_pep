import scrapy

from pep_parse.items import PepParseItem

PEPS_DOMAIN = 'peps.python.org'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEPS_DOMAIN]
    start_urls = [f'https://{PEPS_DOMAIN}/']

    def parse(self, response, **kwargs):
        pep_docs = response.css('section[id=numerical-index] tbody tr')
        for pep_doc in pep_docs:
            pep_link = pep_doc.css('a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_number, name = response.css(
            'h1.page-title::text'
        ).get().split(' – ')
        data = {
            'number': int(pep_number.replace('PEP ', '')),
            'name': name,
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
