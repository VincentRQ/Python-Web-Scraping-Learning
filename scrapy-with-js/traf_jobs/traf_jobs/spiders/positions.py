import scrapy


class PositionsSpider(scrapy.Spider):
    name = "positions"
    allowed_domains = ["traf.com"]
    start_urls = ["https://trafigura.wd3.myworkdayjobs.com/TrafiguraCareerSite"]

    # def parse(self, response):
    #     for job in response.css('section[class*="css"] ul[role="list"] li[class^="css"] div[class^="css"] div[class^="css"] div[class^="css"] h3'):
    #         yield {
    #             'title': job.css('a::text').get()
    #         }


    def parse(self, response):
        for job in response.xpath("/html/body/div[1]/div/div/div[3]/div/div/div[2]/section/ul"):
            yield {
                "title": job.xpath("./li[1]/div[1]/div/div/h3/a").get(),
            }