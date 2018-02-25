import cv2
image = cv2.imread("/Users/abhi/Downloads/output_abhijit.jpg")
l = image.shape[0]
w = image.shape[1]

total  = 0.
counter = 0.
for i in range(0,l,1):
	for j in range(0,w,1):
		counter += 1
		total+= image[i][j][0]

print total/counter


