from PIL import Image, ImageOps

chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

#read in and open image source file 
imageFile = input("Please enter the exact path to an image file: ")
im = Image.open(imageFile)

#break up image path into an array and store image file name
fileName = imageFile.split("/")[-1]
#take off image type 
fileName = fileName.split(".")[0] 

#set image size
x_dimension, y_dimension = im.size[0], im.size[1]

x, y = 21, y_dimension - 42


print("\n", "File Name: ", fileName, "\n", "Format: ", im.format, "\n Width: ", x_dimension, "px  Height: ", y_dimension, "px\n") 

#convert to grayscale
im = ImageOps.grayscale(im)


im.save("test.jpg")

print("Pixel at (1, 1): ", im.getpixel((x, y)))

asciiStr = ""

for i in range(0, x_dimension):
    im.putpixel((x,y), (0))
for i in range(0, y_dimension):
    im.putpixel((x,y), (0))

im.save("cursed.jpg")
