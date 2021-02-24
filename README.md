# Project 7: GrandPy Bot
This application was devloped as part of coding learning with Open Classroom.
The programme is a chat bot which respond a google maps and an wiki text to a asked place.

This works with google API :  https://developers.google.com/places  
and wikimedia API : https://www.mediawiki.org/wiki/API:Main_page  

The programme was devlopp with Flask framework : https://flask.palletsprojects.com/en/1.1.x/

## Installation

- Install python : https://www.python.org/downloads/
- Install pipenv :  
``pip install --user pipenv``
### Pull
``git clone https://github.com/Nicolasdvl/P7``

### Create virtual environment
``pipenv install``

### Create file .env
Create a file name ".env" at the project root.  
Write the next line in the file with your information :  
``GMAPS_KEY = <YOUR API KEY>``

## Usage

Use the virtual environment :  
``pipenv shell``  
Launch the Flask application :  
``python main.py``

## Deployment

The next steps explain how deploy the application on heroku.  
### Install heroku
 https://devcenter.heroku.com/articles/heroku-cli#download-and-install  
### Log in to heroku CLI  
``heroku login``  
### Deploy the app  
``heroku create``  
``git push heroku main``
### Procfile
The procfile is already define on the git depo.
### Config var
Config vars in settings of the heroku app : https://devcenter.heroku.com/articles/config-vars