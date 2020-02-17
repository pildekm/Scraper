# Scraper

$ sudo -u postgres psql;

$ CREATE DATABASE db_pelud;

$ CREATEUSER encode WITH PASSWORD '100';

2. install scrapy

3. Create spider.sh

"#!/bin/sh
python3 scrapy runspider pelud.py"

$ sudo crontab -e

add: 

01 08 * * <path>/spider.sh


