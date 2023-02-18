import cv2 
import numpy as np 
import RPI.GPIO as IO 
import time 
 
IO.setwarnings(False) 
x = 1 
IO.setmode(IO.BCM) 
IO.setup(5, IO.OUT) 
IO.setup(17, IO.OUT) 
 
color_1 = input() 
color_2 = input() 
 
cam = cv2.VideoCapture(0) 
 
while True: 
    _, frame = cam.read() 
    #cv2.imshow("frame", frame) 
 
 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_blue = np.array([100, 50, 50]) 
    upper_blue = np.array([110, 255, 255]) 
    lower_red = np.array([0, 50, 50]) 
    upper_red = np.array([10, 255, 255]) 
    lower_green = np.array([50, 100, 100]) 
    upper_green = np.array([70, 255, 255]) 
    lower_yellow = np.array([22, 93, 0]) 
    upper_yellow = np.array([45, 255, 255]) 
 
 
    mask_b = cv2.inRange(hsv, lower_blue, upper_blue) 
    result_b = cv2.bitwise_and(frame, frame, mask=mask_b) 
    mask_r = cv2.inRange(hsv, lower_red, upper_red) 
    result_r = cv2.bitwise_and(frame, frame, mask=mask_r) 
    mask_g = cv2.inRange(hsv, lower_green, upper_green) 
    result_g = cv2.bitwise_and(frame, frame, mask=mask_g) 
    mask_y = cv2.inRange(hsv, lower_yellow, upper_yellow) 
    result_y = cv2.bitwise_and(frame, frame, mask=mask_y) 
 
    IO.output(5,1) 
    IO.output(17, 0) 
 
    if color_1 == 'blue': 
        color_1 = result_b 
        IO.output(5, 0) 
        IO.output(17, 1) 
        for y in range(x): 
            time.sleep(1) 
        if color_2 == 'red' or 'green' or 'yellow': 
            IO.output(17,1) 
            for y in range(x): 
                time.sleep(1) 
    elif color_1 == 'yellow': 
        color_1 = result_y 
        IO.output(5, 0) 
        IO.output(17, 1) 
        for y in range(x): 
            time.sleep(1) 
 
        if color_2 == 'red' or 'green' or 'blue': 
            IO.output(17, 1) 
            for y in range(x): 
                time.sleep(1) 
 
    elif color_1 == 'red': 
        color_1 = result_r 
        IO.output(5, 0) 
        IO.output(17, 1) 
        for y in range(x): 
            time.sleep(1) 
 
        if color_2 == 'yellow' or 'green' or 'blue': 
            IO.output(17, 1) 
            for y in range(x): 
                time.sleep(1) 
 
    elif color_1 == 'green': 
        color_1 = result_g 
        IO.output(5, 0) 
        IO.output(17, 1) 
        for y in range(x): 
            time.sleep(1) 
 
        if color_2 == 'red' or 'yellow' or 'blue': 
            IO.output(17, 1) 
            for y in range(x): 
                time.sleep(1) 
 
 
    key = cv2.waitKey(25) 
    if key == 27: 
        break
