# Scraper

Create spider.sh file -> 
"#!/bin/sh
python3 scrapy runspider pelud.py"

make script executable -> chmod u+x spider.sh

$ sudo crontab -e
add: 01 08 * * <path>/spider.sh


