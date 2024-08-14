
from PIL import Image
import numpy as np
import os

# CANNOT DO REFLECTION ABT X AXIS WITH THIS METHOD

def get_image_path(tree,directory,img):
    location = os.path.join(tree,directory)
    final_path = os.path.join(location,img)
    return final_path

def transform(tree='/home/vai',img='duck.jpg', directory='Downloads',transform='reflection_x'):
    path = get_image_path(tree, directory,img)
    img = Image.open(path)
    new_pixel_array = do_transform(img , transform)
    new_img = Image.fromarray(new_pixel_array)
    new_img.show()

def do_transform(img ,transform):
    if transform == 'reflection_x':
        transform_matrix = np.array([[1,0],[0,-1]])
    elif transform == 'reflection_y':
        transform_matrix = np.array([[-1,0],[0,1]])
    elif transform == 'reflection_o':
        transform_matrix = np.array([[-1,0],[0,-1]])
    elif transform == 'horizontal_exp':
        transform_matrix = np.array([[0.5,0],[0,1]])
    elif transform == 'horizontal_cont':
        transform_matrix = np.array([[2,0],[0,1]])
    elif transform == 'horizontal_shear':
        transform_matrix = np.array([[1,0],[1.2,1]])

    width, height = img.size
    RGB_size = 3
    new_pixel_array = np.zeros((height,width,RGB_size),dtype=np.uint8) # should be 3 D matrix (height, width, 3)
    for y in range(0,height):
        for x in range(0, width):
            vector = np.array([[x],[y]])
            pixel_val = img.getpixel((x,y))
            transformed_coord = np.dot(transform_matrix,vector)
            try:
                new_pixel_array[y][x] = img.getpixel((transformed_coord[0],transformed_coord[1]))
            except IndexError:
                break
    return new_pixel_array


#transform(transform='reflection_x')
#transform(transform='reflection_y')
#transform(transform='reflection_o')
transform(transform='horizontal_shear')

