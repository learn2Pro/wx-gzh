# -*- coding: utf-8 -*-
# filename: menu.py
import urllib
from basic import Token


class Menu(object):
    def __init__(self):
        pass

    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    # 获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()


if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "type": "view",
                "name": "个人博客",
                "url": "http://learn2pro.tech"
            },
            {
                "name": "奇思妙想",
                "sub_button":
                [
                    {
                        "type": "pic_photo_or_album",
                        "name": "以图还图",
                        "key":"wxmenu_1_0",
                        "sub_button":[]
                    },
                    {
                        "name": "发送位置",
                        "type": "location_select",
                        "key": "wxmenu_1_1"
                    }
                ]
            },
            {
                "type": "click",
                "name": "最新干货",
                "key": "wxmenu_2_0"
            }
          ]
    }
    """
    accessToken = Token.get_access_token()
    # myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)
