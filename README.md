# **google image downloader**

a fast and easy way for downloading relative images for a query
this script uses `google custom search api` and you need to make an api key for using it

## Usage

for getting an api key you can follow this link:
https://developers.google.com/custom-search/v1/overview

after getting links in `output.txt` file you can download all the images using `wget`

use this command for downloading all links :

> `$ wget -i output.txt -P <desination directory>`

