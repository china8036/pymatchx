import numpy as np
import pyautogui
import cv2

img = pyautogui.screenshot() # x,y,w,h region=[0,0,100,100]
img.save('screenshot.png')
#img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
