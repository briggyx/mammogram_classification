from sys import argv
from PIL import Image, ImageOps

# Open the input image
img = Image.open(argv[1])

# Convert the image to black and white
img = ImageOps.grayscale(img)

# Automatically adjust the contrast of the image
img = ImageOps.autocontrast(img)

# Resize the image to 2000 x 2400
img = img.resize((2000, 2400))

# Get the width and height of the image
width, height = img.size

# Get the pixel values for each half of the image
left_pixels = list(img.crop((0, 0, width//2, height)).getdata())
right_pixels = list(img.crop((width//2, 0, width, height)).getdata())

# Calculate the average pixel brightness for each half of the image
left_brightness = sum(left_pixels) / len(left_pixels)
right_brightness = sum(right_pixels) / len(right_pixels)

# Create a boolean for which side was brighter
side = 'R' if right_brightness > left_brightness else 'L'

# If the right side is brighter, flip the image horizontally
if side == 'R':
    img = ImageOps.mirror(img)

# Parse the filename for output info
patient = argv[1].split('_')[0]
img_num = int(argv[1].split('.')[-2][-1])
view = 'T' if img_num in [1,3] else 'S'

outfile = f'{argv[2]}/{patient}.{side}.{view}.jpg'

# Save the image to the output file name
img.save(outfile, 'JPEG')
