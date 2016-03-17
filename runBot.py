import cBot

while True:
	cBot.start()
'''
while True:
	try:
		newStart = startCam() 
		newStart.run()
	except:
		pass
	finally: # want to restart cam, so be sure prev is gone
		try:
			newStart.g.camera.close()# ensure that cam res freed
		except:
			pass
'''
