import numpy as np
import time
import cv2
import aruco_dict
from arm_movement import goto_box
ARUCO_DICT = aruco_dict.ARUCO_DICT


def arm_translation(corners, ids, image):
	x=y=0
	arm_id = 3
	box_id = 4
	box = [0,0]
	arm = [0,0]
	offset = [20,10]

	if len(corners) > 0:

		ids = ids.flatten()
		
		for (markerCorner, markerID) in zip(corners, ids):

			if markerID == arm_id:
				corners = markerCorner.reshape((4, 2))
				(topLeft, topRight, bottomRight, bottomLeft) = corners
				
				cX = int((topLeft[0] + bottomRight[0]) / 2.0)
				cY = int((topLeft[1] + bottomRight[1]) / 2.0)
				cv2.circle(image, (cX, cY), 10, (145, 105, 25), -1)
				arm[0] = cX
				arm[1] = cY
				# print('arm: ', arm)
			
			elif(markerID == box_id):
				corners = markerCorner.reshape((4, 2))
				(topLeft, topRight, bottomRight, bottomLeft) = corners
				
				cX = int((topLeft[0] + bottomRight[0]) / 2.0)
				cY = int((topLeft[1] + bottomRight[1]) / 2.0)
				cv2.circle(image, (cX, cY), 10, (145, 105, 25), -1)
				box[0] = cX
				box[1] = cY
				# print('box: ', box)
			else:
				pass


		# if arm and box are at the same position return or any one of them is not detected return [0,0]
		if (box[0] == arm[0] and box[1] == arm[1]) or (box == [0,0] or arm == [0,0]):
			return [0,0]
		else:
			x = box[0]-arm[0]+offset[0]
			y = arm[1]-box[1]+offset[1]
			print('x: ', x, 'y: ', y)
			cv2.line(image, box, arm, (145, 105, 25), 2)
			cv2.circle(image, (int(box[0]+offset[0]), int(box[1])+offset[1]), 4, (200, 20, 205), -1)
		print(goto_box(x, y))
		return [x,y]


def aruco_display(corners, ids, rejected, image):
	if len(corners) > 0:
		
		ids = ids.flatten()
		
		for (markerCorner, markerID) in zip(corners, ids):
			
			corners = markerCorner.reshape((4, 2))
			(topLeft, topRight, bottomRight, bottomLeft) = corners
			
			topRight = (int(topRight[0]), int(topRight[1]))
			bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
			bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
			topLeft = (int(topLeft[0]), int(topLeft[1]))

			cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
			cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
			cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
			cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
			
			cX = int((topLeft[0] + bottomRight[0]) / 2.0)
			cY = int((topLeft[1] + bottomRight[1]) / 2.0)
			cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)
			
			cv2.putText(image, str(markerID),(topLeft[0], topLeft[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (0, 255, 0), 2)
			# print("[Inference] ArUco marker ID: {}".format(markerID))
			
	return image




aruco_type = "DICT_4X4_1000"

arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[aruco_type])

arucoParams = cv2.aruco.DetectorParameters()
# print(arucoParams)


cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


while cap.isOpened():
	
	ret, img = cap.read()
	h, w, _ = img.shape

	width = 1000
	height = int(width*(h/w))
	img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)

	detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams)
	corners, ids, rejected = detector.detectMarkers(img)

	detected_markers = aruco_display(corners, ids, rejected, img)
	arm_translation(corners, ids, detected_markers)
	cv2.imshow("Image", detected_markers)

	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

cv2.destroyAllWindows()
cap.release()