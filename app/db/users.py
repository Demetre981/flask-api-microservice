from sqlalchemy import Column, Integer, String
from app.db.db_models import Base#
from flask_login import UserMixin




class User(Base, UserMixin):
    __tablename__="users"
    id = Column(Integer, primary_key=True)
    username = Column(String(70), nullable=False)
    password = Column(String(70), nullable=False)
    email = Column(String(70), default=None)
    #text = Column(Text, nullable=False)
    


    def __init__(self, username, password, email):# id,
        # self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return self.username
