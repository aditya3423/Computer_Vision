import cv2
import numpy as np

img = cv2.imread('3D.jpg')
point_matrix1 = []
point_matrix2 = []
count1 = 0
all = []

def mouse_click(event, x, y, flags, param):
    global count1
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix1.append([x, y])
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(count1 + 1), (x, y), font, 1, (90, 255, 0), 2)
        cv2.imshow('image', img)
        count1 += 1


def initiate(i1):
    global point_matrix1
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', mouse_click)
    cv2.waitKey(0)
    point_matrix1 = np.array(point_matrix1)
    for at in point_matrix1:
        att = input("Enter the correlated 3D point: ")
        point_matrix2.append(att.split(','))
    Three_D(point_matrix1, point_matrix2)


def Three_D(a, b):
    global P
    global all
    for i in range(len(a)):
        x = a[i][0]
        y = a[i][1]
        X = int(b[i][0])
        Y = int(b[i][1])
        Z = int(b[i][2])
        row1 = [-X, -Y, -Z, -1, 0, 0, 0, 0, x*X, x*Y, x*Z, x]
        row2 = [0, 0, 0, 0, -X, -Y, -Z, -1, y*X, y*Y, y*Z, y]
        all.append(row1)
        all.append(row2)
    t1, t2, t3 = np.linalg.svd(all)
    P = t3[-1].reshape(3, 4)
    P = P/ P[2][3]
    print("P\n", P)
    test(P)


def test(P):
    X, Y, Z = input("Enter a 3D point: ").split(',')
    a = [int(X), int(Y), int(Z), 1]
    t = np.dot(P, a)
    t = t/t[2]
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.circle(img, (int(t[0]), int(t[1])), 2, (255, 0, 0), 1)
    cv2.putText(img, (str(a[0:3])) , (int(t[0]), int(t[1])), font, 1, (255, 0, 0), 2)
    cv2.imshow('image', img)
    cv2.waitKey(0)


initiate(img)

