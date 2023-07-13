from win32api import GetSystemMetrics
from PIL import ImageGrab
import numpy as np
import cv2
import datetime

widith = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.png'

img = ImageGrab.grab(bbox=(0, 0, widith, height))
img_np = np.array(img)
img_fin = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
cpim =cv2.imwrite(f'Screenshot/{file_name}', img_fin)
