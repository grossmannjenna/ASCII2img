from PIL import Image

imageFile = input("Please enter the exact path to an image file: ")
im = Image.open(imageFile)

print(im.format, "\n Len: ", im.size[0], "px  Wid: ", im.size[1], "px\n") 
