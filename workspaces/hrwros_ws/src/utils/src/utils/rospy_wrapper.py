import rospy
import random

class RospyWrapper:
    def __init__(self):
        # Initialize any custom attributes if necessary
        pass

    def __getattr__(self, name):
        """
        This method is called when trying to access an attribute that doesn't exist on this instance.
        It delegates the call to the rospy module.
        """
        return getattr(rospy, name)

    # Add your custom methods here
    def my_custom_function(self):
        rospy.loginfo("This is a custom function added to rospy.")
    
    def distSensorData(self,sensor_type, min_range, max_range):
        if sensor_type != 0:
            print("Sensor type not supported!")
            return -1
        else:
            if random.uniform(0.0, 1.0) < 0.95:
                return max_range
            else:
                return random.uniform(min_range, max_range)
