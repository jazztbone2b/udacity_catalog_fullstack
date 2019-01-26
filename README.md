# Sports Catalog Application

A basic fullstack application that demonstrates CRUD functionality and OAUTH support for Google + Login and authentication/authorization.

## Requirements and Dependencies

 1. [Python 2.7](https://www.python.org/download/releases/2.7/)
 2. [Flask](http://flask.pocoo.org/docs/1.0/)
 3. [Flask-Dance](https://flask-dance.readthedocs.io/en/latest/index.html)
 4. [Sqlachemy](https://www.sqlalchemy.org/)

## Quickstart

1. Be sure the required dependencies are installed by running the following in your terminal:

    * To install Flask: `pip install Flask`
    * To install Flask-Dance: `pip install Flask-Dance`
    * To install Sqlalchemy: `pip install SQLAlchemy`

2. Clone this repository to a folder containing your Vagrant file: `git clone https://github.com/jazztbone2b/udacity_catalog_fullstack.git`

3. Open a terminal window and navigate to the folder containing this project

4. Run `vagrant up` then `vagrant ssh` to start the virtual machine and ssh into it

5. Navigate to the project directory in the virtual machine by running `cd /vagrant/udacity_catalog_fullstack`

6. Type the following commands to create the database, populate the database, and run the application:

    * `python db_setup.py`
    * `python items.py`
    * `python project.py`

7. Once the app is running, go to `http://localhost:5000` in your browser

## JSON API Endpoints

* http://localhost:5000/catalog/JSON
* http://localhost:5000/catalog/items/JSON

## Important things to note

* Only Google Plus logins are currently supported. You must have a Google Plus account in order to sign in and use this application

* You may need to run `sudo pip install` ... in order to install the dependencies
