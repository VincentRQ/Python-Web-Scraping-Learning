import scrapy
from elems.items import PeriodicElementItem
from scrapy.loader import ItemLoader


class PeriodicElementsSpider(scrapy.Spider):
    name = "periodic_elements"


    def start_request(self):
        yield scrapy.Request('https://pubchem.ncbi.nlm.nih.gov/ptable/', meta=dict(
            playwright=True
        ))


    def parse(self, response):
        for element in response.css("div.ptable div.elements"):
            i = ItemLoader(item=PeriodicElementItem(), selector=element)

            i.add_css('symbol', '[data-tooltip="Symbol"]')
            i.add_css('name', '[data-tooltip="Name"]')
            i.add_css('atomic_number', '[data-tooltip="Atomic Number"]')
            i.add_css('atomic_mass', '[data-tooltip*="Atomic Mass"]')
            i.add_css('chemical_group', '[data-tooltip="Chemical Group Block"]')

            yield i.load_item()