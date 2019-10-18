import numpy as np
import pyautogui
import cv2

img = pyautogui.screenshot() # x,y,w,h
#img.save('screenshot.png')

#target = cv2.imread("target.png")
target = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)

template = cv2.imread("template.png")

theight, twidth = template.shape[:2]

result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)

cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

strmin_val = str(min_val)

cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)

cv2.imshow("MatchResult----MatchingValue="+strmin_val,target)
cv2.waitKey()
cv2.destroyAllWindows()