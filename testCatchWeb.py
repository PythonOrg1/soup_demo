import requests
from bs4 import BeautifulSoup
import json


def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    return r.text


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    con = soup.find(id='content-left')
    # print(con)
    con_list = con.find_all('div', class_="article")

    result = []
    for c in con_list:
        res = {}

        auth = c.find('div', class_="author")
        # 作者
        # print(auth.find('h2').text)
        # print(auth.find('h2').string)

        icon = c.find('img')
        icon_url = 'https:' + icon.attrs.get('src')
        print('头像地址： ' + icon_url)
        # 也是 作者
        auth_name = icon.attrs.get('alt')
        print('作者名字： ' + auth_name)

        auth_attr = c.find('div', class_="articleGender")
        # 性别： manIcon (男性) womenIcon (女性)
        auth_gender = '男'
        auth_age = 0
        if auth_attr == None:
            print('匿名用户')
            auth_gender = '未知'
            auth_age = '未知'
        else:
            gender = auth_attr.attrs.get("class")[1]
            if gender == 'womenIcon':
                auth_gender = '女'
            print('性别： ' + auth_gender)

            # 年龄
            auth_age = auth_attr.string
            print('年龄： ' + auth_age)

        # 正文图片内容获取
        con = c.find('div', class_='thumb').find('img')
        context = 'https:' + con.attrs.get('src')
        print('分享内容： ' + context)
        # 内容标签（类别）
        context_tag = con.attrs.get('alt')
        print('标签： ' + context_tag)

        # 评论
        commons = c.find('div', class_='stats')
        cs = commons.find_all('i', class_='number')
        num_funny = cs[0].string
        # 好笑（点赞）数
        print('点赞数： ' + num_funny)
        # 评论数
        num_commons = cs[1].string
        print('评论数： ' + num_commons)

        print("\n")

        res.setdefault('authName', auth_name)
        res.setdefault('authAge', auth_age)
        res.setdefault('authGender', auth_gender)
        res.setdefault('iconUrl', icon_url)
        res.setdefault('content', context)
        res.setdefault('contentTag', context_tag)
        res.setdefault('numFunny', num_funny)
        res.setdefault('numCommons', num_commons)

        result.append(res)
    return result


#
# 爬虫实例代码
# 爬虫对象： 糗事百科- '热图'模块
# 地址： https://www.qiushibaike.com/imgrank/
# pageStart 起始页
# pageEnd 终点页
#
def getImgRankToJson(pageStart: int, pageEnd: int):
    # 最终结果
    result = {}
    result_list = []

    for p in range(pageStart, pageEnd + 1):
        # 单页抓取结果
        result_p = {}

        url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(p)
        print(url)
        # 页面内容html
        html = download_page(url)
        # 爬虫结果json数组
        list = get_content(html, p)

        result_p.setdefault('currentPage', p)
        print('-----p.setpage' + str(p))
        result_p.setdefault('list', list)

        result_list.append(result_p)
        result.setdefault('pageSize', pageEnd - pageStart + 1)
        result.setdefault('resultList', result_list)

    # dict转化为json
    resultJson = json.dumps(result, separators=(',', ':'), ensure_ascii=False)
    print(resultJson)
    return resultJson


if __name__ == '__main__':
    getImgRankToJson(1, 2)
