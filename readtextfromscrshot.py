import pyautogui
from pynput import mouse
import time
import os

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pos = ()
ifpressed = False

def on_click(x, y, button, pressed):
    global pos
    global ifpressed
    if button == mouse.Button.left:
        # print('{} at {}'.format('Pressed Left Click' if pressed else 'Released Left Click', (x, y)))
        pos = (x, y)
        ifpressed = pressed

        # return False # Returning False if you need to stop the program when Left clicked.
    # else:
        
        # print('{} at {}'.format('Pressed Right Click' if pressed else 'Released Right Click', (x, y)))


listener = mouse.Listener(on_click=on_click)
listener.start()




# print('pos')

# Mouse first click and record coordinate
while 1:
    if ifpressed == True:
        print(pos)
        pos1st = pos
        ifpressed = False
        break
# Mouse click for second time and record coordinate
while 1:
    if ifpressed == True:
        print(pos)
        pos2nd = pos
        ifpressed = False
        break
print(pos2nd[0] - pos1st[0])
print(pos2nd[1] - pos1st[1])

scrn_reg = pos1st + ((pos2nd[0] - pos1st[0]), ) + ((pos2nd[1] - pos1st[1]), )
print(scrn_reg)

# Take screenshot
# left, top, width, and height
im = pyautogui.screenshot('output.jpg', region = scrn_reg)

# Save to file

# Read text drom image
img = cv2.imread('output.jpg')

text = pytesseract.image_to_string(img)
print(text)

# # Delete the image
os.remove('output.jpg')


