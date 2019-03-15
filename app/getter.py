
from app.db import RedisClient
from app.setting import *
from app.crawler import Crawler
import sys


class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()
    
    # 判断是否达到了代理池限制
    def is_over_threshold(self):
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
    
    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for site_name in self.crawler.__CrawlName__:
                proxies = self.crawler.get_raw_proxies(site_name)
                sys.stdout.flush()
                for item in proxies:
                    self.redis.add(item)