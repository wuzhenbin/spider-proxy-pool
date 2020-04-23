
# Redis数据库地址
REDIS_HOST = '127.0.0.1'
# Redis端口
REDIS_PORT = 6379
# Redis密码，如无填None
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'


# 开关 手动控制
# 检查器开关
TESTER_ENABLED = True
# 获取器开关
GETTER_ENABLED = True
# api开关
API_ENABLED = True

# 获取周期 
GETTER_CYCLE = 300
# 检查周期
TESTER_CYCLE = 20


# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

# 测试API，建议抓哪个网站测哪个
# TEST_URL = 'http://www.baidu.com'
TEST_URL = 'https://data.p4psearch.1688.com/data/ajax/get_premium_offer_list.json?beginpage=1&asyncreq=1&keywords=%E8%8C%B6%E5%8F%B6&sortType=&descendOrder=&province=&city=&priceStart=&priceEnd=&dis=&cosite=baidujj&location=re&trackid=8856886241459804884118&spm=a2609.11209760.j3f8podl.e5rt432e&keywordid=57065993601&pageid=6bcb51e048iARp&p4pid=1552387531017239008785&callback=jsonp_1552387531620_83004&_=1552387531620'


# 允许测试结果状态码
VALID_STATUS_CODES = [200, 302]

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 代理池数量界限
POOL_UPPER_THRESHOLD = 10000

# 最大批测试量
BATCH_TEST_SIZE = 10