#!/usr/bin/env python

# SETUP: Import global modules
import TweetStreetCam
import buzz


def start():
	try:
		g = TweetStreetCam.GraffCam()
		mentions = g.GetMentions()
		if mentions:
			for tweet in mentions:
				buzz.startMotor()
				g.ActionTweet(tweet)
		
		for tweet in g.GetStream():
			if 'text' in tweet:
				buzz.startMotor()
				g.ActionTweet(tweet)
	except:
		pass
	finally:
		g.camera.close()
'''
class startCam:
	g = TweetStreetCam.GraffCam()
	mentions = g.GetMentions()

	def run():
		if mentions:
			for tweet in mentions:
				g.ActionTweet(tweet)
		
		for tweet in g.GetStream():
			if 'text' in tweet:
				g.ActionTweet(tweet)
'''


		
