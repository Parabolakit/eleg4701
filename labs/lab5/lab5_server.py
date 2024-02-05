#!/usr/bin/env python

import rospy

# TODO 1: import the service type you need


def handle_multiplication(req):
    # TODO 2: figure out what should be returned and modify the printed message
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
   

def lab5_server():
    rospy.init_node('lab5_server')
    
    # TODO 3: write a service using rospy

  
    print("Ready to do multiplication.")
    rospy.spin()

if __name__ == "__main__":
    lab5_server()
