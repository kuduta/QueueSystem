#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:25:09 2019

@author: nexpose
"""
import sys
import time
import sqlalchemy as db
import pandas as pd
from datetime import datetime

from flask import Flask , request


app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

engine = db.create_engine('sqlite:///queue.sqlite')
connection = engine.connect()
metadata=db.MetaData()
tbqueue = db.Table('tbqueue', metadata, autoload=True, autoload_with=engine)

'''
result = session.query(tbqueue).all()
for row in result:
   print (row)

type(result)
'''


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


'''
query=db.select([tbqueue])
result = connection.execute(query)

for row in result:
    print(row)
'''    

@app.route('/addque/<numtype>',methods=['GET'])
def addqueue(numtype):
    #1. check type of queue in table tbqueue type have 6 type
    dtsearch = datetime.now().strftime('%Y-%m-%d')
    query=db.select([tbqueue]).where(db.and_(tbqueue.columns.dtReqest_.like(dtsearch+'%'),\
                    tbqueue.columns.numType_ == numtype)).order_by(tbqueue.columns.id.desc()).limit(1)
    result = connection.execute(query)
    df = pd.DataFrame(result)
    # df[1] is number queue
    
    if df[1] != "":
        number = int(df[1])
        quenumber = numtype+str(number).zfill(4)
    else :
        number = 1
        quenumber = numtype+str(number).zfill(4)
        

    que = Queue()
    que.enqueue(quenumber)      
    
    
    
        
    
        
    #insert data to db and add queue
    
        
        
        
    #2. if type of queue is empty add queue in type qu
    #3.    
     
    #numtype = request.args.get('numtype')
    #dtnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return "Add Queue {}".format(numtype)

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
