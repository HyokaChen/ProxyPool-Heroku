# -*- coding: utf-8 -*-
import os
# Redis Host
# HOST = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
# # Redis PORT
# PORT = 6379
REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

# Redis 中存放代理池的 Set 名
POOL_NAME = 'proxies'

# Pool 的低阈值和高阈值
POOL_LOWER_THRESHOLD = 15
POOL_UPPER_THRESHOLD = 20

# 两个调度进程的周期
VALID_CHECK_CYCLE = 600
POOL_LEN_CHECK_CYCLE = 300

# headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}
