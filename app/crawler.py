

from .utils import *
from pyquery import PyQuery as pq
import re


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlName__'] = []
        # 遍历类的所有属性筛选出crawl_开头的函数
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlName__'].append(k)

        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_raw_proxies(self, site_name):
        return [item for item in eval("self.{}()".format(site_name))]
    
    # 爬取此代理需要开splash服务
    def crawl_data5u(self):
        start_url = 'http://www.data5u.com/free/gngn/index.shtml'
        splash_url = 'http://localhost:8050/render.html'
        args = { 'url': start_url }
        html = get_response(splash_url,params=args)

        if html:
            doc = pq(html)
            lis = doc('.wlist ul.l2').items()
            for li in lis:
                ip = li.find('span:nth-child(1) li').text()
                port = li.find('span:nth-child(2) li').text()
                yield ':'.join([ip, port])   

    def crawl_xicidaili(self):
        start_url = 'https://www.xicidaili.com/nn/'       
        html = get_response(start_url)
        if html:
            doc = pq(html)
            trs = doc('table tr').items()
            for tr in trs:
                ip = tr.find('td:nth-child(2)').text()
                port = tr.find('td:nth-child(3)').text()
                if ip and port:
                    yield ':'.join([ip, port]) 


    def crawl_iphai(self):
        start_url = 'http://www.iphai.com/'
        html = get_response(start_url)
        if html:
            doc = pq(html)
            trs = doc('table tr').items()
            for tr in trs:
                ip = tr.find('td:nth-child(1)').text()
                port = tr.find('td:nth-child(2)').text()
                yield ':'.join([ip, port])

    def crawl_xiaohuan(self):
        url = 'https://ip.ihuan.me/address/5Lit5Zu9.html'
        html = get_response(url)
        print('Crawling', url)
        if html:
            doc = pq(html)
            trs = doc('tbody tr').items()
            for tr in trs:
                ip = tr.find('td:nth-child(1)').text()
                port = tr.find('td:nth-child(2)').text()
                yield ':'.join([ip, port])

    def crawl_kuai(self):
        url = 'https://www.kuaidaili.com/free/'
        html = get_response(url)
        print('Crawling', url)
        if html:
            doc = pq(html)
            trs = doc('tbody tr').items()
            for tr in trs:
                ip = tr.find('td:nth-child(1)').text()
                port = tr.find('td:nth-child(2)').text()
                yield ':'.join([ip, port])

    def crawl_xila(self):
        url = 'http://www.xiladaili.com/gaoni/'
        html = get_response(url)
        print('Crawling', url)
        if html:
            doc = pq(html)
            trs = doc('tbody tr').items()
            for item in trs:
               yield item.find('td:nth-child(1)').text() 


    def crawl_66(self,page_count=4):
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_response(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_ip3366(self):
        for page in range(1, 4):
            start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
            html = get_response(start_url)
            if html:
                doc = pq(html)
                trs = doc('tbody tr').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

            