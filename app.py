from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in your app root folder

e = create_engine('sqlite:///salaries.db')

app = Flask(__name__)

api = Api(app)

class Departments_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct DEPARTMENT from salaries")
        return {'departments': [i[0] for i in query.cursor.fetchall()]}


class Departmental_pos(Resource):
    def get(self, department_name):
        conn = e.connect()
        query = conn.execute("select distinct POSITION from salaries where Department='%s'"%department_name.upper())
        result = {'positions': [i[0] for i in query.cursor.fetchall()]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient


class Departmental_pos_name(Resource):
    def get(self, department_name, pos_name):
        conn = e.connect()
        query = conn.execute("select distinct NAME from salaries where Department='%s'"%department_name.upper() + "AND Position='%s'"%pos_name.upper())
        result = {'name': [i[0] for i in query.cursor.fetchall()]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient


class Departmental_pos_name_sal(Resource):
    def get(self, department_name, pos_name, name):
        conn = e.connect()
        query = conn.execute("select * from salaries where Department='%s'"%department_name.upper() + "AND Position='%s'"%pos_name.upper() + "AND Name='%s'"%name.upper())
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

api.add_resource(Departmental_pos_name_sal, '/dept/<string:department_name>/<string:pos_name>/<string:name>')
api.add_resource(Departmental_pos_name, '/dept/<string:department_name>/<string:pos_name>')
api.add_resource(Departmental_pos, '/dept/<string:department_name>')
api.add_resource(Departments_Meta, '/departments')

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')