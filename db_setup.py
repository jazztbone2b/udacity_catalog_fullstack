from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    email = Column(String(100), nullable=False)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'email': self.email,
            'id': self.id,
        }

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=False)

    @property
    def serialize(self):
        return {
            'category_name': self.category_name,
            'id': self.id,
        }

class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    item_name = Column(String(50), nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    description = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'item_name': self.item_name,
            'date_created': self.date_created,
            'description': self.description,
            'id': self.id,
        }

engine = create_engine('sqlite:///catalog.db', connect_args={'check_same_thread': False})

Base.metadata.create_all(engine)

print("Database created!")
