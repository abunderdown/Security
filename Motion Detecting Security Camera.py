''' 
Adam Underdown, 2017
made in python 3, OpenCv 2 is a dependency

This program uses CV2 to run the computer's webcam and detect motion that moves past the camera.
This runs forever, creating 1 video each hour, with each video containing only the movement recorded in that hour,
all other video is ignored. The time of the movement is recorded on the videos.

press q to create a new video, otherwise, another one will be created when the hour is over.
The only way to fully exit the program is through the task manager, or stop it in the command prompt on Linux.

'''

import cv2, time

prev_frame=None
movement=False
font = cv2.FONT_HERSHEY_SIMPLEX
#video=cv2.VideoCapture(0)
while True:
	video=cv2.VideoCapture(0)
	fname=time.strftime("%Y-%m-%d-%H-%M-%S")
	hour=time.strftime("%H")
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter(fname+".avi",
		fourcc, 
		60.0, 
		(6400,480))

	while True:
		check, frame=video.read()
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		gray=cv2.GaussianBlur(gray,(21,21),0)
		
		if prev_frame is not None:
			delta_frame=cv2.absdiff(prev_frame,gray)
			thresh_frame=cv2.threshold(delta_frame, 30,255,cv2.THRESH_BINARY)[1]
			thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)

			(_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

			for contour in cnts:
				
				if cv2.contourArea(contour)<100:
					movement=False
					continue
				
				movement=True
				cv2.putText(frame,
					time.strftime("%Y-%m-%d-%H-%M-%S"),
					(10,450), 
					font,
					1,
					(0,255,0),
					2,
					cv2.LINE_AA)
				out.write(frame)


		#cv2.imshow("Capturing",frame)
		key=cv2.waitKey(1)
		
		prev_frame=gray
		if key==ord("q"):
			break

		if time.strftime("%H")!=hour:
			break

	video.release()
	out.release()
	cv2.destroyAllWindows()