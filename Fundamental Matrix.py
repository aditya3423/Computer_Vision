import cv2
import numpy as np
from numpy.linalg import eig

img = cv2.imread('MN.jpg')
img2 = cv2.imread('MM.jpg')
point_matrix1 = []
point_matrix2 = []
point_matrix_new1 = []
point_matrix_new2 = []
count1 = 0
count2 = 0
count_new1 = 0
count_new2 = 0
all_1 = []
h = []


#To get new image coordinates for testing fundamental matrix from image 1
def mouse_click_new(event, x, y, flags, param):
    global count_new1
    global point_matrix_new1
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix_new1.append([x, y, 1])
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(count_new1 + 1) , (x, y), font, 1, (90, 255, 0), 2)
        cv2.imshow('image', img)
        count_new1 += 1


#To get new image coordinates for testing fundamental matrix from image 2
def mouse_click_new2(event, x, y, flags, param):
    global count_new2
    global point_matrix_new2
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix_new2.append([x, y, 1])
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img2, str(count_new2 + 1) , (x, y), font, 1, (90, 255, 0), 2)
        cv2.imshow('image', img2)
        count_new2 += 1


#To get image coordinates for making fundamental matrix from image 1
def mouse_click1(event, x, y, flags, param):
    global count1
    global point_matrix1
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix1.append([x, y])
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(img, str(count1 + 1), (x, y), font, 1, (255, 102, 0), 2)
        cv2.imshow('image', img)
        count1 += 1


#To get image coordinates for making fundamental matrix from image 2
def mouse_click2(event, x, y, flags, param):
    global count2
    global point_matrix2
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix2.append([x, y])
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(img2, str(count2 + 1), (x, y), font, 1, (255, 102, 0), 2)
        cv2.imshow('image', img2)
        count2 += 1


#Finding similar points
def similar_points(img, img2, a):
    global point_matrix1
    global point_matrix2
    for i in range(int(a)):
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', mouse_click1)
        cv2.waitKey(0)
        cv2.imshow('image', img2)
        cv2.setMouseCallback('image', mouse_click2)
        cv2.waitKey(0)


#Fundamental Matrix
def f_matrix(a, b):
    global all_1
    global h
    for i in range(len(a)):
        x = a[i][0]
        y = a[i][1]
        x_ = b[i][0]
        y_ = b[i][1]
        row1 = [x*x_, x_*y, x_, y_*x, y_*y, y_, x, y, 1]
        all_1.append(row1)
    w, v, p = np.linalg.svd(all_1)
    f = p[-1].reshape(3, 3)
    f = f / f[2][2]
    print("Fundamental Matrix:\n", f)
    test(f)


#initiating the program
def ha(i1, i2, a):
    global point_matrix1
    global point_matrix2
    similar_points(i1, i2, a)
    point_matrix1 = np.array(point_matrix1)
    point_matrix2 = np.array(point_matrix2)
    cv2.imwrite("C:/Users/aksha/Desktop/NewImageA.jpg", img)
    cv2.imwrite("C:/Users/aksha/Desktop/NewImageB.jpg", img2)
    f_matrix(point_matrix1, point_matrix2)


#testing the accuracy of Fundamental Matrix
def test(f):
    global point_matrix_new1
    global point_matrix_new2
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', mouse_click_new)
    cv2.waitKey(0)
    cv2.imshow('image', img2)
    cv2.setMouseCallback('image', mouse_click_new2)
    cv2.waitKey(0)
    for i in range(len(point_matrix_new1)):
        p1 = (np.array(point_matrix_new2[i])).transpose()
        p2 = np.array(point_matrix_new1[i])
        a = np.matmul(p1, f)
        b = np.matmul(a, p2)
        print(i,". {x1 ",p1, "x2: ",p2,"}x1T.F.x2 = ", b)


ha(img, img2, 1)
cv2.destroyAllWindows()
