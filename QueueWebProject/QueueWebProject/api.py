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

from flask import Flask , request ,jsonify


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

que1 = Queue()
que2 = Queue()
que3 = Queue()
que4 = Queue()
que5 = Queue()

que5.enqueue('31231242')
que5.printQueue()
que5.dequeue()
'''
query=db.select([tbqueue])
result = connection.execute(query)

for row in result:
    print(row)
    
'''


def dbquery(typenumber):
    dtsearch = datetime.now().strftime('%Y-%m-%d')
    dtnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    query=db.select([tbqueue]).where(db.and_(tbqueue.columns.dtReqest_.like(dtsearch+'%'),\
                    tbqueue.columns.numType_ == typenumber)).order_by(tbqueue.columns.id.desc()).limit(1)
    result = connection.execute(query)
    df = pd.DataFrame(result)
        # df[1] is number queue
    
    if df[1] != "":
        number = int(df[1])
        quenumber = typenumber+str(number).zfill(4)
    else :
        number = 1
        quenumber = typenumber+str(number).zfill(4)
    
    return quenumber, dtnow
    
    
@app.route('/addque/<numtype>',methods=['GET'])
def addqueue(numtype):
    
        #1. check type of queue in table tbqueue type have 6 type
      
    
    if numtype == '1':
        #dbquery(numtype) 
        quenum,datenow = dbquery(numtype)
        que1.enqueue(quenum)
        
        ins = tbqueue.insert().values(numQue_=quenum, numType_=numtype, dtReqest_=datenow)
        connection.execute(ins)
       
        return jsonify( quenumber=quenum,sizeque=que1.size(), daterequest= datenow )
        

    elif numtype == '2':
        quenum,datenow = dbquery(numtype)
        que2.enqueue(quenum)
        
        ins = tbqueue.insert().values(numQue_=quenum, numType_=numtype, dtReqest_=datenow)
        connection.execute(ins)
       
        return jsonify( quenumber=quenum,sizeque=que2.size(), daterequest= datenow )
               
    elif numtype == '3':
        quenum,datenow = dbquery(numtype)
        que3.enqueue(quenum)
        
        ins = tbqueue.insert().values(numQue_=quenum, numType_=numtype, dtReqest_=datenow)
        connection.execute(ins)
       
        return jsonify( quenumber=quenum,sizeque=que3.size(), daterequest= datenow )
 
    elif numtype == '4':
        quenum,datenow = dbquery(numtype)
        que2.enqueue(quenum)
        
        ins = tbqueue.insert().values(numQue_=quenum, numType_=numtype, dtReqest_=datenow)
        connection.execute(ins)
       
        return jsonify( quenumber=quenum,sizeque=que2.size(), daterequest= datenow )
       
    elif numtype == '5':
        
        pquenum,datenow = dbquery(numtype)
        que2.enqueue(quenum)
        
        ins = tbqueue.insert().values(numQue_=quenum, numType_=numtype, dtReqest_=datenow)
        connection.execute(ins)
       
        return jsonify( quenumber=quenum,sizeque=que2.size(), daterequest= datenow )
    
    else:
        return 0
        
        
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
