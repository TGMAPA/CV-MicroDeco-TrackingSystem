# Camera model

import cv2, os

class Camera:
    def __init__(self, source = 0):
        if type(source) == str: assert os.path.exists(source), "File not found " + source; 
        self.videoSourceCapture = cv2.VideoCapture(source)

    def getFrame(self):
        return self.videoSourceCapture.read()
    
    def kill(self):
        self.videoSourceCapture.release()

