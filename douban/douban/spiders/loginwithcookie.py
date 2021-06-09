# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest


class LoginwithcookieSpider(scrapy.Spider):
    name = 'loginwithcookie'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    cookie = '''bid=ZJEQ1FVTIHA; ll="118159"; __utmc=30149280; push_doumail_num=0; __utmv=30149280.16884; 
    dbcl2="168843432:x7pLIM0yJJM"; ck=o_eT; push_noty_num=0; ap_v=0,
    6.0; gr_user_id=ad5299cc-dd00-418d-8560-d303708fb113; 
    gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=a4d830bd-4b6f-4d59-91a1-9b802507fff9; 
    gr_cs1_a4d830bd-4b6f-4d59-91a1-9b802507fff9=user_id%3A1; 
    __utma=30149280.545610310.1616071305.1623225815.1623241673.19; 
    __utmz=30149280.1623241673.19.18.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_douban=1; 
    __utma=81379588.1633675371.1623241673.1623241673.1623241673.1; __utmc=81379588; 
    __utmz=81379588.1623241673.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; 
    _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1623241673%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; 
    _pk_ses.100001.3ac3=*; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_a4d830bd-4b6f-4d59-91a1-9b802507fff9=true; 
    __gads=ID=de1f301c770422d8-2228b3ca4cc900a7:T=1623241675:RT=1623241675:S=ALNI_MYtm2TKFUZJBS_m4px3OSMh1-puJQ; 
    _pk_id.100001.3ac3=c7dca6267a8d648b.1623241673.1.1623241805.1623241673.; __utmb=30149280.5.10.1623241673; 
    __utmb=81379588.5.10.1623241673; Hm_lvt_1953076d62ee35b7103b8d2e4473cc49=1623241715,1623241728,1623241738,
    1623241805; Hm_lpvt_1953076d62ee35b7103b8d2e4473cc49=1623241805 '''

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'DNT': '1',
        'Host': 'book.douban.com',
        'Referer': 'https://book.douban.com/',
        'Upgrade-Insecure-Requests': '1',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"

    }

    # 使用FormRequests发送请求，指定url，请求头信息，cookies
    def start_requests(self):
        for url in self.start_urls:
            return [FormRequest(url,
                                headers=self.headers,
                                # formdata={'name': '1120844583@qq.com',
                                #           'password': 'guoqing1010',
                                #           'remember': 'false'},
                                # cookies=self.cookies,
                                callback=self.parse)]

    # 爬虫处理函数
    def parse(self, response):
        user_check = response.css(
            '.nav-user-account > a > span::text').extract_first()
        self.logger.info('{}doubanbook已经登录成功'.format(user_check))
