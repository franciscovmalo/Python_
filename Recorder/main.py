from win32api import GetSystemMetrics
from PIL import ImageGrab
import numpy as np
import datetime
import cv2


widith = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(f'Screenvideo/{file_name}', fourcc, 20.0, (widith, height))
cam = cv2.VideoCapture(0)

def Capture():
    while True:
        img = ImageGrab.grab(bbox=(0, 0, widith, height))
        img_np = np.array(img)
        img_fin = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        if cv2.waitKey(10) == ord ('c'):
            _, frame = cam.read()
            fr_height, fr_widith, _ = frame.shape
            img_fin[0: fr_height, 0: fr_widith, :] = frame[0: fr_height, 0: fr_widith :]
        
        cv2.imshow('Screen Recorder', img_fin)
        captured_video.write(img_fin)
        
        if cv2.waitKey(10) == ord('q'):
            break

Capture()