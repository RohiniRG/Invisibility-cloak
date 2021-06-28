import cv2
import numpy as np

cap = cv2.VideoCapture(0)
count = 0

while count <= 30:
    ret, bg = cap.read()
    count += 1

while True:
    ret, frame = cap.read()
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red1 = np.array([55, 50, 50])       
    upper_red1 = np.array([55, 255, 255])
    mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)

    lower_red2 = np.array([170, 40, 40])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
    
    final_mask = mask1 + mask2
    
    final_mask = cv2.morphologyEx(final_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2)
    final_mask = cv2.dilate(final_mask, np.ones((3, 3), np.uint8), iterations = 1)
    
    mask = cv2.bitwise_not(final_mask)
    
    op1 = cv2.bitwise_and(bg, bg, mask = final_mask)
    op2 = cv2.bitwise_and(frame, frame, mask = mask)
    final_op = cv2.addWeighted(op1, 1, op2, 1, 0)
  
    cv2.imshow("INVISIBILITY CLOAK", final_op)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
