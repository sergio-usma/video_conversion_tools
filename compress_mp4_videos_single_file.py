import os
import subprocess
import datetime

FFMPEG_PATH = r"C:\ffmpeg\ffmpeg.exe"

# Function to compress a single video file
def compress_video(input_file, output_file):
    command = [
        FFMPEG_PATH, '-i', input_file,
        '-c:v', 'libx265', '-crf', '28', '-preset', 'medium',
        '-b:v', '322855', '-r', '24', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart',
        output_file
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def main():
    # Request file path from the user
    input_file = input("Enter the full path to the video file you want to compress: ").strip()
    input_file = os.path.normpath(input_file)

    # Check if the file exists and is an MP4 file
    if not os.path.exists(input_file) or not input_file.lower().endswith('.mp4'):
        print("The provided file path is invalid or not an MP4 file. Please try again.")
        return

    # Prepare the output file path
    file_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(os.path.dirname(input_file), f"{file_name}_Compressed.mp4")

    print(f"Compressing {input_file}...")
    success = compress_video(input_file, output_file)

    if success:
        compressed_file_size = os.path.getsize(output_file) / (1024 * 1024)
        print(f"Compression completed successfully. Compressed file size: {compressed_file_size:.2f} MB")
        log_file_path = os.path.join(os.path.dirname(input_file), f"compression_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

        # Save the log
        with open(log_file_path, 'w') as log_file:
            log_file.write("=== Video Compression Log ===\n")
            log_file.write(f"Original file: {input_file}\n")
            log_file.write(f"Compressed file: {output_file}\n")
            log_file.write(f"Compressed size: {compressed_file_size:.2f} MB\n")

        print(f"Log file generated at: {log_file_path}")
    else:
        print("Compression failed. Please check the input file and try again.")

if __name__ == "__main__":
    main()
