from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import session as login_session
from flask import make_response

from flask_dance.contrib.google import make_google_blueprint, google

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

#Enable login without HTTPS
import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


app = Flask(__name__)

#connect to database and create a session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

#Google Login using Flask Dance #####

google_blueprint = make_google_blueprint(
    client_id = '1059882579334-9pou6o75d96ls5agole7l6apm6vp6p8k.apps.googleusercontent.com',
    client_secret = 'uZ0J_cLBjEWnX8EXbzn7ZWv9'
)

app.register_blueprint(google_blueprint, url_prefix='/google_login')

@app.route('/google')
def googleLogin():
    if not google.authorized:
        return redirect(url_for('google.login'))
    account_info = google.get("/oauth2/v2/userinfo")

    if account_info.ok:
        account_info_json = account_info.json()
        return "You are {} on Google".format(account_info_json['name'])





#JSON ENDPOINTS Work in Progress ######

@app.route('/catalog/JSON')
def catalogJSON():
    session = DBSession()
    catalog = session.query(Category).all()
    return jsonify(catalog=[r.serialize for r in catalog])

@app.route('/catalog/users/JSON')
def usersJSON():
    session = DBSession()
    users = session.query(User).all()
    return jsonify(users=[r.serialize for r in users])

@app.route('/catalog/items/JSON')
def allItemsJSON():
    session = DBSession()
    items = session.query(Items).all()
    return eval(str(items))
    #return jsonify(items=[r.serialize for r in items])

@app.route('/catalog/<category_id>/JSON')
def itemsJSON(category_id):
    session = DBSession()
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Items).filter_by(category_id=category.id)
    #return str(items)
    return jsonify(tems=[r.serialize for r in items])

######################

@app.route('/')
@app.route('/catalog/')
def Catalog():
    session = DBSession()
    category = session.query(Category).all()
    items = session.query(Items).filter_by(category_id=Items.category_id)
    return render_template('catalog.html', category=category, items=items)

@app.route('/catalog/<category_id>')
def catalogItems(category_id):
    session = DBSession()
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Items).filter_by(category_id=category.id)
    return render_template('items.html', category=category, items=items)

#Create
@app.route('/catalog/<int:category_id>/new/', methods=['GET', 'POST'])
def newItem(category_id):
    session = DBSession()
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Items).filter_by(category_id=category.id)
    #user_id = session.query(Items).filter_by(user_id=Items.user_id)

    if request.method == 'POST':
        newItem = Items(
            item_name=request.form['name'],
            description=request.form['description'], 
            category_id=category.id, user_id=1
            )
        session.add(newItem)
        session.commit()
        flash('New Item Successfully Created')
        return redirect(url_for('catalogItems', category_id=category_id))
    else:
        return render_template('newItem.html', category=category, items=items)

#Edit
@app.route('/catalog/<int:category_id>/<int:item_id>/edit/', 
    methods=['GET', 'POST'])
def editCatalogItem(category_id, item_id):
    session = DBSession()
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Items).filter_by(category_id=category.id)
    itemToEdit = session.query(Items).filter_by(id=item_id).one()

    if request.method == 'POST':
        itemToEdit.item_name = request.form['name']
        itemToEdit.description = request.form['description']
        session.add(itemToEdit)
        session.commit()
        flash('Item edited successfully!')
        return redirect(url_for('catalogItems', category_id=category_id))
    else:
        return render_template('editItem.html', category=category, items=items, item=itemToEdit)

#Delete
@app.route('/catalog/<int:category_id>/<int:item_id>/delete/', 
    methods=['GET', 'POST'])
def deleteCatalogItem(category_id, item_id):
    session = DBSession()
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Items).filter_by(category_id=category.id)
    itemToDelete = session.query(Items).filter_by(id=item_id).one()

    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Item Deleted Successfully')
        return redirect(url_for('catalogItems', category_id=category_id))
    else:
        return render_template('deleteItem.html', category=category, items=items, item=itemToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)