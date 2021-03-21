from time import sleep
import scrapy
from re import sub
class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = ['https://aws.amazon.com/rds/aurora/faqs/'
                 ,'https://aws.amazon.com/glue/faqs/'
                 ,'https://aws.amazon.com/lake-formation/faqs/'
                 ,'https://aws.amazon.com/kinesis/data-firehose/faqs/'
                 ,'https://aws.amazon.com/s3/faqs/'
                 ,'https://aws.amazon.com/iam/faqs/'
                 ,'https://aws.amazon.com/single-sign-on/faqs/'
    ]

    def parse(self, response):
        for category in response.xpath('//div[@class="lb-col lb-tiny-24 lb-mid-24"]'):
            sleep(1)
            for question in category.xpath('./div[@class="lb-txt-16 lb-rtxt" or @class="lb-rtxt"]'):
                question_block = question.xpath('./p[1]/b/text()').extract()
                question_block = list(map(lambda question_chunk:sub("<(.*?)>","",question_chunk),question_block))
                question_block = ''.join(question_block)

                answer_block = question.xpath('./p[2]/node()').extract()
                answer_block = list(map(lambda answer_chunk:sub("<(.*?)>","",answer_chunk),answer_block))
                answer_block = ''.join(answer_block)
                yield {
                    "Service" : response.xpath("//*[@id='aws-page-content']/div/div/div/div/div/h1/text()").extract_first(),
                    'Category': category.xpath('./h2/text()').extract_first(),
                    'Question': question_block,
                    'Answer': answer_block,
                }
