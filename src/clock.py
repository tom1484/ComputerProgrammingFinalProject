#!/usr/bin/env python
import rospy

import time
from std_msgs.msg import Time
from rosgraph_msgs.msg import Clock


if __name__ == "__main__":
    try:
        rospy.init_node("clock", anonymous=False)
        clock_pub = rospy.Publisher('clock', Clock, queue_size=10)

        rate = 200

        zero_time = time.time()
        counter = 0
        while not rospy.is_shutdown():
            clock_pub.publish(rospy.Time.from_sec(rospy.get_time()))
            counter += 1
            while (time.time() - zero_time) * rate < counter:
                pass

    except (rospy.ROSInterruptException, KeyboardInterrupt):
        rospy.signal_shutdown("Process ended")
        sys.exit()

    except:
        pass

