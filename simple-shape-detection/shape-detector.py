from typing import Counter
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

image_url = 'shapes.jpg'
img =  cv2.imread(image_url)

# converting image to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thrash = cv2.threshold(grayscaled_img, 220, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    poly_dp = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [poly_dp], 0, (0, 255, 0), 3)
    x = poly_dp.ravel()[0] 
    y = poly_dp.ravel()[1] + 2
    if len(poly_dp) == 3:
        cv2.putText(img, 'Triangle', (x, y), font, 0.5, (255,0,0))
    elif len(poly_dp) == 4:
        _x, _y, w, h =  cv2.boundingRect(poly_dp)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if 0.9 < aspectRatio < 1.1:
            cv2.putText(img, 'Sqaure', (_x, _y), font, 0.5, (255,0,0))
        else:
            cv2.putText(img, 'Rectangle', (_x, _y), font, 0.5, (255,0,0))
    elif len(poly_dp) == 5:
        cv2.putText(img, 'Pentagon', (x, y), font, 0.5, (255,0,0))
    elif len(poly_dp) == 6:
        cv2.putText(img, 'Hexagon', (x, y), font, 0.5, (255,0,0))
    else:
        _x, _y, w, h =  cv2.boundingRect(poly_dp)
        aspectRatio = float(w)/h
        if 0.9 < aspectRatio < 1.1:
            cv2.putText(img, 'Circle', (x, y), font, 0.5, (255,0,0))
        else:
            cv2.putText(img, 'Oval', (x, y), font, 0.5, (255,0,0))

# show image
cv2.imshow('image: ', img)
cv2.waitKey()

print('\nCode completed\n')