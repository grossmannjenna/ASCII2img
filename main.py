from PIL import Image, ImageOps

chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']


def main():

      #read in and open image source file 
    imageFile = input("Please enter the exact path to an image file: ")
    im = Image.open(imageFile)

    #break up image path into an array and store image file name
    fileName = imageFile.split("/")[-1]
    #take off image type 
    fileName = fileName.split(".")[0] 

    #set image size
    x_dimension, y_dimension = im.size[0], im.size[1]
        #convert to grayscale
    im = ImageOps.grayscale(im)


    im.save("test.jpg")
    x, y = 21, y_dimension - 42

    print("\n", "File Name: ", fileName, "\n", "Format: ", im.format, "\n Width: ", x_dimension, "px  Height: ", y_dimension, "px\n") 

    im = ImageOps.grayscale(im)

    im.save("test.jpg")

    print("Pixel: ", im.getpixel((x, y)))

    asciiStr = ""

    for i in range(0, x_dimension):
        for j in range(0, y_dimension):
            #im.putpixel((i,j), 0)
            asciiStr += getCharFromPixel(im.getpixel((i,j)))    

    im.save("cursed.jpg")

def getCharFromPixel(p):
    
    return 'a'
