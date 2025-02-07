import os
import subprocess
import time
import datetime
from tqdm import tqdm

FFMPEG_PATH = r"C:\ffmpeg\ffmpeg.exe"

# Function to get the total size of a set of files in MB
def get_total_size(file_paths):
    return sum(os.path.getsize(file) for file in file_paths) / (1024 * 1024)

# Function to find all MP4 files in a directory and its subdirectories
def get_video_files(directory):
    video_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.mp4'):
                video_files.append(os.path.join(root, file))
    return video_files

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

# Main script function
def main():
    # Request input directory from the user
    input_directory = input("Enter the directory containing the video files: ")
    input_directory = os.path.normpath(input_directory)

    # Check if the directory exists
    if not os.path.exists(input_directory):
        print("The entered directory does not exist. Please try again.")
        return

    # Get list of MP4 files
    video_files = get_video_files(input_directory)
    total_files = len(video_files)

    if total_files == 0:
        print("No MP4 files were found in the directory.")
        return

    # Calculate the total size of the original files
    original_total_size = get_total_size(video_files)
    estimated_compressed_size = original_total_size * 0.65  # Estimated savings

    print("Number of files to process:", total_files)
    print("Total size of original files: {:.2f} MB".format(original_total_size))
    print("Estimated total compressed size: {:.2f} MB".format(estimated_compressed_size))

    # Time estimate
    estimated_time = total_files * 3  # Assuming 3 seconds per file as an approximation
    print("Estimated operation time: {:.2f} minutes".format(estimated_time / 60))

    # Ask if the user wants to save videos in a new folder
    new_directory_choice = input("Do you want to save the videos in another folder? (Y/N): ").strip().upper()
    if new_directory_choice == 'Y':
        output_base_directory = input("Enter the path of the output directory: ").strip()
        output_base_directory = os.path.normpath(output_base_directory)
        if not os.path.exists(output_base_directory):
            print("The entered output directory does not exist. Please try again.")
            return
        output_directory = os.path.join(output_base_directory, "COMPRESSED")
        os.makedirs(output_directory, exist_ok=True)
    else:
        output_directory = os.path.join(input_directory, "COMPRESSED")
        os.makedirs(output_directory, exist_ok=True)

    # Confirm if the user wants to proceed
    proceed = input("Do you want to start compression? (Y/N): ").strip().upper()
    if proceed != 'Y':
        print("Operation canceled.")
        return

    log_entries = []
    compressed_files_count = 0
    compressed_total_size = 0

    # Process files
    with tqdm(total=total_files, desc="Processing files", unit="file") as pbar:
        for video_file in video_files:
            file_name = os.path.splitext(os.path.basename(video_file))[0]
            output_file = os.path.join(output_directory, f"{file_name}_Lite.mp4")

            # Progress bar for each file
            print(f"Processing: {video_file}")
            with tqdm(total=100, desc="File compression", leave=False) as file_bar:
                success = compress_video(video_file, output_file)
                file_bar.update(100)

                if success:
                    compressed_files_count += 1
                    compressed_file_size = os.path.getsize(output_file) / (1024 * 1024)
                    compressed_total_size += compressed_file_size

                    log_entries.append(f"Compressed file: {video_file} -> {output_file} ({compressed_file_size:.2f} MB)")

            pbar.update(1)

    # Save log
    log_file_name = f"video_compression_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    log_file_path = os.path.join(output_directory, log_file_name)

    with open(log_file_path, 'w') as log_file:
        log_file.write("=== Video Compression Log ===\n")
        log_file.write("\n".join(log_entries))
        log_file.write("\n=== Summary ===\n")
        log_file.write(f"Files read: {total_files}\n")
        log_file.write(f"Files compressed: {compressed_files_count}\n")
        log_file.write(f"Total original size: {original_total_size:.2f} MB\n")
        log_file.write(f"Total compressed size: {compressed_total_size:.2f} MB\n")
        log_file.write(f"Space saved: {original_total_size - compressed_total_size:.2f} MB\n")

    # Show summary
    print("\n=== Compression Summary ===")
    print(f"Files read: {total_files}")
    print(f"Files compressed: {compressed_files_count}")
    print(f"Total original size: {original_total_size:.2f} MB")
    print(f"Total compressed size: {compressed_total_size:.2f} MB")
    print(f"You saved {original_total_size - compressed_total_size:.2f} MB of space by compressing your videos.")
    print(f"Log generated at: {log_file_path}")

if __name__ == "__main__":
    main()
