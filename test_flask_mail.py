from flask import Flask
from flask_mail import Mail
from flask_mail import Message

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

@app.route("/message")
def index():
    # 主旨
    msg_title = "你好，這是 Flask-Mail"
    # 寄件者
    msg_sender = "wangjohnson.khh@gmail.com"
    # 收件者，list 格式
    msg_recipients = ['a0903809066@gmail.com']
    # 郵件內容
    msg_body = "你好，我是 mail body"
    # 建立 mail 物件
    msg = Message(msg_title, sender=msg_sender, recipients=msg_recipients)
    msg.body = msg_body
    
    # 寄出郵件
    mail.send(msg)
    return "信件寄出成功"

if __name__ == "__main__":
    app.debug = True
    app.run()