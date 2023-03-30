from pydicom import dcmread
from sys import argv, exit
from PIL import Image

with Image.fromarray(dcmread(argv[1]).pixel_array) as img:

    img.save(argv[2])

print('Image Save Done.')

exit()



