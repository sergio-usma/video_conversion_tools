# 📚 Efficient MP4 Video Compression Script with Python & FFMPEG

This Python script allows you to compress MP4 videos using the H.265 (HEVC) codec to reduce file sizes without significantly compromising video quality. The tool is designed to handle multiple files within a directory, including subfolders, and provides a detailed report on the space savings achieved after compression.

---

## ⚙️ Prerequisites

1. **Python 3:** Ensure that Python 3 is installed on your system.
2. **FFmpeg:** Download and install FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
   - Add FFmpeg to the system PATH or set the `FFMPEG_PATH` variable in the script with the correct path.

### 🏁 How to Set Up FFmpeg on Windows
1. Download the compressed file from the official website.
2. Extract the contents and copy the path to the `ffmpeg.exe` executable.
3. Add this path to the system PATH or define the `FFMPEG_PATH` variable in the script.

---

## 🚀 How to Use the Script

1. Open a terminal (CMD, PowerShell, or terminal on Mac/Linux).
2. Run the script with the following command:
   ```bash
   python script_name.py
   ```
3. **Enter the directory** containing the video files.
4. Review the **preliminary information:**
   - Number of files to process 🎥
   - Total size of original files 📦
   - Estimated compressed size 📉
   - Estimated operation time ⏱️
5. Confirm whether you want to proceed with the compression (`Y/N`).
6. Decide whether to save the files in a new folder (`Y/N`). If you choose `Y`, provide the path where a subfolder named `COMPRESSED` will be created.

---

## 🛠️ Features

- **Efficient Compression:** Uses the H.265 (HEVC) codec for efficient compression.
- **Adjusted Bitrate:** Configuration of 322855 bps and 24 fps.
- **Subdirectory Support:** Processes all `.mp4` files within folders and subfolders.
- **Original File Preservation:** Does not delete or modify the original files.
- **Detailed Log:** Generates a log file with detailed information about the compressions performed.
- **Informative Summary:** Displays space-saving statistics.
- **Progress Bar:** Visual indicators for file and overall conversion progress.

---

## 📄 Example Workflow

```bash
Enter the directory containing the video files: C:\Videos
Number of files to process: 5
Total size of original files: 1200.00 MB
Estimated total compressed size: 780.00 MB
Estimated operation time: 10.00 minutes
Do you want to start the compression? (Y/N): Y
Do you want to save the videos in a new folder? (Y/N): Y
Enter the directory where you want to save the videos: D:\CompressedVideos
Processing files: 100% |████████████████████| 5/5 [00:45<00:00, 9.00s/file]

=== Compression Summary ===
Files read: 5
Files compressed: 5
Total original size: 1200.00 MB
Total compressed size: 780.00 MB
You have saved 420.00 MB of space by compressing your videos.
Log generated at: video_compression_log_20250207_123938.txt
```

---

## 📋 Technical Details

- **FFmpeg Command:**
  ```bash
  ffmpeg -i input.mp4 -c:v libx265 -crf 28 -preset medium -b:v 322855 -r 24 -c:a aac -b:a 128k output.mp4
  ```
- **Compression:**
  - Video Codec: H.265 (HEVC)
  - CRF Quality: 28 (balance between quality and size)
  - Bitrate: 322855 bps
  - FPS: 24
  - Audio Codec: AAC
  - Audio Bitrate: 128 kbps

---

## 📝 Log Structure
The generated log file has the following format:

```
=== Video Compression Log ===
Compressed file: C:\Videos\video1.mp4 -> D:\CompressedVideos\COMPRESSED\video1_Lite.mp4 (150.00 MB)
Compressed file: C:\Videos\video2.mp4 -> D:\CompressedVideos\COMPRESSED\video2_Lite.mp4 (170.00 MB)
...
=== Summary ===
Files read: 5
Files compressed: 5
Total original size: 1200.00 MB
Total compressed size: 780.00 MB
Space saved: 420.00 MB
```

---

## 🔧 Possible Errors and Solutions

1. **FFmpeg Not Found:**
   - Verify that `FFMPEG_PATH` correctly points to the FFmpeg executable.
   - Ensure that FFmpeg is added to the system PATH.

2. **Permission Denied:**
   - Run the terminal as an administrator.

3. **Files Not Found:**
   - Verify that the entered directory contains `.mp4` files.

4. **Error During Compression:**
   - Check the log file to identify the problematic file.

---

## 💡 Tips

- **Optimize Bitrate:** If you want even greater compression, adjust the CRF value to a higher number (30 or above).
- **Organize Files:** Keep compressed files in separate folders for better organization.
- **Maintain a Backup:** Ensure you keep a backup of your original files.

---

## 🌟 Thank You for Using the Script! 🚀

If you have any questions or suggestions, feel free to share them. I hope you save a lot of space and optimize your videos! 🎥💾

---

## 📜 License
This project is licensed under the MIT License. Please refer to the [LICENSE](./LICENSE) file for more details.
