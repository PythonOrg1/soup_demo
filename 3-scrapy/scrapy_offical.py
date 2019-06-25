import scrapy


class QuotesSpider(scrapy.Spider):

    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    # def __init__(self, name, start_urls):
    #     self.name = name
    #     self.start_urls = start_urls

    def parse(self, response):
        for quote in response.css('div.quote'):
            tags = []
            for tag in  quote.css('a.tag::text'):
                tags.append(tag.get())

            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
                'tags': tags
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)



# if __name__ == '__main__':
    # start_urls = ['http://quotes.toscrape.com/tag/humor/',]
    # spider = QuotesSpider('quotes', start_urls)
    # response = None
    # p = spider.parse(response)
    # print(p)
    # print(response)

    # for q in spider.parse():
    #     print(q)


    # spider = QuotesSpider()
    # print(spider)
    # p = spider.parse(response=None)
    # print(p)
