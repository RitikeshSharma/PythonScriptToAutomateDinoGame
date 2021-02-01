import pyautogui
from PIL import Image, ImageGrab
#from numpy import asarray
import time

def hit(key):
    pyautogui.press(key)
    return

def isCollide(data):
    #checking for birds
    for i in range(200,270):
        for j in range(340, 395):
            if data[i,j] > 90:
                hit ("down")
                return 
    #checking for cactus
    for i in range(200,270):
        for j in range(395, 460):
            if data[i,j] > 90:
                hit("up")
                return
    return 

if __name__ == "__main__":
    print('Game is about to start in 3 seconds....')
    time.sleep(3)

    hit("up")
    
    while True:
        image = ImageGrab.grab().convert('L')           #convert('L') converts the image into greyscale
        data = image.load()   

        isCollide(data)
            

        #print(asarray(image))               #converts the image in array

        #draw the rectangle for birds

        # for i in range(200,270):
        #     for j in range(340, 395):
        #         data[i,j] = 90
        
        # #draw the rectangle for cactus
        # for i in range(200,270):
        #     for j in range(395, 460):
        #         data[i,j] = 0

        
        
        # image.show()
        # break


