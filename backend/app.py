from flask import Flask
from flask_pymongo import PyMongo
import private

app = Flask(__name__)
app.secret_key = "secret key"
app.config["MONGO_URI"] = "mongodb+srv://"+private.user+":"+private.passw + \
    "@cluster0.qqssm.mongodb.net/ourpatch?retryWrites=true&w=majority"
mongo = PyMongo(app)
