#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, request, session
from flask_wechatpy import Wechat, wechat_required, oauth
from wechatpy.replies import TextReply
from wechatpy.replies import create_reply
from wechatpy.replies import ArticlesReply
from wechatpy.utils import ObjectDict


app = Flask(__name__)
app.config['WECHAT_APPID'] = 'wxf768628172134e5c'
app.config['WECHAT_SECRET'] = '9afd19322d7e89b6f1c4cdaed9e55266'
app.config['WECHAT_TOKEN'] = 'token'
app.config['DEBUG'] = True
#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

wechat = Wechat(app)



@app.route('/wechat', methods=['GET', 'POST'])
@wechat_required
def wechat_handler():
    msg = request.wechat_msg
    if msg.type == 'text':
        reply = create_reply(msg.content, message=msg)
    else:
        reply = TextReply(content='hello', message=msg)

    return reply




if __name__ == '__main__':
    app.run(debug=True, ssl_context=(
        "certificate.crt",
        "private.key")
    )







reply = ArticlesReply(message=message)
# simply use dict as article
reply.add_article({
    'title': 'test',
    'description': 'test',
    'image': 'image url',
    'url': 'url'
})
# or you can use ObjectDict
article = ObjectDict()
article.title = 'test'
article.description = 'test'
article.image = 'image url'
article.url = 'url'
reply.add_article(article)
