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
            print(sample.say(key))
            return "hello world!-get"
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            return "hello world!-post"
        except Exception, Argment:
            return Argment
