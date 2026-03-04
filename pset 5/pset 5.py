from PIL import Image , ImageFont , ImageDraw
import numpy 



def make_matrix(color):
    """
    Generates a transformation matrix for the specified color.
    Inputs:
        color: string with exactly one of the following values:
               'red', 'blue', 'green', or 'none'
    Returns:
        matrix: a transformation matrix corresponding to
                deficiency in that color
    """
    # You do not need to understand exactly how this function works.
    if color == 'red':
        c = [[.567, .433, 0], [.558, .442, 0], [0, .242, .758]]
    elif color == 'green':
        c = [[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.142, 0.858]]
    elif color == 'blue':
        c = [[.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, .525]]
    elif color == 'none':
        c = [[1, 0., 0], [0, 1, 0.], [0, 0., 1]]
    return c


def matrix_multiply(m1, m2):
    """
    Multiplies the input matrices.
    Inputs:
        m1,m2: the input matrices
    Returns:
        result: matrix product of m1 and m2
        in a list of floats
    """

    product = numpy.matmul(m1, m2)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result


def img_to_pix(filename):
    """
    Takes a filename (must be inputted as a string
    with proper file attachment ex: .jpg, .png)
    and converts to a list of representing pixels.

    For RGB images, each pixel is a tuple containing (R,G,B) values.
    For BW images, each pixel is an integer.

    # Note: Don't worry about determining if an image is RGB or BW.
            The PIL library functions you use will return the 
            correct pixel values for either image mode.

    Returns the list of pixels.

    Inputs:
        filename: string representing an image file, such as 'lenna.jpg'
        returns: list of pixel values 
                 in form (R,G,B) such as [(0,0,0),(255,255,255),(38,29,58)...] for RGB image
                 in form L such as [60,66,72...] for BW image
    """
    ## open the file name 
    image = Image.open(filename , 'r')
    ## new list to store each image pixels
    image_pixels = []
    ## get the image width and height sustract 1 from each other 
    ## beacuse the wideth and hight return an int of the full 
    ## but if image width is 100 the range of valid pixels on x-coordinates are 0 to 99 no pixel at index 100  
    x = image.width-1
    y = image.height-1
    # print(x , y)
    ## iteration throght the x axis 
    while x >=0:
        ## inner iteration of the y axis 
        ## reset y to original 
        y = image.height-1
        while y >= 0:
            ## then we get the pixel in x and y values 
            pixel = image.getpixel((x,y))
            ## append this pixel in the list 
            image_pixels.append(pixel)
            ## decrement the y values 
            y-=1
        ## after finish the first value of x for each value of y 
        ## we decrement to the second value do the same 
        x-=1

    return image_pixels


## unit testing for img to pixels 

# filename = '/home/ahmed/vscode/1_ps5/hidden2.bmp'
# image = Image.open(filename)
# # print(image.width , image.height)
# # print(image.getextrema())
# print(img_to_pix(filename))



def pix_to_img(pixels_list, size, mode):
    """
    Creates an Image object from a inputted set of RGB tuples.

    Inputs:
        pixels_list: a list of pixels such as the output of
                img_to_pixels.
        size: a tuple of (width,height) representing
              the dimensions of the desired image. Assume
              that size is a valid input such that
              size[0] * size[1] == len(pixels).
        mode: 'RGB' or 'L' to indicate an RGB image or a 
              BW image, respectively
    returns:
        img: Image object made from list of pixels
    """
    ## create new image object 
    image = Image.new(mode , size)
    ## make our varibales x , y , i 
    x = size[0]-1
    y = size[1]-1
    i = 0 ## used to indexing in the pixels list
    ## iterate through the x width
    while x >= 0:
        ## reset the y axis to original 
        y = size[1]-1
        ## iterate through the y axis hight 
        while y>=0:
            ## put each pixel in the new image with the pixel item in  list that correspond it 
            image.putpixel((x,y) , pixels_list[i])
            ## decremt the y 
            y-=1
            ## increment the i 
            i+=1
        ## decrement the x 
        x-=1
    return image
    

## unit testing 
# filename = '/home/ahmed/vscode/1_ps5/hidden2.bmp'
# image = Image.open(filename)
# image.show()
# size = (image.width , image.height)
# pixel_list = img_to_pix(filename)
# image2 = pix_to_img(pixel_list ,size, 'RGB' )
# image2.show()
 

def filter(pixels_list, color):
    """
    pixels_list: a list of pixels in RGB form, such as
            [(0,0,0),(255,255,255),(38,29,58)...]
    color: 'red', 'blue', 'green', or 'none', must be a string representing 
           the color deficiency that is being simulated.
    returns: list of pixels in same format as earlier functions,
    transformed by matrix multiplication
    """
    ## new list
    ls = []
    ## if the color == None we return the same pixels list 
    if color == 'none':
        return pixels_list
    ## 
    else:
        ## we make the transform matrix from the color 
        transform_matrix = make_matrix(color)
        ## iterate through the pixels list 
        for i in range(len(pixels_list)):
           ## multiple each pixel in list by the transform matrix using the function 
           new = matrix_multiply(transform_matrix,pixels_list[i])
           ## we convert each element in the returned list from the multiplication to integer beacuase it return floats
           # ## beacuase it dows not deal with floats  
           r = int(new[0])
           g = int(new[1])
           b = int(new[2])
           ## then add all to tuple beacuse it deal with tuples not lists
           tup = (r ,g ,b)
           ## then append the typle to the ls
           ls.append(tup)

    return ls


## unit testing 

# im = Image.open('/home/ahmed/vscode/1_ps5/image_15.png')
# im.show()
# # img_array = numpy.asarray(im)
# # print(img_array)
# width, height = im.size
# pixels = img_to_pix('/home/ahmed/vscode/1_ps5/image_15.png')
# non_filtered_pixels = filter(pixels,'red')
# im = pix_to_img(non_filtered_pixels, (width, height), 'RGB')
# im.show()


def extract_end_bits(num_end_bits, pixel):
    """
    Extracts the last num_end_bits of each value of a given pixel.

    example for BW pixel:
        num_end_bits = 5
        pixel = 214

        214 in binary is 11010110. 
        The last 5 bits of 11010110 are 10110.
                              ^^^^^
        The integer representation of 10110 is 22, so we return 22.

    example for RBG pixel:
        num_end_bits = 2
        pixel = (214, 17, 8)

        last 3 bits of 214 = 110 --> 6
        last 3 bits of 17 = 001 --> 1
        last 3 bits of 8 = 000 --> 0

        so we return (6,1,0)

    Inputs:
        num_end_bits: the number of end bits to extract
        pixel: an integer between 0 and 255, or a tuple of RGB values between 0 and 255

    Returns:
        The num_end_bits of pixel, as an integer (BW) or tuple of integers (RGB).
    """
    ## if the pixels entered as tuple
    if type(pixel) == tuple:
            ## we extraxt each element in the tuple beacuse it only 3 
            ## and take the modulo  of the 2 exponant to the number of bits to extract 
            r = pixel[0]%2**num_end_bits
            g = pixel[1]%2**num_end_bits
            b = pixel[2]%2**num_end_bits
            ## return as a tuple
            return (r,g,b)
    else:
        ## if only one number 
        return pixel%2**num_end_bits
        

# print(extract_end_bits(1, (13,13,13))) # get one LSB -> return 1
# print(extract_end_bits(2, 13)) # get two LSBs -> return 1
# print(extract_end_bits(3, 13)) # get three LSBs -> return 5

def reveal_bw_image(filename):
    """
    Extracts the single LSB for each pixel in the BW input image. 
    Inputs:
        filename: string, input BW file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    ## new list of hidden pixels 
    hidden_pixels = []
    ## extract the pixels of image
    pixel_lists = img_to_pix(filename)
    ## iterate throught the pixel list of the image
    for i in pixel_lists:
        ## then extract the Least siginficant bit 
        LSB = extract_end_bits(1 , i)
        ## scalled the lSB to use the max number of the 8 bits of photo 
        ## formulaa LSB value * (max decimle number of bits 2**number of bites (255)) / (2**n - 1)  n is the number of LSB extracted 
        scaled = round(LSB*(255/(2-1)))
        ## append
        hidden_pixels.append(scaled)
    # print(hidden_pixels)
    # print(len(pixel_lists)==len(hidden_pixels))
    ## open the file name 
    img = Image.open(filename)
    ## take the size and mode from the original image
    size = img.size
    mode = img.mode

    ## convert the hidden pixels to image by pix to img function 
    hiddden_image = pix_to_img(hidden_pixels , size , mode)

    return hiddden_image


# filename = '/home/ahmed/vscode/1_ps5/hidden1.bmp'
# image = reveal_bw_image(filename)
# image.show()




def reveal_color_image(filename):
    """
    Extracts the 3 LSBs for each pixel in the RGB input image. 
    Inputs:
        filename: string, input RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    ## intialize the hidden pixel list
    hidden_pixels = []
    ## extract the pixel list from the image
    pixels_list = img_to_pix(filename)
    ## iterate through the list
    for i in pixels_list:
        ## extract the last 3 least significant bits
        LSB_tup = extract_end_bits(3 , i)
        ## scale the LSB with same formule 
        r_scaled = round(LSB_tup[0]*(255/((2**3)-1)) )
        g_scaled = round(LSB_tup[1]*(255/((2**3)-1)) )
        b_scaled = round(LSB_tup[2]*(255/((2**3)-1)) )
        ## make new tuple 
        scaled_tup = (r_scaled , g_scaled , b_scaled)

        hidden_pixels.append(scaled_tup)

    imag = Image.open(filename)
    size = imag.size
    mode = imag.mode

    hidden_image = pix_to_img(hidden_pixels , size , mode)

    return hidden_image


# filename = '/home/ahmed/vscode/1_ps5/hidden2.bmp'
# image = reveal_color_image(filename)
# image.show()