#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time,datetime
import PyV8

class v8Doc(PyV8.JSClass):  
    def write(self, s):  
        print s.decode('utf-8')  
   
class Global(PyV8.JSClass):  
    def __init__(self):  
        self.document = v8Doc() 

today_time = datetime.datetime.now()
print today_time.strftime('%Y-%m-%d')

def get_js_curr_times():
    glob = Global()  
    ctxt = PyV8.JSContext(glob)  
    ctxt.enter()  
    func = ctxt.eval("""
                function getTimes(){
                    var myData = new Date();
                    var times = myData.getTime();
                    return times;
                }
             """)
    gettimes = ctxt.locals.getTimes
    times = gettimes()
    return '%d'%times
 
times = get_js_curr_times()
print times