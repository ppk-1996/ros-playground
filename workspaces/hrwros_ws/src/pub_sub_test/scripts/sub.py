#!/usr/bin/env python
import rospy
from pub_sub_test.msg import SensorInformation


class Sub:
    def __init__(self) -> None:
        self.sub = rospy.Subscriber("/pub_test", SensorInformation, self.sub_cb)

    def sub_cb(self, data):

        rospy.loginfo(data.maker_name)


if __name__ == "__main__":
    rospy.init_node("sub_test_node")
    s = Sub()
    rospy.spin()
