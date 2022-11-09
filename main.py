import cv2
import matplotlib.pyplot as plt
import math
# drawing function
from numpy.ma import copy

from spot import Spot

points = []
spots = []
temp = []
counter = 0
draw = False
p1 = ()
p2 = ()


def draw_points(event, x, y, flags, params):
    global draw
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        temp.append((x, y))
        if len(temp) == 4:
            draw = True
    if event == cv2.EVENT_RBUTTONDOWN:
        for spot in spots:
            if FindPoint(spot[0][0],spot[0][1],spot[2][0],spot[2][1],x,y) or FindPoint(spot[1][0],spot[1][1],spot[3][0],spot[3][1],x,y):
                print(spot)
                points.remove(spot[0])
                points.remove(spot[1])
                points.remove(spot[2])
                points.remove(spot[3])
                spots.remove(spot)

def FindPoint(x1, y1, x2, y2, x, y) :
    if (x > x1 and x < x2 and  y > y1 and y < y2) :
        return True
    else:
        return False


path = 'pic2.png'
img = plt.imread(path, 0)
cap = cv2.VideoCapture('video1.mp4')

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", draw_points)

while True:
    _, frame = cap.read()

    for point in points:
        cv2.circle(frame, point, 5, (255, 0, 255), 5)
    for spot in spots:
        cv2.line(frame, (spot[0][0], spot[0][1]), (spot[1][0], spot[1][1]), (255, 0, 255), 2)
        cv2.line(frame, (spot[1][0], spot[1][1]), (spot[2][0], spot[2][1]), (255, 0, 255), 2)
        cv2.line(frame, (spot[2][0], spot[2][1]), (spot[3][0], spot[3][1]), (255, 0, 255), 2)
        cv2.line(frame, (spot[3][0], spot[3][1]), (spot[0][0], spot[0][1]), (255, 0, 255), 2)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(10) & 0xFF == 27:
        break
    if cv2.waitKey(10) == ord("n"):
        if draw:
            spots.append([(temp[0][0], temp[0][1]), (temp[1][0], temp[1][1]), (temp[2][0], temp[2][1]),
                          (temp[3][0], temp[3][1])])
            temp.clear()
            draw = False
    if cv2.waitKey(10) == ord("d"):
        spots.clear()
        points.clear()
        temp.clear()
        draw = False
        print(points)

cap.release()
cv2.destroyAllWindows()

























"""
       for i in range(0, len(points) - 1):
        cv2.line(img, (points[i][0], points[i][1]), (points[i + 1][0], points[i + 1][1]), (255, 0, 255), 5)
    if spots:
        for spot in spots:
            print(spot)
            cv2.line(img, (spot[0][0], spot[0][1]), (spot[1][0], spot[1][1]), (255, 0, 255), 5)
            cv2.line(img, (spot[1][0], spot[1][1]), (spot[2][0], spot[2][1]), (255, 0, 255), 5)
            cv2.line(img, (spot[2][0], spot[2][1]), (spot[3][0], spot[3][1]), (255, 0, 255), 5)
            cv2.line(img, (spot[3][0], spot[3][1]), (spot[0][0], spot[0][1]), (255, 0, 255), 5)

   
"""
