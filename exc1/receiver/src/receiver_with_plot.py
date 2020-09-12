import rospy

from std_msgs.msg import Uint8

from matplotlib import style

import matplotlib.pyplot as plt

import matplotlib.animation as animation


#Init for plotting, should not actually be in here
objects=[]
style.use('fivethirtyeight')


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
		res=division[0])
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
	objects):ant to use that module by importing we have to comment out our call. Rather than that approach best approach is to use following code:
	q=0.15
	res=data/q
	obj = Data(data, res)
	objects.append(obj)
	return res, data


def prep_plot():
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)
	return fig, ax1


def plot(objects):
	[fig, ax1] = prepare_plot
	for o in objects:
		ax1.plot(o.x_value, o.y_value)
	
	
if __name__ == '__main__':
    listener()
	ani = animation.FuncAnimation(fig, plot, interval = 1000)
	plt.show()
