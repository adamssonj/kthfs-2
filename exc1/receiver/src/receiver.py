import rospy

from std_msgs.msg import Uint8


class Data:
	def __init__(self, x_value, y_value)
	self.x_value=x_value
	self.y_value=y_value
  

def listener():
	rospy.init_node(
		'nodeB', 
		anonymous=True)
	rospy.Subscriber(
		"sommarlund", 
		Uint8, 
		res=division)
	rospy.Publisher(
		'/kthfs/result',
		Uint8,
		queue_size=100)
    rate = rospy.Rate(20) 
	while not rospy.is_shutdown():
    	pub.publish(res)
		rospy.loginfo(res)
    	rate.sleep()


def division(
	data,
	objects):
	q=0.15
	res=data/q
	return res
	
	
if __name__ == '__main__':
    listener()


	
