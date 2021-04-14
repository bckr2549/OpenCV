import cv2
img = cv2.imread('photoes/cat.jpg')
cv2.imshow('Cat', img)

def rescaleFrame(frame, scale=0.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
resized_image = rescaleFrame(img)
cv2.imshow('Image', resized_image)
capture = cv2.VideoCapture('vedious/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = 0.40)
    cv2.imshow('Vedio',frame)
    cv2.imshow('vedio Resized', frame_resized)

    if cv2.waitKey(40) & 0xFF == ord('d'):
        break
capture.release()
cv2.destroyAllWindows()