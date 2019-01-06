from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_email = Column(String(100), nullable=False)

    @property
    def serialize(self):
        return {
            'user_name'  : self.user_name,
            'user_email' : self.user_email,
            'id'         : self.id,
        }
        
class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(25), nullable=False)

    @property
    def serialize(self):
        return {
            'category_name' : self.category_name,
            'id'            : self.id,
        }

class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    item_name = Column(String(25), nullable=False)
    category = Column(String(25), nullable=False)
    description = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'item_name'   : self.item_name,
            'category'    : self.category,
            'description' : self.description,
            'user_id'     : self.user_id,
            'id'          : self.id,
        }

engine = create_engine('sqlite:///categories.db', connect_args={'check_same_thread': False})

Base.metadata.create_all(engine)

print("Database created!")
