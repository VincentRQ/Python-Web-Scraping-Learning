import scrapy
from countries_gdp.items import CountryGdpItem
from scrapy.loader import ItemLoader


class GdpSpider(scrapy.Spider):
    name = "gdp"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"]

    def parse(self, response):
        # table.wikitable.sortable
        for country in response.css('table.wikitable.sortable tbody tr:not([class])'):
            # item = CountryGdpItem()
            # item["country_name"] = country.css('td:nth-child(1) a::text').get()
            # item["region"] = country.css('td:nth-child(2) a::text').get()
            # item["gdp"] = country.css('td:nth-child(3) ::text').get()
            # item["year"] = country.css('td:nth-child(4) ::text').get()
            # yield item
                #we can query various things using the scrapy shell selector.
            item = ItemLoader(item=CountryGdpItem(), selector=country)
            item.add_css("country_name", 'td:nth-child(1) a')
            #We are using takefirst, so we don't need to use the ::text after the anchor.
            item.add_css("region", 'td:nth-child(2) a')
            item.add_css("gdp", 'td:nth-child(3)')
            item.add_css("year", 'td:nth-child(4)')

            yield item.load_item()


        # for country in response.xpath("//table[contains(@class,'wikitable sortable')]//tbody//tr"):
        #     yield {
        #         "country_name": country.xpath(".//td[1]//a/text()").get(),
        #         "region": country.xpath(".//td[2]//a/text()").get(),
        #         "gdp": country.xpath(".//td[3]/text()").get(),
        #         "year": country.xpath(".//td[4]/text()").get(),
        #
        #     }
            #using xpath
            # /html/body/table[3]/tbody/tr/td[2]
            # //table[3]//td[2]
            # //table[@class='wikitable']
            # //table[3]/@closs
            # //img[1]/@src
            # //table[3]/td[2]/text()

            #for outputting: scrapy crawl gdp -O  gdp.csv (allows for overwriting with capital 0)







