# -*- coding: utf-8 -*-
# filename: say.py

import hashlib
import web
from poem import sample
import redis


class Poem(object):
    def con(self):
        pool = redis.ConnectionPool(host='23.106.148.101', port=6379, password=r'banwagong-redis')
        r = redis.Redis(connection_pool=pool)
        r.ttl(1000)
        return r

    def GET(self):
        try:
            title = web.input()
            key = title.get("keyword")
            if key is not None:
                key = key.encode("utf-8")
            pool = self.con()
            poem = pool.get('poem')
            if poem is not None:
                return poem
            else:
                back = sample.say(key)
                pool.set('poem', back, ex=600)
                return back
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            return "hello world!-post"
        except Exception, Argment:
            return Argment
