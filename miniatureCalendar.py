import ntplib
from bs4 import BeautifulSoup
from time import gmtime, localtime, strftime
from urllib import request
from os import path, mkdir

import urllib.request
import shutil
from screeninfo import get_monitors
from PIL import Image, ImageDraw

# -*- coding: utf-8 -*-

"""
Created on Mon Oct  2 13:02:22 2017

@author: Fernando Castaño
"""

# Program to set http://miniature-calendar.com image of the day as desktop wallpaper.

__author__ = 'Fernando Castaño'
__copyright__ = 'Copyright (C) 2017'


url_base = 'http://miniature-calendar.com'
ntp_server = 'europe.pool.ntp.org'
dir_path = path.expanduser('~') + '/.miniature-calendar/'


def generate_url():
    # TODO: what happens if there is no internet connection?
    # TODO: Should take the local hour
    try:

        c = ntplib.NTPClient()
        t = c.request(ntp_server, version=3)

        local_offset = localtime().tm_gmtoff
        day_str = strftime("%y%m%d", gmtime(t.tx_time + local_offset))

        return url_base + "/" + day_str

    except:

        # if no internet connection, return false
        print("No internet connection")
        return ""


def get_title_day(soup):

    img = soup.find("img", {"class": "size-full"})
    return img.get('title')


def get_url_images(soup):

    images = soup.find_all("img", {"class": "size-full"})
    url_images = []
    for img in images:
        url_images.append(img.get('src'))

    return url_images


def get_url_file_extension(url):

    url = url.split('.')
    return url[-1]


def main():

    # print(generate_url())

    url = generate_url()
    html_doc = request.urlopen(url).read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    print(dir_path)
    if not path.isdir(dir_path):
        mkdir(dir_path)

    # request.urlretrieve()

    i = 0
    for url_img in get_url_images(soup):
        file_name = "image{}.{}".format(i, get_url_file_extension(url_img))
        with urllib.request.urlopen(url_img) as response, open(dir_path + file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        i += 1

# *********************************** till here is working ********************************


    print(get_title_day(soup))
    print(get_url_images(soup))
    #print(GetSystemMetrics(0) + "x" + GetSystemMetrics(1))





    unique_url_image = "http://miniature-calendar.com/wp-content/uploads/2017/10/171002mon1.jpg"
    file_name_o1 = "C:\\Users\\castafe\\Documents\\image1.jpg"
    file_name_o2 = "C:\\Users\\castafe\\Documents\\image2.jpg"

    # -------------- opcion 1
    # Download the file from `url` and save it locally under `file_name`:
    with urllib.request.urlopen(unique_url_image) as response, open(file_name_o1, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    # -------------- opcion 2
    # Download the file from `url` and save it locally under `file_name`:
    # with urllib.request.urlopen(url) as response, open(file_name_o2, 'wb') as out_file:
    #    data = response.read()  # a `bytes` object
    #    out_file.write(data)

    # --------------
    # number of monitors
    print(len(get_monitors()))

    for m in get_monitors():
        print(str(m))

    # ------------------

    img = Image.open(file_name_o1)
    # first screen
    img = img.resize((1080, 1080), Image.ANTIALIAS)
    borde = Image.new("RGB", (1920, 1080))
    ImageDraw.Draw.fill()
    borde.paste(img, (0, 0))
    borde.save("C:\\Users\\castafe\\Documents\\image_wall.jpg")


if __name__ == '__main__':
    main()




'''

FROM THE OLD PC

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 13:02:22 2017

@author: castafe
"""

import urllib.request
import shutil

from PIL.ImageShow import show
from screeninfo import get_monitors
from PIL import Image, ImageDraw, ImageColor, ImageFont
import ctypes

url = "http://miniature-calendar.com/wp-content/uploads/2017/10/171024tue.jpg"
url2 = "http://miniature-calendar.com/wp-content/uploads/2017/10/171024tue.jpg"
file_name_o1 = "C:\\Users\\castafe\\Documents\\image1.jpg"
file_name_o2 = "C:\\Users\\castafe\\Documents\\image2.jpg"

# -------------- opcion 1
# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen(url) as response, open(file_name_o1, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

with urllib.request.urlopen(url2) as response, open(file_name_o2, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

# -------------- opcion 2
# Download the file from `url` and save it locally under `file_name`:
#with urllib.request.urlopen(url) as response, open(file_name_o2, 'wb') as out_file:
#    data = response.read()  # a `bytes` object
#    out_file.write(data)

# --------------
# number of monitors
print(len(get_monitors()))

for m in get_monitors():
    print(str(m))


# ------------------
number_screens = 2
image_width = 1500
image_height = 1500
resolution_width = 1920
resolution_height = 1080
DISPLACEMENT = 0
bottom_margin = 0.13  # in %

img = Image.open(file_name_o1)
# first screen
img1 = img.resize((1080, 1080), Image.ANTIALIAS)
background1 = Image.new("RGBA", (resolution_width, resolution_height), "#FFFDF3")
# new_im = ImageDraw.Draw(background)
# new_im.rectangle([(0, 0), (1920, 1080)], ImageColor.getrgb(255, 0, 0))
background1.paste(img1, (resolution_width - img1.size[0], 0))
# background1 = background1.convert("RGB")
# background1.save("C:\\Users\\castafe\\Documents\\image_wall.jpg", "JPEG")


# ** second screen
img2 = Image.open(file_name_o2)
background2 = Image.new("RGBA", (resolution_width, resolution_height), "#FFFDF3")
# if image_height > resolution_height:
img3 = img2.crop((0, image_height - (resolution_height + (int(image_height * bottom_margin))),
                img2.size[0], (image_height - int(image_height * bottom_margin))))

background2.paste(img3, (resolution_width - img3.size[0], 0))
# background2 = background2.convert("RGB")
# background.save("C:\\Users\\castafe\\Documents\\image_wall2.jpg", "JPEG")

# ** text title
txt = Image.new('RGBA', background1.size, (255, 255, 255, 0))
fnt = ImageFont.truetype("C:\\Windows\\Fonts\\CENTAUR.TTF", 40)
d = ImageDraw.Draw(txt)
d.text((100, 100), "Sushi bridge", font=fnt, fill=(255, 255, 255, 128))
background1 = Image.alpha_composite(background1, txt)
#show(background1)

# compose wallpaper
compost = Image.new("RGBA", ((2 * resolution_width), resolution_height + DISPLACEMENT), "#FFFDF3")
compost.paste(background1, (0, 0))
compost.paste(background2, (resolution_width, DISPLACEMENT))
big_wallpaper = compost.convert("RGB")
big_wallpaper.save("C:\\Users\\castafe\\Documents\\image_bigwall.jpg", "JPEG")



# ** set wallpaper
SPI_SETDESKWALLPAPER = 0x0014
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,1, "C:\\Users\\castafe\\Documents\\image_bigwall.jpg", 3)




'''