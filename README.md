# Scraper
Potrebno instalirati PostgreSQL, Scrapy, Chart.js, Python3
________________________________________________________
$ sudo -u postgres psql;

$ CREATE DATABASE db_pelud;

$ CREATEUSER encode WITH PASSWORD '100';
________________________________________________________


Create spider.sh

"#!/bin/sh
python3 scrapy runspider pelud.py"

$ sudo crontab -e

* 08 * * <path>/spider.sh
_________________________________________________________

Atributi REST api: grad, biljka, datum

Dohvačamo sve podatke.
URL = 'http://127.0.0.1:5000/api/v1/pelud'

U slučaju potrebe dobivanja podatka za više gradova razdvojimo ih '|'

URL = 'http://127.0.0.1:5000/api/v1/pelud?grad=Zagreb|Osijek'

URL = 'http://127.0.0.1:5000/api/v1/pelud?grad=Zagreb' -> dohvača podatke za jedan grad

U slučaju potreba za dobivanje podataka za više biljka razdvojimo ih '|'

URL = 'http://127.0.0.1:5000/api/v1/pelud?biljka=Joha|Čempresi'

URL = 'http://127.0.0.1:5000/api/v1/pelud?biljka=Joha' - dohvača podatke za jednu biljku

Atribut datum odvajamo znakom '|' ako želimo dobiti podatke nekog razdoblja

URL = 'http://127.0.0.1:5000/api/v1/pelud?datum=13.02.2020|14.02.2020'

URL = 'http://127.0.0.1:5000/api/v1/pelud?datum=13.02.2020' -> dohvača podatke samo za određeni datum.

Primjer kombinacije atributa. Atribute odvajamo znakom '&'

URL = 'http://127.0.0.1:5000/api/v1/pelud?grad=Zagreb|Osijek|Split&biljka=Joha|Čempresi&datum=12.02.2020|14.02.2020'


