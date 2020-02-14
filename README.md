# Scraper

1. install postgres
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04
$ sudo -u postgres psql
$ CREATE DATABASE db_pelud;
$ CREATEUSER encode WITH PASSWORD '100';

Create spider.sh file -> 
"#!/bin/sh
python3 scrapy runspider pelud.py"

make script executable -> chmod u+x spider.sh

$ sudo crontab -e
add: 
01 08 * * <path>/spider.sh


