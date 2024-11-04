import numpy as np
import traceback
import pyautogui
import mss
import cv2


pyautogui.FAILSAFE = False
  
  
class Recorder():
    def __init__(self):
        self.monitor = {"left": 0, "top": 0, "width": 1920, "height": 1080}
        
    def capture(self):
        try:
            if self.monitor:
                with mss.mss() as sct:
                    screen = sct.grab(self.monitor)
                    image = np.array(screen)
                    image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
                    return image
                
        except:
            traceback.print_exc()