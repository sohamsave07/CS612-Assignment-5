# REST API

## what is this?
simple api example using flask. a flask api object contains one or more functionalities (GET, POST, etc). The FLASK app was uploaded in a Docker container. The RESTful API fetches Departments,Positions in that Departments,Name of the People having Positions and Salary of the People.


## install

```
pip install -r requirements.txt
```

## run
```
python app.py
```

then go to http://localhost:5000/departments

you could drill down by deparments too!

try http://localhost:5000/dept/police

try http://localhost:5000/dept/police/police%20officer

try http://localhost:5000/dept/police/police%20officer/acevedo,%20%20eric
