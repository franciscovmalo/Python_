from win32api import GetSystemMetrics
from PIL import ImageGrab
import tkinter as tk
import numpy as np
import datetime
import cv2
import sys


widith = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
ifile_name = f'{time_stamp}.png'

def Shot():
    
    img = ImageGrab.grab(bbox=(0, 0, widith, height))
    img_np = np.array(img)
    img_fin = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cpim =cv2.imwrite(f'Screenshot/{ifile_name}', img_fin)


def Capture():

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    captured_video = cv2.VideoWriter(f'Screenvideo/{file_name}', fourcc, 20.0, (widith, height))
    cam = cv2.VideoCapture(0)
    
    while True:
        img = ImageGrab.grab(bbox=(0, 0, widith, height))
        img_np = np.array(img)
        img_fin = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        if cv2.waitKey(10) == ord ('c'):
            _, frame = cam.read()
            fr_height, fr_widith, _ = frame.shape
            img_fin[0: fr_height, 0: fr_widith, :] = frame[0: fr_height, 0: fr_widith :]
        
        if cv2.waitKey() == ord('q'):
            Close()
            

        cv2.imshow('Screen Recorder', img_fin)
        captured_video.write(img_fin)
        
        
def Close():
    sys.exit("QUIT")

def Write():
    print("Until Its Done!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

#label = tk.Label(root, text='Hello World!')
#label.pack (padx=20, pady=20)

slogan = tk.Button(frame, text="Screenshot", command=Shot)
slogan.pack(padx=3, pady=1, side=tk.RIGHT)
cap = tk.Button(frame, text="Capture", command=Capture)
cap.pack(padx=3, pady=1, side=tk.LEFT)
button = tk.Button(frame, text="Quit", fg="red", command=quit)
button.pack(padx=3, pady=1, side=tk.LEFT)

root.mainloop()