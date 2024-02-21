from PIL import Image

# Take list of paths for images
image_path_list = ['dog-1.png','dog-2.png']

# Create a list of image objects
image_list = [Image.open(file) for file in image_path_list]




