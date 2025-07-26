import os
from PIL import Image

input_folder = "input_images"
output_folder = "output_images"
new_size = (800, 800) 
output_format = "JPEG" 


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        image_path = os.path.join(input_folder, filename)
        img = Image.open(image_path)

        # Resize the image
        resized_img = img.resize(new_size)

        # Convert RGBA (with alpha) to RGB (no alpha) for JPEG
        if resized_img.mode == 'RGBA' and output_format.upper() == 'JPEG':
            resized_img = resized_img.convert('RGB')

        # Build output path
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")

        # Save resized image
        resized_img.save(output_path, output_format)

        print(f"✔️ Resized and saved: {output_path}")

print("\n Done resizing all images!")
