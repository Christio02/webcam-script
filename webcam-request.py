import os
import requests

def download_image(image_url):
    global counter

    response = requests.get(image_url)
    if response.status_code == 200:
        while os.path.exists(f"Cam_Skigebiet_Balderschwang_{counter}.jpg"):
            counter += 1
        file_name = f"Cam_Skigebiet_Balderschwang_{counter}.jpg"
        counter += 1
        with open(file_name, "wb") as file:
            file.write(response.content)
            print("Image downloaded successfully.")
    else:
        print("Failed to download the image. " + str(response.status_code))

if __name__ == "__main__":
    image_url = "https://www.skigebiet-balderschwang.de/website/static/webcam/Cam_Skigebiet_Balderschwang.jpg"
    counter = 332
    download_image(image_url)
