# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:00:54 2016

@author: inouek
"""

# -*- coding: utf-8 -*-

import random
 
if __name__ == "__main__":
 
    print random.random()
     
    print random.uniform(1,100)
     
    print random.randint(1,100)
     
    print random.choice("1234567890abcdefghij")
 
    sample_list = ["python","izm","com","random","sample"]
    random.shuffle(sample_list)
    print sample_list
