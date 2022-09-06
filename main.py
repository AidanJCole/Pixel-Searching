from cv2 import imread
import cv2
import numpy

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img = imread("img.png", cv2.IMREAD_UNCHANGED)
    copy = img.copy()
    color = (78, 97, 102)
    for x in range(len(img)):
        for y in range(len(img[0])):
            tmp = tuple(img[x][y])
            if tmp == color:
                print(x, y)
                copy[x][y][0] = 0
                copy[x][y][1] = 0
                copy[x][y][2] = 255
    cv2.imwrite("copy.png", copy)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
