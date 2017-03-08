# -*- coding: utf-8 -*-
# filename: say.py

import hashlib
import web
from poem import sample


class Poem(object):
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
