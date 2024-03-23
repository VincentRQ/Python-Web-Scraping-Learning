import scrapy
from scrapy_playwright.page import PageMethod

class PositionsSpider(scrapy.Spider):
    name = "positions"
    allowed_domains = ["trafigura.wd3.myworkdayjobs.com"]
    start_urls = ["https://trafigura.wd3.myworkdayjobs.com/TrafiguraCareerSite"]

    def start_requests(self):
        yield scrapy.Request(
            self.start_urls[0],
            meta=dict(
                playwright=True,
                playwright_page_methods = [
                    PageMethod("wait_for_selector", 'section[class*="css"] ul[role="list"]'),
                    PageMethod("evaluate", "")
                ]
            )
        )

        # btn selector: #mainContent > div > div.css-uvpbop > section > div.css-3z7fsk > nav > div > ol > li:nth-child(2) > button


    # async def parse(self, response):
    #     for job in response.css('section[class*="css"] ul[role="list"] li[class^="css"] div[class^="css"] div[class^="css"] div[class^="css"] h3'):
    #         yield {
    #             'title': job.css('a::text').get()
    #         }

    async def parse(self, response):
        for job in response.css('# mainContent > div > div.css-uvpbop > section > ul > li:nth-child(20) '):
            yield {
                'title': job.css('div.css-qiqmbt > div > div > h3 > a::text').get()
            }



    # def parse(self, response):
    #     for job in response.xpath("/html/body/div[1]/div/div/div[3]/div/div/div[2]/section/ul"):
    #         yield {
    #             "title": job.xpath("./li[1]/div[1]/div/div/h3/a").get(),
    #         }
