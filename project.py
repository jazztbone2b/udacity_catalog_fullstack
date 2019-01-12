from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Category, Items
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

#connect to database and create a session
engine = create_engine('sqlite:///category_app.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def Homepage():
    return "Home Page with default catalog view and login option"

@app.route('/catalog')
def Catalog():
    return "User's catalog will be here"

@app.route('/catalog/item/new')
def newItem():
    return "After logging in, users can add new items"

@app.route('/catalog/item/edit')
def editCatalogItem():
    return "User can edit catalog items here"

@app.route('/catalog/item/update')
def updateCatalogeItem():
    return "User can update catalog item here"
    
@app.route('/catalog/item/delete')
def deleteCatalogItem():
    return "User can delete catalog item here"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)