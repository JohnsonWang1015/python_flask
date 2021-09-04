from flask import Flask
from flask_mail import Mail
from flask_mail import Message
from flask import render_template
# 加入 threading
from threading import Thread

from datetime import datetime

app = Flask(__name__)

app.config.update(
    # gmail 設置
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PROT = 465,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = "wangjohnson.khh@gmail.com",
    MAIL_PASSWORD = "@wangJohnson91"
)
# 先設置參數，再實作 mail
mail = Mail(app)

@app.route("/")
def index():
    #message = "我是首頁\n" + str(datetime.now())
    return render_template('home.html')

@app.route("/message")
def message():
    # 主旨
    msg_title = "你好，這是 Flask-Mail"
    # 寄件者
    msg_sender = "wangjohnson.khh@gmail.com"
    # 收件者，list 格式
    msg_recipients = ['a0903809066@gmail.com', 'wang0981335939@gmail.com']
    # 郵件內容
    #msg_body = "你好，我是 mail body"
    # 使用 html 內容
    #msg_html = "<h1>你好，Flask-Mail 可以使用 HTML，而且使用 threading</h1>"    
    # 建立 mail 物件
    
    #msg.body = msg_body
    #msg.html = msg_html
    template_name = "sendmailtest"
    
    # 寄出郵件
    #mail.send(msg)
    send_mail(sender=msg_sender, recipients=msg_recipients, subject=msg_title, template=template_name, user_name="Johnson")
    
    return "信件寄出成功"

def send_async_email(app, msg):
    # app_context() 承接上下文
    with app.app_context():
        mail.send(msg)
        
#def send_mail(sender, recipients, subject, context, **kwargs):
# 內容調整樣板名稱 template
def send_mail(sender, recipients, subject, template, **kwargs):
    '''
    sender：sender 的部份可以考慮透過設置default
    recipients：要list格式
    subject：郵件主旨
    template：樣板名稱
    **kwargs：參數
    '''
    msg = Message(subject, sender=sender, recipients=recipients)
    #msg.body = template
    msg.html = render_template(template + '.html', **kwargs)
    
    # 使用多執行緒
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return thread

if __name__ == "__main__":
    app.debug = True
    app.run()