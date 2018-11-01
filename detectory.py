import cv2
import sys


def variance_of_laplacian(image):
    # compute the variance of laplacian of the image
    return cv2.Laplacian(image, cv2.CV_64F).var()

def main(file):
    # load the image
    image = cv2.imread(file)

    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # calculate the variance of laplacian of the grayscale image
    thres = variance_of_laplacian(gray)

    # set the threshold to 100
    # if the threshold is less than 100 the image is blurry
    if thres < 100:
        return 1

    # good image
    else:
        return 0

file = sys.argv[1]

if __name__ == '__main__':
    main(file)