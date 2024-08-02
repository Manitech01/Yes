Create a directory "images" $ mkdir images
$ cd images
Run the update command:
$ sudo apt update
Install "imagemagick" $ sudo apt install imagemagick
Command to download a .png file in Linux subsystem:
$ wget
https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/1200pxInstagram_icon.png
Command to create a shell script:
$ nano pngtojpg.sh
Paste the following code :
#!/bin/bash
# Check if ImageMagick is installed
if ! command -v convert &> /dev/null; then
echo "Error: ImageMagick is not installed. Please install it first." exit 1
fi
# Convert images to JPEG
for file in *.{png,jpg,jpeg,gif,bmp}; do
if [ -f "$file" ]; then
filename="${file%.*}" extension="${file##*.}"
Ex.No:05
Write a shell script, which converts all images inthecurrent directory in JPEG. Date:
if [ "$extension" != "jpg" ] && [ "$extension" != "jpeg" ]; then
convert "$file" "${filename}.jpg" echo "Converted $file to ${filename}.jpg"
fi
fi
done
echo "Conversion completed." To save and d exit:
Ctrl+s
Ctrl+x
Make sure that both the script and png file is located in the same directory!
Now run the shell script:
$ bash pngtojpg.sh
The png file will be converted into Jpg file :
$ ls
will show both png and jpg files in same directory