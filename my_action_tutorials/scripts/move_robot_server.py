#!/usr/bin/env python

import rospy 
import actionlib
from my_robot_msgs.msg import MoveRobotFeedback, MoveRobotAction, MoveRobotResult

class MoveRobotServer:
	def __init__(self):
		self._as = actionlib.SimpleActionServer('/move_robot',
			MoveRobotAction, execute_cb = self.on_goal, auto_start=False) 
		self._as.start()

		self._current_position = 50
		rospy.loginfo('Server has been started')

	def on_goal(self, goal):
		rospy.loginfo('A goal is received')
		rospy.loginfo(goal)

		goal_position = goal.position
		velocity = goal.velocity
		
		success = False
		preempted = False
		invalid_parameters = False
		message = ''
		rate = rospy.Rate(0.2)

		if goal_position < 0 or goal_position > 100:
			message = 'Invalid goal'
			invalid_parameters = True

		while not rospy.is_shutdown() and not invalid_parameters:
			# check for goal termination
			if self._as.is_preempt_requested():
				preempted = True
				break

			# exec			
			diff = goal_position - self._current_position
			if diff == 0:
				success = True
				break
			elif diff < 0:
				self._current_position -= min(velocity, abs(diff))
			elif diff > 0:
				self._current_position += min(velocity, diff)


			# send feedback
			self.send_feedback()
			
			rate.sleep()
			
		# send result 
		result = MoveRobotResult()

		result.position = self._current_position
		result.message = message
		rospy.loginfo('Send goal result to client')			

		if preempted:
			message = 'Preempted'
			rospy.loginfo('Preempted')
			self._as.set_preempted(result)
		elif success:
			message = 'Success'
			rospy.loginfo('Success')
			self._as.set_succeeded(result)
		else:
			rospy.loginfo('Aborted')
			self._as.set_aborted(result)


	def send_feedback(self):
		feedback = MoveRobotFeedback()
		feedback.current_position = self._current_position
		self._as.publish_feedback(feedback)

	def callback(self):
		pass


if __name__ == '__main__':

	rospy.init_node('move_robot_server')	

	serv = MoveRobotServer()

	rospy.spin()
