import cv2 as cv

# Read image

path=input("Give image path : ")

new_size=int(input("Enter the size to be reduced (in percentage): "))
new_size= new_size/100

img = cv.imread(path)
cv.imshow('Real Image', img)

#grayscaling

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Resizing

def Resize(frame, size):
    
    width=int(frame.shape[1]*size)
    height=int(frame.shape[0]*size)

    dimentions=(width,height)

    return cv.resize(frame, dimentions,interpolation=cv.INTER_AREA)

newimg = Resize(gray,new_size)

cv.imshow('New Image', newimg)
cv.waitKey(0)

cv.destroyAllWindows()
