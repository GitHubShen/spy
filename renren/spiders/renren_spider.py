import scrapy

class RenrenSpider(scrapy.Spider):
    name = "renren"
    allowed_domains = ["renren.com"]
    start_urls = [
        "http://status.renren.com/status/v7/419208280"
    ]

    def __init__(self):
        self.username = input("input your renren\'s username:\n")
        self.passwd = input("input your renren\'s password:\n")

    def start_requests(self):
        return [scrapy.FormRequest('http://www.renren.com/PLogin.do',
            formdata={'email':self.username,'password':self.passwd},
            callback=self.login)]

    def login(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)


    def parse(self, response):
        print(response)
        print("########################")
        print(response.body)
