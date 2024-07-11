# importing required libraries 
import cv2 
import numpy as np	
import matplotlib.pyplot as plt




def captureImage(vid):
	# capturing the current frame 
	_, frame = vid.read() 

	# displaying the current frame 
	cv2.imshow("frame", frame)
	
	cv2.waitKey(1000)
	return frame

def returnColorWithHighestMean(frame):
	blue_channel, green_channel, red_channel = cv2.split(frame)

	# computing the mean 
	b_mean = np.mean(blue_channel) 
	g_mean = np.mean(green_channel) 
	r_mean = np.mean(red_channel) 
	print(f'r mean: {r_mean}')
	print(f'g mean: {g_mean}')
	print(f'b mean: {b_mean}')
	# displaying the most prominent color 
	if (b_mean > g_mean and b_mean > r_mean): 
		return("Blue") 
	elif (g_mean > r_mean and g_mean > b_mean): 
		return("Green") 
	else: 
		return("Red")

def main():
	# taking the input from webcam 
	vid = cv2.VideoCapture(0) 
	# running while loop just to make sure that 
	# our program keep running until we stop it 
	while True: 

		frame = captureImage(vid)
		color = returnColorWithHighestMean(frame)
		print(color)

if __name__ == '__main__':
	main()