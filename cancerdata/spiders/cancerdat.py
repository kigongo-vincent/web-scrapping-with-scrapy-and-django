import scrapy
import requests

class CancerdatSpider(scrapy.Spider):
    name = "cancerdat"
    allowed_domains = ["prescriptec.org"]
    start_urls = ["https://prescriptec.org/countries/uganda/"]

    def parse(self, response):

        data = response.css('div table tr td::text').getall()
        obj = {"key": None, "value": None}

        for round_number in range(8):
            index = round_number * 2  # Calculate the index based on the round number
            obj["key"] = data[index]
            obj["value"] = data[index + 1]
            requests.post('http://localhost:8000/data/', obj)
    obj = {"key": None, "value": None}


