#!/bin/bash

# Set your compression level here (in bits per second), default is 500k
COMPRESSION_LEVEL=${1:-500k}

# List of supported video file extensions
EXTENSIONS=("mp4" "avi" "mkv" "mov")

# Loop through all video files in the current directory with supported extensions
for ext in "${EXTENSIONS[@]}"; do
  for i in *."$ext"; do
    # Get the base name of the file without the extension
    BASE=$(basename "$i" ."$ext")
    # Run ffmpeg to compress the video
    ffmpeg -i "$i" -b:v "${COMPRESSION_LEVEL}" "${BASE}_compressed.$ext"
  done
done
