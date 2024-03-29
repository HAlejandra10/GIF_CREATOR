from PIL import Image

# Take list of paths for images
image_path_list = ['dog-1.png','dog-2.png']

# Create a list of image objects
image_list = [Image.open(file) for file in image_path_list]

# Save the first image as a GIF file
image_list[0].save(
            'animation2.gif',
            save_all=True,
            append_images=image_list[1:], # append rest of the images
            duration=1000, # in milliseconds
            loop=0)

#The image must be the same dimensions




