import cv2 as cv

img = cv.imread('TestPhoto.jpg')

blur = cv.GaussianBlur(img, (5,5), 0)

cv.imshow("Blur", blur)

edges = cv.Canny(img, 100, 200)

cv.imshow("Edges", edges)