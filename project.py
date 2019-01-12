from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import session as login_session
from flask import make_response

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

from db_setup import Base, User, Category, Items

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

import httplib2
import json
import random
import string
import requests


app = Flask(__name__)

#connect to database and create a session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

@app.route('/')
def Homepage():
    return "Home Page with default catalog view and login option"

@app.route('/catalog/')
def Catalog():
    session = DBSession()
    category = session.query(Category).all()
    items = session.query(Items).filter_by(category_id=Items.category_id)
    return render_template('catalog.html', category=category, items=items)

@app.route('/catalog/<int:category_id>')
def catalogItems(category_id):
    session = DBSession()
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Items).filter_by(category_id=category.id)
    return render_template('items.html', category=category, items=items)
    '''output = ''
    for i in items:
        output += i.item_name
        output += '<br>'
        output += i.description
        output += '<br>'
        output += str(i.id)
        output += '<br>'
    return output'''

#Create
@app.route('/catalog/item/new')
def newItem():
    return "After logging in, users can add new items"

#Edit
@app.route('/catalog/item/edit')
def editCatalogItem():
    return "User can edit catalog items here"

#Update
@app.route('/catalog/item/update')
def updateCatalogeItem():
    return "User can update catalog item here"

#Delete
@app.route('/catalog/item/delete')
def deleteCatalogItem():
    return "User can delete catalog item here"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)