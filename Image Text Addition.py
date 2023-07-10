import cv2 as cv
import numpy as np


#Placement of text at some positions
def txtt(img):
    txt = input("Enter the text you want to enter- ")
    coo = (0, 0)
    shap = np.shape(img)
    pos = int(input("Enter the position you want to place it\n1.Top-Left\t     2.Top\t    3.Top-Right"
                    "\n4.Middle_left\t 5.Centre\t6. Middle-Right\n7.Bottom-Left\t 8.Bottom\t9. Bottom-Right --- "))
    if int(pos) == 1:
        coo = (0, 25)
    elif pos == 2:
        coo = (int(shap[1] / 2) - len(txt) * 8, 25)
    elif pos == 3:
        coo = (int(shap[1])-len(txt)*20, 25)
    elif pos == 4:
        coo = (0, int(shap[0] / 2))
    elif pos == 5:
        coo = (int(shap[1] / 2) - len(txt) * 8, int(shap[0] / 2))
    elif pos == 6:
        coo = (int(shap[1]/2), (int(shap[0]/2)+20))
    elif pos == 7:
        coo = (0, shap[0] - 10)
    elif pos == 8:
        coo = (int(shap[1] / 2) - len(txt) * 8, int(shap[0]) - 10)
    elif pos == 9:
        coo = (int(shap[1]/2), int(shap[0])-10)
    cv.putText(img=img, text = txt , org=coo, fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(45, 26, 239), thickness=3)


#creating new image to add text
def creat_newimg(old_img):
    new_img = []
    x = np.shape(old_img)
    for i in range(x[0]):
        temp = []
        for j in range(x[1]):
            col = []
            for k in range(x[2]):
                col.append(220)
            temp.append(col)
        new_img.append(temp)

    new_img = np.array(new_img)
    new_img = new_img.astype(np.uint8)
    return new_img


#From new Image generated, place the text in the original image
def add_text_man(old_img, new_img):
    txtt(new_img)
    x = np.shape(old_img)
    for a in range(x[0]):
        for b in range(x[1]):
            if new_img[a][b][2] == 239:
                old_img[a][b] = new_img[a][b]
    cv.imshow("After Text Addition", old_img)
    cv.waitKey(0)

cba = cv.imread("grey.png")
new_img = creat_newimg(cba)
add_text_man(cba, new_img)
