from flask import jsonify, Blueprint
from flask_restful import Resource, Api, reqparse
import psycopg2
from datetime import datetime


pelud_api = Blueprint('resources.pelud', __name__)
api = Api(pelud_api)
parser = reqparse.RequestParser()
parser.add_argument('grad', type=str)
parser.add_argument('biljka', type=str)
parser.add_argument('datum', type=str)

class Pelud(Resource):

    def create_sql(self, clause, name, len, value):
       if len > 1:
           word = 'in'
           value = tuple(value)
       else:
           word = 'like'
           value = "\'" + str(value[0]) + "\'"
       sql= """ {} {} {} {}""".format(clause, name, word, value)
       return sql

    def create_sql_datum(self, clause, name, len, value):
        if len > 1:
            word1 = ' BETWEEN'
            word2 = ' AND'
            date1 = datetime.strptime(value[0], "%d.%m.%Y").strftime('%Y-%m-%d')
            date1 = "\'" + date1 + "\'" + '::date'
            date2 = datetime.strptime(value[1], "%d.%m.%Y").strftime('%Y-%m-%d')
            date2 = "\'" + date2 + "\'" + '::date'
            sql = """ {} {} {} {} {} {}""".format(clause, name, word1, date1, word2, date2 )
        else:
            word = '='
            date = datetime.strptime(value[0], "%d.%m.%Y").strftime('%Y-%m-%d')
            date = "\'" + date + "\'" + '::date'
            sql = """ {} {} {} {}""".format(clause, name, word, date)
        return sql


    def get(self):
        args = parser.parse_args()
        grad = args['grad'].split('|') if args['grad'] else False
        biljka = args['biljka'].split('|') if args['biljka'] else False
        datum = args['datum'].split('|') if args['datum'] else False

        sql = """SELECT * FROM peludstats"""

        if grad and biljka:
            sqlgrad = self.create_sql('WHERE', 'grad', len(grad), grad)
            sql += sqlgrad
            sqlbiljka = self.create_sql('AND', 'naziv', len(biljka), biljka)
            sql += sqlbiljka
        elif grad:
            sqlgrad = self.create_sql('WHERE', 'grad', len(grad), grad)
            sql += sqlgrad
        elif biljka:
            sqlbiljka = self.create_sql('WHERE', 'naziv', len(biljka), biljka)
            sql += sqlbiljka

        if datum and grad or biljka or grad and biljka:
            sqldatum = self.create_sql_datum('AND', 'datum', len(datum), datum)
            sql += sqldatum
        elif datum:
            sqldatum = self.create_sql_datum('WHERE', 'datum', len(datum), datum)
            sql += sqldatum

        conn = psycopg2.connect(host="127.0.0.1", database="db_pelud", user="encode", password="100", port=5432)
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        data = [{r[1]: {'datum': r[2].strftime("%d.%m.%Y"), 'biljka': r[3], 'vrijednost': float(r[4])}} for r in res]
        return jsonify(data)

# pelud_api = Blueprint('resources.pelud', __name__)
# api = Api(pelud_api)
api.add_resource(Pelud, '/api/v1/pelud', endpoint='pelud', )
