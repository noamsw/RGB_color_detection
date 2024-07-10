# importing required libraries 
import cv2 
import numpy as np
import time
import matplotlib.pyplot as plt

# taking the input from webcam 
vid = cv2.VideoCapture(0) 

# capturing the current frame 
_, frame = vid.read()
# displaying the current frame 
cv2.imshow("frame", frame)
cv2.waitKey(500)

blue, green, red = cv2.split(frame)

# running while loop just to make sure that 
# our program keep running until we stop it 
while True: 

	# capturing the current frame 
	_, frame = vid.read() 

	# displaying the current frame 
	cv2.imshow("frame", frame)
	
	cv2.waitKey(1000)

	# setting values for base colors 
	b = frame[:, :, 2] 
	g = frame[:, :, 1] 
	r = frame[:, :, 0] 

	# computing the mean 
	b_mean = np.mean(b) 
	g_mean = np.mean(g) 
	r_mean = np.mean(r) 
	print(f'r mean: {r_mean}')
	print(f'g mean: {g_mean}')
	print(f'b mean: {b_mean}')
	# displaying the most prominent color 
	if (b_mean > g_mean and b_mean > r_mean): 
		print("Blue") 
	elif (g_mean > r_mean and g_mean > b_mean): 
		print("Green") 
	else: 
		print("Red")