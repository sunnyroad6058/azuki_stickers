import json
import os
import sys
import requests

# Using the data generated from discord_web_scraper.js, this script will download the images to the folder "azuki_stickers".
# You can run the script by running the following:
#   cat stickers.json | python download_script.py

def clean_suffix(url):
    # remove everything after last '?' in url
    return url.rsplit('.', 1)[0]

def download_images(data, folder):
    # create folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    for name, url in data:
        # clean suffix and download image
        cleaned_url = clean_suffix(url)
        print(f'Downloading {name} from {cleaned_url}...')
        # open the url
        r = requests.get(url)
        with open(f'{folder}/{name}.jpg', 'wb') as outfile:
            outfile.write(r.content)

if __name__ == '__main__':
    # read json data from stdin
    stuff = sys.stdin.read()
    data = json.loads(stuff)
    download_images(data, 'azuki_stickers')
