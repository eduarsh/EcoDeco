import cv2
import Image
import numpy as np

def change_resolution(path, width, height):
    width = width
    height = height
    im1 = Image.open(path)
    image = im1.resize((width, height), Image.ANTIALIAS)
    ext = ".jpg"
    image.save("images/ANTIALIAS" + ext)
    converter_to_P("images/ANTIALIAS.jpg")
    
def image_show(path):
    height = 100
    width = 100
    im1 = Image.open(path)
    image = im1.resize((width, height), Image.ANTIALIAS)
    ext = ".jpg"
    image.save("images/SHOW" + ext)
    converter_to_P("images/SHOW.jpg")

def converter_to_P(path):
    image = cv2.imread(path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path,gray_image)

def image_to_matrix(path):
    
    img = Image.open(path).convert('P')
    mat = np.array(img)   
    return mat

def matrix_to_image(array):
    
    im = Image.fromarray(array)
    im.save('images/output.jpg')