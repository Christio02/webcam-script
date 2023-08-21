# webcam-script

#Image Downloader
This is a simple python script that downloads an image from a given URL and saves it to the current directory with a unique file name.

#Requirements
Python 3.x
Requests library (pip install requests)
#Usage
Edit the image_url variable in the script to the URL of the image you want to download.
Edit the counter variable in the script to the starting number for the file name.
Run the script with python image_downloader.py
The script will download the image and save it as Cam_Skigebiet_Balderschwang_<counter>.jpg, where <counter> is an incrementing number to avoid overwriting existing files.
The script will print “Image downloaded successfully.” if the download was successful, or “Failed to download the image. <status_code>” if there was an error, where <status_code> is the HTTP status code returned by the server.
#Example
Here is an example of running the script with the default values:

python image_downloader.py
Image downloaded successfully.
Copy
The script will download the image from [this URL] and save it as Cam_Skigebiet_Balderschwang_332.jpg in the current directory. The image is a webcam view of the Balderschwang ski resort in Germany. Here is how it looks like:

![Cam_Skigebiet_Balderschwang_332.jpg]
