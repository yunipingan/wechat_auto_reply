# coding=utf-8

import re

import itchat


def itchat_login():
    itchat.auto_login(True)


@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def test(msg):
    group = msg['User']
    if group['NickName'] == groupName:
        content = msg['Content']
        c = re.compile(u'(进\s*?线\s*?)(([1-9]\d+)|[8-9])')
        pattern = c.findall(content)
        if len(pattern) > 0:
            for f in friends:
                if f['RemarkName'] == userName:
                    itchat.send(msg['Content'] + ' 下', toUserName=f['UserName'])
                    print (msg['ActualNickName'] + ':' + msg['Content'])


groupName = input(u'请输入要监听的群聊名称：')
userName = input(u'请输入唯一好友备注：')
itchat_login()
friends = itchat.get_friends(update=True)
itchat.run()
