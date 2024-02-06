#!/usr/bin/env python
from __future__ import print_function
import sys
import rospy
from beginner_tutorial.srv import *

def multiplication_client(x, y):
    # TODO 1: make the code block until the service named "multiply_two_floats" is available.
    rospy.wait_for_service('beginner_srv')
    try:
        pass
        # TODO 2: create a handle for calling the service
        multitask = rospy.ServiceProxy('beginner_srv',beginner_srv)
        # TODO 3: use this handle just like a normal function and call it
        num = multitask(x,y)
        # TODO 4: return the product
        return num
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        rospy.loginfo(usage())
        sys.exit(1)
    print("Requesting %s + %s"%(x, y))
    print("%s + %s = %s"%(x, y, multiplication_client(x, y)))

