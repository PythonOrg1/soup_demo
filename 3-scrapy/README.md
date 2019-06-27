**Scrapy**

适合模版式的页面结构爬虫，效率较高；对于模版化的页面布局，只需要指出模版需要的每个标签元素，即可一次性抓取。

例如： http://quotes.toscrape.com/tag/humor/

安装：

    #pip install scrapy

命令行创建工程：

    scrapy startproject <project_name> [project_dir]
    #scrapy startproject myproject dir
    会在 'dir' 目录（如果没有，则会自动创建一个跟'myproject'同名的目录）下，生成固定格式和目录结构的项目，例如此处的 auto_cmd_project 项目;

    创建一个Spider(统一目pj下可以创建多个spider)：
    scrapy genspider [-t template] <name> <domain>
    #scrapy genspider spname domain.com

运行：
    
    #scrapy runspider xxx.py
    
输出数据成文件 (支持 .json .jl .xml 等格式)

    #scrapy runspider xxx.py -o filename.json  
    
    注意： 由于历史原因，Scrapy会'附加'到给定文件而不是'覆盖'其内容。如果在第二次之前没有删除文件的情况下运行此命令两次，则最终会出现损坏的JSON文件。
   
    
实时交互：（通过这种方式方便判和确定断抓取到的界面元素标签）    
   
    #scrapy shell $url
    例如：
    #scrapy shell 'http://quotes.toscrape.com/page/1/' 

两种方式获取元素(标签选择器)：

关于xpath的更多实用细节：
https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors

    1。css （实际上scrapy底层还是将其转化为后者xpath）
        获取元素：   response.css('title')
        获取元素文字内容：response.css('title::text').get()
        
    2。xpath    
        获取元素：   response.xpath('//title')
        获取元素文字内容：response.xpath('//title/text()').get()
        
        get()        获取单个元素内容(string)
        getall()     获取所有的(array)
        re(r'Quotes.*') 正则匹配(array)
    
    3.获取属性元素
        ::attr(xxx)
        eg: res.css('div.next a::attr(href)').get()
        
        attrib['xxx']
        eg: res.css('div.next a').attrib['href']
    
    
    