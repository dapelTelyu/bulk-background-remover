from rembg import remove
from PIL import Image
import os

# Input and output folders
# Make sure to change with your input folder path
input_folder = r'C:\users\user\Pictures\input'
# Make sure to change with your output folder path
output_folder = r'C:\users\user\Pictures\output'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported image extensions
allowed_extensions = ('.jpg', '.jpeg', '.png', 'HEIC')

# Total files processed
total = 0
success = 0
failed = 0

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(allowed_extensions):
        total += 1
        print(f"🔄 Processing: {filename} ...")
        try:
            name_only = os.path.splitext(filename)[0]
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, name_only + ".webp")  # Change extension as needed

            # Open image and remove background
            input_image = Image.open(input_path)
            output_image = remove(input_image)

            # Save the result to output
            output_image.save(output_path)

            success += 1
            print(f"✅ Success: Background removed for {filename}\n")
        except Exception as e:
            failed += 1
            print(f"❌ Failed to process {filename}: {e}\n")

# Final summary
print("📝 Summary:")
print(f"Total files found: {total}")
print(f"Successfully processed: {success}")
print(f"Failed to process: {failed}")
