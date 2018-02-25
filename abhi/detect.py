#!/usr/bin/env python

import requests
import base64


image_url = '/Users/abhi/Downloads/arun.jpg'

if image_url.startswith('http'):
	data = image_url
else:
	with open(image_url, "rb") as image_file:
	    data = base64.b64encode(image_file.read())

# put your keys in the header
headers = {
    "app_id": "bf894930",
    "app_key": "e948eed7f57f4038b17a1f3c3f7f2d29"
}

payload = '{"image":"'+data+'"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)

import cv2
import urllib
import numpy as np

# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)

	# return the image
	return image

if image_url.startswith('http'):
	img = url_to_image(image_url)
else:
	img = cv2.imread(image_url,cv2.IMREAD_COLOR)
#cv2.imwrite("/Users/abhi/Downloads/photo.jpg",img)

a = r.json()
print a
counter = 1
for f in a["images"][0]["faces"]:
		X = f['topLeftX']
		Y = f['topLeftY']
		w = f['width']
		h = f['height']
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img,'Face : '+str(counter),(X, Y), font, 1,(0,255,0))
		cv2.rectangle(img, (X, Y), (X+w, X+h), (255,0,0), 2)
		counter += 1
		ethnicity = 'hispanic'
		if f['attributes']['asian'] > f['attributes'][ethnicity]:
			ethnicity = 'asian'
		elif f['attributes']['black'] > f['attributes'][ethnicity]:
			ethnicity = 'black'
		elif f['attributes']['white'] > f['attributes'][ethnicity]:
			ethnicity = 'white'

		gender = 'female'
		if f['attributes']['gender']['maleConfidence'] > f['attributes']['gender']['femaleConfidence'] :
			gender = 'male'

		age = f['attributes']['age']

		glasses = f['attributes']['glasses']

print 'Ethnicity: ', ethnicity,'Gender: ', gender,'Age: ', age,'Glasses: ', glasses
#cv2.imshow("lalala", img)
cv2.imwrite(r''+image_url, img)

