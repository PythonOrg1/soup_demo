import scrapy


# 定义 Spider的子类（必须）， 用于提取网站数据
class QuotesSpider(scrapy.Spider):

    # 必须唯一，Spider子类的名称标识符
    name = "quotes"

    # 必须返回一个可迭代的请求（您可以返回请求列表或编写生成器函数），Spider将开始从中爬行。后续请求将从这些初始请求中连续生成。
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, method='GET',encoding='utf-8')

    # 将调用一个方法来处理为每个请求下载的响应。响应参数是TextResponse保存页面内容的实例，并具有处理它的其他有用方法。
    # 该parse()方法通常解析响应，将抽取的数据提取为dicts，并查找要遵循的新URL并Request从中创建新的request（）。
    def parse(self, response):


        # Save as a HTML file
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                # 'author': quote.xpath('span/small/text()').get(),     #两种方式都可以
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }
            # self.log(' ---> quote : %s' % )

        # 获取 元素链接 及此处的下一页内容
        next_page = response.css('li.next a::attr("href")').get()
        # self.log('--->quote nextpage = %s' % next_page)
        if next_page is not None:
            # 使用该urljoin()方法构建完整的绝对URL （因为链接可以是相对的）并向下一页生成新请求，
            next_page = response.urljoin(next_page)
            # self.log('--->quote nextpage = %s' % next_page)

            # 继续回调请求下一页的数据
            yield scrapy.Request(url=next_page, callback=self.parse)
            # yield response.follow(next_page, self.parse)
