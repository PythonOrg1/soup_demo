**Scrapy 官方示例工程**

https://docs.scrapy.org/en/latest/intro/tutorial.html

项目结构预览：

    tutorialProject/
        scrapy.cfg            # deploy configuration file  部署配置文件
    
        tutorial/             # project's Python module, you'll import your code from here  代码
            __init__.py
            
            items.py          # project items definition file   模版item定义
            middlewares.py    # project middlewares file    中间件
            pipelines.py      # project pipelines file     
            settings.py       # project settings file   项目配置文件
            spiders/          # a directory where you'll later put your spiders
                __init__.py    
        