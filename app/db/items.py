from sqlalchemy import Column, Integer, String, Boolean, BinaryExpression
from app.db.db_models import Base#




class Item(Base):
    __tablename__="items"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    experience = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False)
    #text = Column(Text, nullable=False)
    


    def __init__(self, title, price, experience, score, phone):# id,
        # self.id = id
        self.title = title
        self.price = price
        self.experience = experience
        self.score = score
        self.phone = phone


    def __repr__(self):
        return self.title
