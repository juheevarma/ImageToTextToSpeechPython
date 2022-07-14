# 1. Install the following packages
# pip install pytesseract
# pip install pyautogui
# pip install pillow
# pip install numpy
# pip install pyttsx3
# [text to speech conversion library]
# pip install gTTS
# pip install playsound

# 2. Import Python for GUI Automation
import pyautogui

# 3. Extract the image from Python Imaging Library
# PIL enables opening and manipulating of image in different image formats
from PIL import Image

# 4. To convert text to speech, import commands from pyttsx3
from pytesseract import *
import pyttsx3

# 5. Use Google-Text-To-Speech for output audio
import gtts
from playsound import playsound

# 6. For manipulation using arrays, numpy is used
import numpy as np

# 7. Use tesseract.exe extention for path of installed tesseract 
pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 8. Extraction image and store in a variable
# Ensure that the image and Python file are in the same folder
filename = 'sample1.png' 
img1 = np.array(Image.open(filename))

# 9. Convert image to string
text = pytesseract.image_to_string(img1)

# 10. Display text
print(text)

# 11. Convert text to speech 
t = gtts.gTTS(text)
t.save("audio.mp3")

# 12. Audible output speech for input text
playsound("audio.mp3")