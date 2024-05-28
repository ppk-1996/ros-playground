#!/usr/bin/env python
from pub_sub_test.msg import SensorInformation
from utils.rospy_wrapper import rospy


class Pub:
    def __init__(self):
        self.pub = rospy.Publisher("/pub_test", SensorInformation, queue_size=10)
        self.rate = rospy.Rate(10)

    def publish_to_topic(self):
        while not rospy.is_shutdown():
            sensor_info = SensorInformation()
            sensor_info.sensor_data.header.stamp = rospy.Time.now()
            sensor_info.sensor_data.header.frame_id = "distance_sensor_frame"
            sensor_info.sensor_data.radiation_type = sensor_info.sensor_data.ULTRASOUND
            sensor_info.sensor_data.field_of_view = 0.5
            sensor_info.sensor_data.min_range = 0.02
            sensor_info.sensor_data.max_range = 2.00
            sensor_info.maker_name = "The Ultrasound Company"
            sensor_info.part_number = 123456
            sensor_info.sensor_data.range = rospy.distSensorData(
                sensor_info.sensor_data.radiation_type,
                sensor_info.sensor_data.min_range,
                sensor_info.sensor_data.max_range,
            )

            self.pub.publish(sensor_info)
            self.rate.sleep()


if __name__ == "__main__":
    rospy.init_node("pub_test_node")
    try:
        Pub().publish_to_topic()
    except rospy.ROSInterruptException:
        rospy.logerr("Pub Node Shutting Down")
        pass
