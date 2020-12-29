import cv2
import numpy as np 

class Visioner:
    def __init__(self,image_path):
        self.image = cv2.imread(image_path)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

    def findred(self):
        ## Gen lower mask (0-5) and upper mask (175-180) of RED
        mask1 = cv2.inRange(self.image, (0,50,20), (5,255,255))
        mask2 = cv2.inRange(self.image, (175,50,20), (180,255,255))

        ## Merge the mask and crop the red regions
        mask = cv2.bitwise_or(mask1, mask2 )
        return mask

    def saveImage(self,img_to_save,path):
        img_to_save = np.asarray(img_to_save)
        cv2.imwrite(path,img_to_save) 
        




    

