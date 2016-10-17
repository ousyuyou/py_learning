# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import urllib

class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate,sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Host": "www.zhihu.com",
        "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36",
        "Referer": "http://www.zhihu.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    def start_requests(self):
        return [scrapy.Request("https://www.zhihu.com", 
                                headers = self.headers,
                                meta = {'cookiejar' : 1},
                                callback = self.post_login)]
        
    def post_login(self, response):
        print 'Preparing login'
        xsrf = scrapy.Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        print xsrf
        #captcha = scrapy.Selector(response).xpath('//input[@name="captcha_type"]/@value').extract()[1]
        #getCaptchaCode picture
        urllib.urlretrieve("https://www.zhihu.com/captcha.gif?r=&type=login", "code.gif")
        print 'please input captcha code'
        captcha = raw_input()
        form = {
                        '_xsrf': xsrf,
                        'account': 'ousyuyou@163.com',
                        'password': '791227',
                        'captcha': captcha
                    }
                    
        return [scrapy.FormRequest.from_response(response,   #"http://www.zhihu.com/",
                            meta = {'cookiejar' : response.meta['cookiejar']}, 
                            headers = self.headers,
                            formdata = form,
                            callback = self.after_login,
                            dont_filter = True
                            )]
    def after_login(self, reponse):
        print 'after login'