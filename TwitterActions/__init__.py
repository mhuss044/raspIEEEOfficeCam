import os
import sys

class TA():
	_PHOTO_HASHTAGS = ['snap']

	def __init__(self, home_path, api, logging):
		self.api = api
		self.home_path = home_path
		self.logging = logging

	def check_status(self, request):
		print request.text
		if request.status_code < 200 or request.status_code > 299:
			print(request.status_code)
			print(request.text)
			sys.exit(0)

	def is_photo(self, tweet):
		e = tweet['entities']
		photo = False
		if e['hashtags']:
                        for hashtag in e['hashtags']:
				if any(hashtag['text'] in s for s in self._PHOTO_HASHTAGS):
					photo = True

		return photo

	def upload_image(self, filename):
		# Upload a file
		file = open(filename, 'rb')
		data = file.read()

		self.logging.info('Uploading picture')
		request = self.api.request('media/upload', None, {'media': data})
		#self.logging.info('Picture request: ' + str(request.json()))
		return request
