#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from io import BytesIO
import ffmpeg


def camera_callback(msg):
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")

        if cv_image is not None:
            cv2.imshow("Decoded Image", cv_image)
            cv2.waitKey(1)
        else:
            rospy.logwarn("Decoded image is None")
    except Exception as e:
        rospy.logerr(f"Error decoding image: {e}")

      
def main():
    rospy.init_node('image_subscriber')
    rospy.Subscriber('/tello/image_raw', Image, camera_callback)
    rospy.spin()

if __name__ == "__main__":
    main()
