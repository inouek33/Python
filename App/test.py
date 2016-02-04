# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:43:24 2016

@author: inouek
"""

from todoitem import ToDoItem
from datetime import datetime

i = ToDoItem('time', 'desc', datetime(2012,12,12,10,0))
print(i)

i.title = 'another title'
print(i)