import re
import time
from urllib import request
from daily.tools.config import Config


class BingPage:
    def __init__(self):
        field = "bing-page"
        config_data = Config()
        self.url = config_data.get(field, "html_url")
        self.path = config_data.get(field, "save_path")
        self.regular = config_data.get(field, "bg_regular")

    def get_html(self):
        page = request.urlopen(self.url).read()
        # decode数据
        page = page.decode('utf-8')
        return page

    def get_background_img_link(self, html_data):
        # 解析bing页面源码获得背景图链接正则表达式 目前例子：
        bg_reg = '\/[^\"]*\.jpg'
        img_re = re.compile(bg_reg, re.M)
        bg_img_link = re.findall(img_re, html_data)
        # 这里默认取第一个数据作为背景图
        return self.url + bg_img_link[0]

    def load_img(self, link):
        pic_name = 'bing_' + time.strftime('%Y%m%d', time.localtime(time.time())) + '.jpg'
        # 落地链接图片数据
        request.urlretrieve(link, self.path + pic_name)

    def load(self):
        # 获取页面数据
        page_data = self.get_html()
        # 解析获取背景图链接
        img_link = self.get_background_img_link(page_data)
        # 落地背景图
        self.load_img(img_link)
