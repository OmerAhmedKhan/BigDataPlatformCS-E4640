import requests
import time
import grequests



def do_something(tick):
    print(time.clock() - tick)

tick = time.clock()
rs=(grequests.post("http://127.0.0.1:5000/write/", data={"app": "omer"},hooks = {'response' : do_something(tick)}) for x in range(0,100) )
grequests.map(rs)