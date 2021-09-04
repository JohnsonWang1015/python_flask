from flask import Flask
from flask import render_template
from flask.json import jsonify
from flask.views import MethodView
from flask import request
from itsdangerous import TimedJSONWebSignatureSerializer as TJSS
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(10)

class AuthorToken(MethodView):
    def post(self):
        grant_type = request.form.get('grant_type')
        username = request.form.get('username')
        password = request.form.get('password')
        
        # 判斷 grant_type 是否為 password
        if grant_type is None or grant_type != 'password':
            response = jsonify(message="bad grant type")
            response.status_code = 400
            return response
        
        # 測試用
        if username != "johnson" or password != "123456":
            response = jsonify(message="wrong username or password")
            response.status_code = 400
            return response
        
        # 產生 token，有限期限設置為 3600 秒
        s = TJSS(app.config['SECRET_KEY'], expires_in=3600)
        token = s.dumps({'username':username}).decode('UTF-8')
        
        # 回傳符合 RFC-6750 的格式
        response = jsonify(
            {
                'access_token':token,
                'token_type':'Bearer',
                'expires_in':3600
            }
        )
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        
        return response

class FakeSource(MethodView):
    def get(self):
        # 驗證 token
        try:
            token_type, access_token = request.headers.get('Authorization').split(' ')
            if token_type != 'Bearer' or token_type is None:
                # 驗證 token 是否為 Bearer
                pass 
        except Exception as e:
            print('Error：', e)
        
        s = TJSS(app.config['SECRET_KEY'])
        data = s.loads(access_token)
        return jsonify({'data':data['username']})

app.add_url_rule('/author_token', view_func=AuthorToken.as_view('author_token'))
app.add_url_rule('/author_token', view_func=FakeSource.as_view('fake_source'))

@app.route("/")
def index():
    return render_template('home.html')

if __name__ == "__main__":
    app.debug = True
    app.run()