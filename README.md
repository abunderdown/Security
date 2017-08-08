''' 
Adam Underdown, 2017
made in python 3, OpenCv 2 is a dependency

This program uses CV2 to run the computer's webcam and detect motion that moves past the camera.
This runs forever, creating 1 video each hour, with each video containing only the movement recorded in that hour,
all other video is ignored. The time of the movement is recorded on the videos.

press q to create a new video, otherwise, another one will be created when the hour is over.
The only way to fully exit the program is through the task manager, or stop it in the command prompt on Linux.

'''
