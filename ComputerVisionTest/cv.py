import cv2
import os
import numpy


# A class that takes in a path of an image and turns it into a Contoured image
class ContourImage:
    def __init__(self, path:str, threshold:float = 0.15) -> None:
        self.img = cv2.imread(path)
        self.col_len = len(self.img)
        self.row_len = 0 if not self.col_len else len(self.img[0])
        self.threshold = threshold

        self.__grayscale = [[0.0 for _ in col] for col in self.img]
        self.__smooth = [[0.0 for _ in col] for col in self.img]
        self.__gradient_threshold = [[0.0 for _ in col] for col in self.img]

        self.__grayscale_func()
        self.__smoothing_func()
        self.__gradient_threshold_func()
        self.__overlay_func()

    #grayscale
    def __grayscale_func(self):
        for x, col in enumerate(self.img):
            for y, pixel in enumerate(col):
                grayscale = (pixel[0]/3.0 + pixel[1]/3.0 + pixel[2]/3.0)
                self.__grayscale[x][y] = grayscale

    #SMOOTH
    def __smoothing_func(self):
        for x , col in enumerate(self.img):
            for y, _ in enumerate(col):
                average = self.__grayscale[x][y]
                if x > 0 and y > 0 and self.col_len-1> x and self.row_len-1>y:
                    average = 0
                    average += ( self.__grayscale[x-1][y-1] + self.__grayscale[x-1][y] + self.__grayscale[x-1][y+1] \
                                + self.__grayscale[x][y-1] + self.__grayscale[x][y] + self.__grayscale[x][y+1] \
                                + self.__grayscale[x+1][y-1] + self.__grayscale[x+1][y]+ self.__grayscale[x+1][y+1])
                self.__smooth[x][y] = average/9.0

    def __gradient_threshold_func(self):
        min_value = 255
        max_value = 0
        for x , col in enumerate(self.__smooth):
            for y, _ in enumerate(col):
                sum = min_value
                if self.col_len-1> x and self.row_len-1> y:
                    sum = (abs(self.__smooth[x+1][y] - self.__smooth[x-1][y]) \
                            +abs(self.__smooth[x][y+1] - self.__smooth[x][y]))
                min_value = min(min_value, sum)
                max_value = max(max_value, sum)
                self.__gradient_threshold[x][y] = sum
        threshold_value = self.threshold*max_value + (1-self.threshold)*min_value

        for x , col in enumerate(self.__gradient_threshold):
            for y, pixel in enumerate(col):
                self.__gradient_threshold[x][y] = 0 if pixel < threshold_value else 255

    def __overlay_func(self):
        for x , col in enumerate(self.img):
            for y, pixel in enumerate(col):
                if self.__gradient_threshold[x][y] == 255:
                    pixel[0] = 0
                    pixel[1] = 255
                    pixel[2] = 0

    def show_image(self, title:str=""):
        cv2.imshow(title,self.img)
        
    def save_image(self, path:str):
        try:
            cv2.imwrite(path, self.img)
            print("Image saved!")
        except:
            print("Error. Please try again")



def open_image_user_input():
    while(True):
        try:
            image_path = str(input("Please input image path: "))
            os.path.exists(image_path)
        except:
            print("File/path not found. Please try again.")
        else:
            return image_path

def save_image_user_input():
    while(True):
        try:
            image_path = str(input("Please input new image path: "))
        except:
            print("Invalid input. Please try again.")
        else:
            return image_path

def enter_threshold():
    while(True):
        try:
            threshold = float(input(f"(Default threshold: 0.15) Please input threshold [0-1]: "))
        except:
            print("Using threshold = 0.15")
            return 0.15
        else:
            return threshold

def enter_action():
    while(True):
        try:
            print("- Actions -")
            print("0: Process new image")
            print("1: Save new image")
            print("2: Exit")
            action_index = int(input(f"Select Action (0/1/2): "))
        except:
            print("Invalid input. Please try again.")
        else:
            if(action_index<0 or action_index>2):
                print("Invalid input. Please try again.")
                break
            else:
                return action_index 

def run_program():
    print("************** Start Contour Program **************")
    action = 0
    img = None
    while action != 2:
        action = enter_action()
        if action == 2:
            break
        elif action == 0:
            image_path = open_image_user_input()
            user_threshold = enter_threshold()
            img = ContourImage(image_path, user_threshold)
            img.show_image("contour")
            cv2.waitKey(0)
        elif action == 1:
            if img is None:
                print("No image processed. Please try again.\n")
                continue
            else:
                new_image_path = save_image_user_input()
                img.save_image(new_image_path)


run_program()
_ = input('Press any key...')