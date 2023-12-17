from PIL import Image

def merge_images(background_path, foreground_path, output_path):
    # Open the background and foreground images
    background = Image.open("generated_image(3).png")
    foreground = Image.open("output.png")

    # Resize the foreground image to match the background dimensions
    foreground = foreground.resize(background.size, Image.ANTIALIAS)

    # Composite the images
    merged_image = Image.alpha_composite(background.convert('RGBA'), foreground.convert('RGBA'))

    # Save the result
    merged_image.save(output_path, format='PNG')

# Specify the paths for the background and foreground images
background_path = 'output.png'  # Adjust the path to your background image
foreground_path = 'generated_image(3).png'  # Adjust the path to your foreground image
output_path = 'merged_image.png'  # Adjust the desired output path

# Merge the images
merge_images(background_path, foreground_path, output_path)

print(f'Merged image saved to {output_path}')
