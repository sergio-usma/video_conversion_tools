import os
import subprocess
import time
import datetime
from tqdm import tqdm

FFMPEG_PATH = r"C:\ffmpeg\ffmpeg.exe"

# Function to compress a video file
def compress_video(input_file, output_file):
    command = [
        FFMPEG_PATH, '-i', input_file,
        '-c:v', 'libx265', '-crf', '28', '-preset', 'medium',
        '-b:v', '322855', '-r', '24', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart',
        output_file
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error compressing {input_file}. Error: {result.stderr.decode()}")
    return result.returncode == 0

def main():
    # Ask for the input file path
    input_file = input("Enter the full path of the video file: ").strip()
    input_file = os.path.normpath(input_file)

    # Check if the file exists and is an MP4 file
    if not os.path.isfile(input_file) or not input_file.lower().endswith('.mp4'):
        print("The specified file does not exist or is not an MP4 file. Please try again.")
        return

    # Display file size information
    original_size = os.path.getsize(input_file) / (1024 * 1024)
    print(f"Original file size: {original_size:.2f} MB")

    # Ask for the output directory path
    output_base_directory = input("Enter the path for the output directory: ").strip()
    output_base_directory = os.path.normpath(output_base_directory)

    if not os.path.exists(output_base_directory):
        print("The entered output directory does not exist. Please try again.")
        return

    # Prepare the output file path
    output_directory = os.path.join(output_base_directory, "COMPRESSED")
    os.makedirs(output_directory, exist_ok=True)
    file_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_directory, f"{file_name}_Lite.mp4")

    # Confirm if the user wants to proceed
    proceed = input("Do you want to start the compression? (Y/N): ").strip().upper()
    if proceed != 'Y':
        print("Operation canceled.")
        return

    print(f"\nProcessing: {input_file}")
    with tqdm(total=100, desc="File compression", leave=False) as file_bar:
        success = compress_video(input_file, output_file)
        file_bar.update(100)

    if success:
        compressed_size = os.path.getsize(output_file) / (1024 * 1024)
        print(f"\n=== Compression Summary ===")
        print(f"Original file size: {original_size:.2f} MB")
        print(f"Compressed file size: {compressed_size:.2f} MB")
        print(f"Space saved: {original_size - compressed_size:.2f} MB")
        print(f"Output saved at: {output_file}")
    else:
        print("Compression failed.")

if __name__ == "__main__":
    main()
