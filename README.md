# A Python 3.6 script for scrapping ps direct
I made this script using WSL - Linux 4.4.0-18362-Microsoft

Make sure you have python3.6 and pipenv installed, if not run

`sudo -H pip3 install pipenv`

Have the following packages installed

`apt-get update`

`apt-get install libasound2 libatk1.0-0 libatk-bridge2.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget libcairo-gobject2 libxinerama1 libgtk2.0-0 libpangoft2-1.0-0 libthai0 libpixman-1-0 libxcb-render0 libharfbuzz0b libdatrie1 libgraphite2-3 libgbm1`

Then install requests-html

`pipenv install requests-html`

Once thats installed activate the virtual env with

`pipenv shell`

## To run

Edit the script to select the ps5 you want to search for

Run the script with
`python3 main.py`

To quit use
`ctrl + c`

## Known issues

This script has **NOT** been tested to work as of 12/10/2020, use only as a back up

The script has issues with pyppeteer freezing, If the terminal isnt updating it may have froze and you will have to restart it.