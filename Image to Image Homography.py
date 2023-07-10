import cv2
import numpy as np
from numpy.linalg import eig

img = cv2.imread('MM.jpg')
img2 = cv2.imread('MN.jpg')
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


def mouse_click_new(event, x, y, flags, param):
    global count_new1
    global point_matrix_new1
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix_new1.append([x, y])
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(count_new1 + 1) , (x, y), font, 1, (90, 255, 0), 2)
        cv2.imshow('image', img)
        count_new1 += 1


def mouse_click1(event, x, y, flags, param):
    global count1
    global point_matrix1
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix1.append([x, y])
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(img, str(count1 + 1), (x, y), font, 1, (255, 255, 0), 2)
        cv2.imshow('image', img)
        count1 += 1


def mouse_click2(event, x, y, flags, param):
    global count2
    global point_matrix2
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix2.append([x, y])
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(img2, str(count2 + 1), (x, y), font, 1, (255, 255, 0), 2)
        cv2.imshow('image', img2)
        count2 += 1


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


def h_graph_n(a, b):
    global all_1
    global h
    for i in range(len(a)):
        x = a[i][0]
        y = a[i][1]
        x_ = b[i][0]
        y_ = b[i][1]
        row1 = [-x, -y, -1, 0, 0, 0, x_*x, x_*y, x_]
        row2 = [0, 0, 0, -x, -y, -1, y_*x, y_*y, y_]
        all_1.append(row1)
        all_1.append(row2)
    w, v, x = np.linalg.svd(all_1)
    h = x[-1].reshape(3, 3)
    h = h / h[2][2]


def ha(i1, i2, a):
    global point_matrix1
    global point_matrix2
    similar_points(i1, i2, a)
    point_matrix1 = np.array(point_matrix1)
    point_matrix2 = np.array(point_matrix2)
    cv2.imwrite("C:/Users/aksha/Desktop/NewImageA.jpg", img)
    cv2.imwrite("C:/Users/aksha/Desktop/NewImageB1.jpg", img2)
    h_graph_n(point_matrix1, point_matrix2)
    new_map(h)


def new_map(h):
    global count_new2
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', mouse_click_new)
    cv2.waitKey(0)
    global point_matrix_new1
    global point_matrix2
    hnp = np.array(h)
    for i in range(len(point_matrix_new1)):
        a_1 = np.array([point_matrix_new1[i][0], point_matrix_new1[i][1], 1])
        point_matrix_temp = (np.matmul(hnp, a_1))
        point_matrix_new2.append(point_matrix_temp/point_matrix_temp[2])
    for po in range(len(point_matrix_new2)):
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img2, str(count_new2 + 1) , (int(point_matrix_new2[po][0]), int(point_matrix_new2[po][1])), font, 1, (90, 255, 0), 2)
        cv2.imshow('image', img2)
        count_new2 += 1
        cv2.waitKey(0)
    cv2.imwrite("C:/Users/aksha/Desktop/NewImage.jpg", img)
    cv2.imwrite("C:/Users/aksha/Desktop/NewImage1.jpg", img2)

ha(img, img2, 1)
cv2.destroyAllWindows()
