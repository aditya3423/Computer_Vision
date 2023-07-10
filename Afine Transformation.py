import cv2 as cv
import numpy as np

#creating new image with two axis crossing the image
def new_im(x, y):
    img = []
    for i in range(int(x)):
        temp = []
        for j in range(int(y)):
            col = []
            for k in range(3):
                if i == int(x/2) or j == int(y/2):
                    col.append(0)
                else:
                    col.append(245)
            temp.append(col)
        img.append(temp)
    img = np.array(img)
    img = img.astype(np.uint8)
    return img

#using this function to place the original image at the centre in a bigger image
def axis(img):
    new_img = new_im(1000, 1000)
    x = np.shape(img)
    l1 = (500 - (x[0] / 2))
    l2 = (500 - (x[1] / 2))
    for a1 in range(len(img)):
        for a2 in range(len(img[0])):
            new_img[a1 + int(l1)][a2 + int(l2)] = img[a1][a2]
    return new_img

#to transpose the image
def transp(img):
    x, y = input("Enter the position you want to move to: ").split()
    x = int(x)
    y = int(y)
    mat = [[x], [y]]
    a = np.shape(img)
    l1 = (500 - (a[0] / 2))
    l2 = (500 - (a[1] / 2))
    aa = axis(img)
    aa = cv.resize(aa, (500, 500))
    cv.imshow("In a 2D plane", aa )
    cv.waitKey(0)
    new_img = new_im(1000, 1000)
    for i in range(len(img)):
        for j in range(len(img[i])):
            new_img[i - y + int(l1)][j + x + int(l2)] = img[i][j]
    new_img = cv.resize(new_img, (500, 500))
    cv.imshow("After Translation", new_img)
    cv.waitKey(0)


#to rotate the image
def rotate1(img):
    ang = float(input("Enter the angle of rotation: "))
    a = np.shape(img)
    l1 = (500 - (a[0] / 2))
    l2 = (500 - (a[1] / 2))
    aa = axis(img)
    aa = cv.resize(aa, (500, 500))
    cv.imshow("In a 2D plane", aa)
    cv.waitKey(0)
    new_img = new_im(1000, 1000)
    matrix2 = [[np.cos(ang), -np.sin(ang), l1],[np.sin(ang), np.cos(ang), l2],[0, 0, 1]]
    matrix2 = np.array(matrix2)
    for x in range(len(img)):
        for y in range(len(img[x])):
            matrix1 = [x, y, 1]
            matrix1 = np.array(matrix1)
            b = np.matmul(matrix2, matrix1)
            new_img[int(b[0])][int(b[1])] = img[x][y]
    new_img = cv.resize(new_img, (500, 500))
    cv.imshow("New", new_img)
    cv.waitKey(0)


#to scale the image
def scale(img):
    cx, cy = input("Enter the scaling factor ").split()
    a = np.shape(img)
    l1 = (500 - (a[0] / 2))
    l2 = (500 - (a[1] / 2))
    aa = axis(img)
    aa = cv.resize(aa, (500, 500))
    cv.imshow("In a 2D plane", aa)
    cv.waitKey(0)
    new_img = new_im(1000, 1000)
    matrix2 = [[float(cx), 0, l1],[0, float(cy), l2],[0, 0, 1]]
    matrix2 = np.array(matrix2)
    for x in range(len(img)):
        for y in range(len(img[x])):
            matrix1 = [x, y, 1]
            matrix1 = np.array(matrix1)
            b = np.matmul(matrix2, matrix1)
            new_img[int(b[0])][int(b[1])] = img[x][y]
    new_img = cv.resize(new_img, (500, 500))
    cv.imshow("New", new_img)
    cv.waitKey(0)


#to shear the image
def shear(img):
    l = int(input("Enter 1 for vertical shear and 2 for horizontal shear"))
    s = input("Enter the shearing factor")
    matrix2 = []
    a = np.shape(img)
    l1 = (500 - (a[0] / 2))
    l2 = (500 - (a[1] / 2))
    aa = axis(img)
    aa = cv.resize(aa, (500, 500))
    cv.imshow("In a 2D plane", aa)
    cv.waitKey(0)
    new_img = new_im(1000, 1000)
    if int(l) == 1:
        matrix2 = [[1, float(s), l1], [0, 1, l2], [0, 0, 1]]
        matrix2 = np.array(matrix2)
    elif int(l) == 2:
        matrix2 = [[0, 1, l1], [float(s), 1, l2], [0, 0, 1]]
        matrix2 = np.array(matrix2)
    for x in range(len(img)):
        for y in range(len(img[x])):
            matrix1 = [x, y, 1]
            matrix1 = np.array(matrix1)
            b = np.matmul(matrix2, matrix1)
            new_img[int(b[0])][int(b[1])] = img[x][y]
    new_img = cv.resize(new_img, (500, 500))
    cv.imshow("New", new_img)
    cv.waitKey(0)


def all():
    val = int(input("Choose the transformation \n1.Transpose\n2.Rotate\n3.Shear\n4.Scale\nEnter the value: "))
    if val == 1:
        transp(cba)
    elif val == 2:
        rotate1(cba)
    elif val == 3:
        shear(cba)
    elif val == 4:
        scale(cba)
    else:
        print("Enter correct value.")


cba = cv.imread("grey.png")
for i in range(4):
    all()





