#dont forget to pip install IL

from PIL import Image
import binascii

def hex_to_image(hex_string, width, height):
    # Convert the hexadecimal string to binary data
    binary_data = binascii.unhexlify(hex_string)

    # Create an image from the binary data
    image = Image.frombytes('RGB', (width, height), binary_data)

    return image

if __name__ == "__main__":
    # Replace this hexadecimal string with your actual hexadecimal data
    hex_data = "0x5......."#hexdecimal goes in here
    #you can also visit https://rawpixels.net/ and upload the hxadecimal in .txt format but where is the fun in that
    # Specify the width and height of the image
    image_width = 100
    image_height = 100

    # Convert hexadecimal string to image
    img = hex_to_image(hex_data, image_width, image_height)

    # Save or display the image
    img.save("output_image.png")
    img.show()
