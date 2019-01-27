from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Base, User, Category, Items

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Test User
test_user = User(name='Test User', email='tes@email.com')
session.add(test_user)
session.commit()

# ategories to add to the database
category1 = Category(category_name='Soccer')
session.add(category1)
session.commit()

category2 = Category(category_name='Baseball')
session.add(category2)
session.commit()

category3 = Category(category_name='Football')
session.add(category3)
session.commit()

category4 = Category(category_name='Hockey')
session.add(category4)
session.commit()

category5 = Category(category_name='Frisbee')
session.add(category5)
session.commit()

category6 = Category(category_name='Snowboarding')
session.add(category6)
session.commit()

category7 = Category(category_name='Foosball')
session.add(category7)
session.commit()

category8 = Category(category_name='Rock Climbing')
session.add(category8)
session.commit()

# items to add to the database
item1 = Items(item_name='Soccer Ball', category=category1,
              description='A black and white ball to play soccer.',
              user_id=1)
session.add(item1)
session.commit()

item2 = Items(item_name='Baseball', category=category2,
              description='A white ball with red thread.',
              user_id=1)
session.add(item2)
session.commit()

item3 = Items(item_name='Football', category=category3,
              description='A brown, leather ball used for Football.',
              user_id=1)
session.add(item3)
session.commit()

item4 = Items(item_name='Hockey Stick', category=category4,
              description='A wooden stick used for hitting a hockey puck.',
              user_id=1)
session.add(item4)
session.commit()

item5 = Items(item_name='Frisbee', category=category5,
              description='A round plastic saucer.',
              user_id=1)
session.add(item5)
session.commit()

item6 = Items(item_name='Snowboard', category=category6,
              description='A long flat board used to ride on top of the snow.',
              user_id=1)
session.add(item6)
session.commit()

item7 = Items(item_name='Foosball ball', category=category7,
              description='A white and black ball used to play Foosball.',
              user_id=1)
session.add(item7)
session.commit()

item8 = Items(item_name='Climbing Shoes', category=category8,
              description='Shoes with extra grip used to climb up rock walls.',
              user_id=1)
session.add(item8)
session.commit()


print("Added items to the database!")
