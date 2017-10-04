# -*- coding: utf-8 -*-

# Program to set http://miniature-calendar.com image of the day as desktop wallpaper.

__author__ = 'Fernando Castaño'
__copyright__ = 'Copyright (C) 2017'

import ntplib
import time
from time import ctime

url_base = 'http://miniature-calendar.com'
ntp_server = 'europe.pool.ntp.org'


def get_date():

    c = ntplib.NTPClient()
    response = c.request(ntp_server, version=3)
    return response


def main():

    print(time.strptime("30 Nov 00", "%d %b %y"))
    text =  (get_date())
    text.stratum
    print(text)



#     time.strftime("%H:%M:%S")
# dir_name = path.expanduser('~') + '\\Bing_Pic_of_the_Day\\' # Wallpaper directory name


if __name__ == '__main__':
    main()
