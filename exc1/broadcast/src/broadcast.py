import rospy

from std_msgs.msg import Uint8


def broadcaster():
    pub = rospy.Publisher(
		'sommarlund', 
		Uint8, 
		queue_size=100)
    rospy.init_node(
		'nodeA', 
		anonymous=True)
    rate = rospy.Rate(20)
    n=4
    k=1
    i=0
    while not rospy.is_shutdown():
		i=i+1
        k=k*n
        rospy.loginfo(k)
        pub.publish(k)
        rate.sleep()


if __name__ == '__main__':
    broadcaster()
