from flask_register import db

class UserRegister(db.Model):
    # 記錄使用者資料的資料表
    __tablename__ = "UserRegisters"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return 'username:{}, email:{}'.format(self.username, self.email)