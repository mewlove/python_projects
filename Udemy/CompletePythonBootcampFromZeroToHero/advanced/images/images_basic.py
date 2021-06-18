# (control + '/' for comments)

# pip install pillow
# official documentation in pillow.readthedocs.io

import os, sys
os.chdir(os.path.abspath(os.path.dirname(sys.argv[0]))) #CHANGE DIR TO THE SAME DIRECTORY AS THIS FILE


from PIL import Image
blue_color_png = 'blue_color.png'
example_jpg = 'example.jpg'
mask_png = 'mask.png'
pencils_jpg = 'pencils.jpg'
purple_png = 'purple.png'
red_color_jpg = 'red_color.jpg'
word_matrix_png = 'word_matrix.png'

#####################################################
# UNCOMMENT TO SEE IMAGE OF mac - GET IMAGE DETAILS
#####################################################
mac = Image.open(example_jpg)
# mac.show() #OPENS A BROWSER TO SEE THE IMAGE
# print(f"Size of image: {mac.size}")
# print(f"Format of image: {mac.format}")



#####################################################
# UNCOMMENT TO SEE IMAGE OF pencils  - CROP
#####################################################
pencils = Image.open(pencils_jpg)
# pencils.show() # OPENS A BROWSER TO SEE THE IMAGE
# print(pencils.size)

# TOP LEFT PENCILS
top_left_x = 0
top_left_y = 0
bottom_right_x = 0.3*pencils.size[0]    # 30% of the width
bottom_right_y = 0.1*pencils.size[1]    # 10% of the height

cropped_pencils = pencils.crop((top_left_x,top_left_y,bottom_right_x,bottom_right_y)) #type: ignore
# cropped_pencils.show() # OPENS A BROWSER TO SEE THE IMAGE
# print(cropped_pencils.size)


# BOTTOM LEFT PENCILS
top_left_x = 0
top_left_y = 0.8*pencils.size[1]        # 80% of the height
bottom_right_x = 0.3*pencils.size[0]    # 30% of the width
bottom_right_y = top_left_y + 0.2*pencils.size[1]    # 20% of the height

cropped_pencils = pencils.crop((top_left_x,top_left_y,bottom_right_x,bottom_right_y)) #type: ignore
# cropped_pencils.show() # OPENS A BROWSER TO SEE THE IMAGE
# print(cropped_pencils.size)


#####################################################
# COPY AND PASTE IMAGE
#####################################################
coord_to_paste = (800,0)
pencils.paste(im = cropped_pencils, box=coord_to_paste)
#pencils.show() # OPENS A BROWSER TO SEE THE IMAGE



#####################################################
# RESIZE IMAGE
#####################################################
resize_to = (3000,500)
pencils = pencils.resize(resize_to)
#pencils.show() # OPENS A BROWSER TO SEE THE IMAGE



#####################################################
# ALPHA AND TRANSPARENCY
#####################################################
red_color = Image.open(red_color_jpg)
blue_color = Image.open(blue_color_png)

red_color.putalpha(128)
red_color.show()

blue_color.putalpha(128)
blue_color.show()
print(blue_color.size)

#mix colors
blue_color.paste(im = red_color,box = (100,100),mask=red_color)
blue_color.show()

blue_color.save('mix_color.png')   #WARNING THIS OVERWRITES ANY FILE CALLED mix_color.png