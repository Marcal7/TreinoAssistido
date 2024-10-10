import cv2

# Initialize MediaPipe
#

# Create a video capture object
cap = cv2.VideoCapture(0)

#with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
while True:
    success, image = cap.read()

    # Convert the image to RGBand process it

    # Convert the image back to BGR and draw results

    cv2.imshow('MediaPipe Pose', image)

    # Release resources
cap.release()
cv2.destroyAllWindows()