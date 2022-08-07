import cv2 as cv

img = cv.imread('Fotos/IMG_20220307_223504.jpg')

# cv.imshow('Ariel', img)

def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Redimensionada', resized_image)

# Convertir a escala de grises
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('Escala de grises', gray)

# Blur (eliminar ruido, problemas con el sensor de la imagen)
blur = cv.GaussianBlur(resized_image, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Borde
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Dilatar la imagen
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Erosionar
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resize = cv.resize(resized_image, (500,500))
cv.imshow('Resized', resize)

# Cropping
cropped = resized_image[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)