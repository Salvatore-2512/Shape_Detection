import cv as cv 

image = cv.imread("/Users/aryanvasudeva/Desktop/openCV/SCR-20240121-dlhk.png")
# here i am saving the image in variable image
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) 
# here i am Converting to gray image
_, thresh_image = cv.threshold(gray_image, 220, 255, cv.THRESH_BINARY)
#here we makeall colours except white into black
# edge coordiantes
contours, hierarchy = cv.findContours(thresh_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for i, contour in enumerate(contours):
    if i == 0:
        continue
    epsilon = 0.01*cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)

    # Drawing the outer-edges onto the image
    cv.drawContours(image, contour, 0, (0, 0, 0), 4)

    # Retrieving coordinates of the contour so that we can put text over the shape.
    x, y, w, h= cv.boundingRect(approx)
    x_mid = int(x + (w/3)) 
    y_mid = int(y + (h/1.5))
    
    # Setting some variables which will be used to display text on the final image
    coords = (x_mid, y_mid)
    colour = (0, 0, 0)
    font = cv.FONT_HERSHEY_DUPLEX

   
    if len(approx) == 3:
        cv.putText(image, "Triangle", coords, font, 1, colour, 1) # Text on the image
    elif len(approx) == 4:
        cv.putText(image, "Square", coords, font, 1, colour, 1)
    elif len(approx) == 5:
        cv.putText(image, "Pentagon", coords, font, 1, colour, 1)
    else:
        cv.putText(image, "Hexagon", coords, font, 1, colour, 1)
    
cv.imshow("shapes_detected", image)
cv.waitKey(0)