# -*- coding: utf-8 -*-
# filename: basic.py
import urllib
import time
import json
import redis


class Token:
    def con(self):
        pool = redis.ConnectionPool(host='23.106.148.101', port=6379, password=r'banwagong-redis')
        r = redis.Redis(connection_pool=pool)
        r.ttl(1000)
        return r

    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0

    def __real_get_access_token(self):
        appId = "wx7306b3e0b9b4a9ef"
        appSecret = "888198e6080e49096a96028fd220a3f1"

        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
                   "client_credential&appid=%s&secret=%s" % (appId, appSecret))
        urlResp = urllib.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())

        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']
        pool = self.con()
        pool.set('token', self.__accessToken, ex=self.__leftTime)
        return self.__accessToken

    def get_access_token(self):
        pool = self.con()
        access_token = pool.get('token')
        if access_token is None:
            return self.__real_get_access_token()
        else:
            return access_token

    def run(self):
        while (True):
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_access_token()
