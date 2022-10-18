## Flask-Python3-Starter-Kit 
### by © djengineer 2022
Date updated: 18 OCTOBER 2022

## Purpose:
This starter kit includes a starting bootstrap jumbotron template using bootstrap-4.0.0, python3.6.2 in the virtual environment. You can check the items installed in the requirements.txt.

This is a basic template to jumpstart lightweight python webapps using the base Flask, or Flask-RESTful if you are creating an api backend.

## This doc includes:
- pip packages
- other files
- venv details
- Setting up system environment in linux OSes
- How to start the local server

## How connect to the applications
### flask_app.py
This is for the normal flask application.
```python
http://localhost:8080
http://localhost:8080/form
http://localhost:8080/page1

```
### flask_restful_app.py
This is a RESTFUL flask API application
```python
http://localhost:8081/example/url/hey%20there

```
# Getting Started (Linux)

### Set up the environment
Install python and python virtual environment packages. You may install the packages for the latest python instead.
```bash
sudo apt install python3.9 python3.9-venv -y
```
Create a new venv folder. This will create a new folder called "venv" with the virtual environment.
```bash
# the terminal should be in the python project folder.
python3.9 -m venv venv
```
Have the terminal use the virtual environment
```bash
source ./venv/bin/activate
```
You should see a (venv) in the terminal.

### Starting the servers

Using the new (venv) environment, go to the project folder. We will install the dependencies.
```Python
# install the required packages if it is the first time starting up.
pip install -r requirements.txt
```
To start the servers, use the following commands.
```Python
# to start flask
python flask_app.py

# to start flask
python flask_restful_app.py

```

### Deploying
When deploying a flask app, the main script should be called flask_app.py. If you are running two servers, then split the two into separate project folders.

## pip packages include:
- Pandas
- Numpy
- flask
- flask-restful
- flask-mongoengine
- flask-mqtt

### Package explanations
- https://www.w3schools.com/python/python_mongodb_getstarted.asp: PyMongo is needed for MongoDB non-relational database.
- https://flask.palletsprojects.com/en/2.2.x/patterns/mongoengine/ : MongoEngine is needed to connect with the MongoDB.
- https://mqtt.org/ : MQTT is an IoT messaging standard
- https://www.redhat.com/en/topics/api/what-is-a-rest-api: REST/RESTFUL is a api standard definition. Uses HTTP for req and response.


## Others files:
- Bootstrap 4.0.0-dist 
- Proc file
- requirements.txt

## Venv:
Python 3.9 as per the apt-get python3.9 below

## Setting up the system environment to run the virtual environment

If you have python3.9 in your system already, you may skip this part.
However, you may need to install python3.9-venv before you can use the venv that is included in this kit.

For users with using linux os, use the bash script to install python3.6 and python3.6-venv

### Use the following command to activate the venv
```
source venv/bin/activate
```
For windows or other OSes, make sure you have python3.9

You may want to consider using *Anaconda* to manage virtual environments in windows.

https://www.anaconda.com/

## To run the flask server
### If you have a local terminal:
```
python flask_app.py
```
If you want to run the flask-restful, it is best-practice to change the file name to flask_app.py

Different hosts have different way of starting the app. Please refer to their respective docs for more information.

# Upgrading dependencies(requirements.txt) in the future
https://stackoverflow.com/questions/24764549/upgrade-python-packages-from-requirements-txt-using-pip-command

```python
pip install pip-upgrader
pip-upgrade ./requirements.txt
```