# TestingJpegDeblocking
Python scripts for batch testing image deblocking programs

Made for Lanit-Tercom Summer School 2022

# How to use

This uses:
- Pillow (https://github.com/python-pillow/Pillow)
- Sewar (https://github.com/andrewekhalel/sewar)
- FFmpeg (https://ffmpeg.org/)
- JPEG2PNG (https://github.com/victorvde/jpeg2png)
- Jpeg-Quantsmooth (https://github.com/ilyakurdyukov/jpeg-quantsmooth)
- Knusperli (https://github.com/google/knusperli)
- COLMAP (https://github.com/colmap/colmap)

1. Set up the work folder like in the example
2. Launch the makefolders.py script
3. Launch the compress.py script with appropriate parameters to compress the images
4. Launch the restore.py script with appropriate parameters to restore the compressed images with a program
5. Launch the metrics.py script to calculate the average PSNR, PSNR-B, SSIM and Cross Match Value (Feeatures) into results.csv
6. Launch the metricscolmap.py script to write the COLMAP camera settings into the output folder

Credit to my colleage Abletobetable for sharing his code with me
https://github.com/Abletobetable/lanit-summer2022-traffic
