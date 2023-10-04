from PIL import Image 
from gtts import gTTS
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\SHREE\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
def image_to_sound(image):   
    try:
        open_image = Image.open(image)
        text = pytesseract.image_to_string(open_image)
        text_file = " ".join(text.split("\n"))
        print(text_file)
        sound = gTTS(text_file,lang="en")
        sound.save("sound.mp3")
        os.system("sound.mp3")
        return True
    except Exception as bug:
        print("The error while executing the code\n",bug)
        return
if __name__ == "__main__":
    image_to_sound("attitude.png")
    input()
    