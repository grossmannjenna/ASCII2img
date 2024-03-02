from PIL import Image, ImageOps

imageFile = input("Please enter the exact path to an image file: ")
im = Image.open(imageFile)

fileName = imageFile.split("/")[-1]
# fileName[-1] should be fileName
fileName = fileName.split(".")[0] 

x_dimension, y_dimension = im.size[0], im.size[1]

x, y = 0, 0

print("\n", "File Name: ", fileName, "\n", "Format: ", im.format, "\n Len: ", x_dimension, "px  Wid: ", y_dimension, "px\n") 

im = ImageOps.grayscale(im)

pixels = im.load()

print("Pixel at (1, 1): ", pixels[x, y])
