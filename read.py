import cv2 as cv

img = cv.imread('Fotos/IMG_20220307_223504.jpg')
cv.imshow('Ariel', img)

cv.waitKey(0)