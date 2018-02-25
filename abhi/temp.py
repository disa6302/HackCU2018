def populate_gallery(title, url):
	import json
	import datetime


	now = datetime.datetime.now()
	f = open('/Users/abhi/Downloads/hackcu/gallery.js','rb')
	data = ''
	for line in f.readlines():
		temp = line.replace('\n',' ')
		data += temp

	photos = json.loads(data)
	photos['photos'] = []

	print photos
	title ='Hi'
	url =''

	temp = {u'title': u''+title, u'url': u''+url, u'location': u'Rescue location', u'date': u''+str(now), u'thumb_url': u''+url, u'id': u'1'}
	print temp
	photos['photos'].append(temp)
	print photos
	with open('/Users/abhi/Downloads/hackcu/gallery.js', 'w') as outfile:
     		json.dump(photos, outfile)
	f.close()


import numpy as np
import cv2
img = cv2.imread('/Users/abhi/Downloads/hackcu/Photo-Gallery/static/video/u_received_file_5.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Temp: 1", (20,10), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0,255,0))
cv2.imwrite('/Users/abhi/Downloads/hackcu/Photo-Gallery/static/video/u_received_file_5.jpg',img)
height, width, channels = img.shape
print height, width, channels

