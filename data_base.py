from peewee import *

pg_db = PostgresqlDatabase('db_pelud', user='encode', password='100', host='127.0.0.1', port=5432)

class PeludStats(Model):
    id = AutoField()
    grad = CharField()
    datum = DateField()
    naziv = CharField()
    vrijednost = DecimalField(decimal_places=1)

    class Meta:
        database = pg_db

def add_pelud_data(**kwargs):
    try:
        PeludStats.create(grad=kwargs['grad'],
                          datum=kwargs['datum'],
                          naziv=kwargs['naziv'],
                          vrijednost=kwargs['vrijednost'])
    except:
        print('Error')


def connect_to_db():
    c = pg_db.connect()
    pg_db.create_tables([PeludStats], safe=True)
    if c:
        print('Konekcija otvorena!')

def close_conection_to_db():
    c = pg_db.close()
    if c:
        print('Konekcija zatvorena!')


if __name__ == '__main__':
    connect_to_db()


