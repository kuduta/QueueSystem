"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.

command >>> from api import db
command >>> db.create_all()
"""


import os
import queue
import pygame
import time
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'queue.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)



##### class play sound
class playsound:
    def playsound(num):
        pygame.init()
        #pygame.mixer.music.load("sounds/"+ str(num)+".mp3")
        pygame.mixer.music.load("sound/"+ str(num)+".wav")
        pygame.mixer.music.play()
        time.sleep(1.1)

######## end classs playsound


###### Start classs queue #######
class Queue:

  #Constructor creates a list
  def __init__(self):
      self.queue = list()

  #Adding elements to queue
  def enqueue(self,data):
      #Checking to avoid duplicate entry (not mandatory)
      if data not in self.queue:
          self.queue.insert(0,data)
          return True
      return False

  #Removing the last element from the queue
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("Queue Empty!")

  #Getting the size of the queue
  def size(self):
      return len(self.queue)

  #printing the elements of the queue
  def printQueue(self):
      return self.queue

###### end classs queue #######




# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app



class Data(db.Model):
    #Table name
    __tablename__ = "tbqueue"
    id = db.Column(db.Integer, primary_key=True)
    numQue_ = db.Column(db.String(10))
    numberType_ = db.Column(db.String(10))
    counter_ = db.Column(db.String(10))
    dtReqest_ = db.Column(db.String(30))
    dtStart_ = db.Column(db.String(30))
    dtStop_ = db.Column(db.String(30))
    
    def __init__(self, numQue_, numType_, counter_, dtReqest_, dtStart_, dtStop_  ):
        self.numQue_ = numQue_
        self.numType_ = numType_
        self.counter_ = counter_
        self.dtReqest_ = dtReqest_
        self.dtStart_ = dtStart_
        self.dtStop_ = dtStop_




@app.route('/addque')
def addqueue():
	return "Add Queue"

@app.route('/reqque')
def reqqueue():
	return "Reqest Queue"


@app.route('/startque')
def startqueue():
	return "Start Queue"

@app.route('/endque')
def endqueue():
	return "End Queue"

@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
