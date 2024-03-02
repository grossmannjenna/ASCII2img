from PIL import Image, ImageOps, ImageDraw, ImageFont

chars = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]

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

    asciiStr = ""

    scaleFac = float(input("Enter the scaling factor (as num): "))

    im = im.resize((int(x_dimension / scaleFac), int(y_dimension / scaleFac)),resample=Image.LANCZOS)
    x_dimension, y_dimension = im.size[0], im.size[1]

    for i in range(0, y_dimension):
        asciiStr += "\n"
        for j in range(0, x_dimension):
            #im.putpixel((i,j), 0)
            asciiStr += str(getCharFromPixel(im.getpixel((j,i)))) 

    print(asciiStr)


def getCharFromPixel(p):
    if (p < 25):
        return chars[0]
    elif (p < 51):
        return chars[1]
    elif (p < 76):
        return chars[2]
    elif (p < 102):
        return chars[3]
    elif (p < 127):
        return chars[4]
    elif (p < 153):
        return chars[5]
    elif (p < 178):
        return chars[6]
    elif (p < 204):
        return chars[7]
    elif (p < 229):
        return chars[8]
    elif (p <= 255):
        return chars[9]


#actually run it this time you dork
main()



