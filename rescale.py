import cv2 as cv

img = cv.imread('Fotos/IMG_20220307_223504.jpg')
cv.imshow('Ariel', img)

def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Redimensionada', resized_image)

cv.waitKey(0)