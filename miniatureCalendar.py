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


def main():

    # print(generate_url())
    url = generate_url()
    html_doc = request.urlopen(url).read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    print(dir_path)
    if not path.isdir(dir_path):
        mkdir(dir_path)

    request.urlretrieve()


    print(get_title_day(soup))
    print(get_url_images(soup))
    print(GetSystemMetrics(0) + "x" + GetSystemMetrics(1))


# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 13:02:22 2017

@author: castafe
"""



url = "http://miniature-calendar.com/wp-content/uploads/2017/10/171002mon1.jpg"
file_name_o1 = "C:\\Users\\castafe\\Documents\\image1.jpg"
file_name_o2 = "C:\\Users\\castafe\\Documents\\image2.jpg"

# -------------- opcion 1
# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen(url) as response, open(file_name_o1, 'wb') as out_file:
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

img = Image.open(file_name_o1)
# first screen
img = img.resize((1080, 1080), Image.ANTIALIAS)
borde = Image.new("RGB", (1920, 1080))
ImageDraw.Draw.fill()
borde.paste(img, (0, 0))
borde.save("C:\\Users\\castafe\\Documents\\image_wall.jpg")



if __name__ == '__main__':
    main()


