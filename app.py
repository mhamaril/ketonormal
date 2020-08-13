from flask import Flask
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

import routes
import pandas as pd

data = pd.read_sql_table('messages', 'postgres://epnudglueutcfa:8873a2da1797aab137de5e176797e0199fb7543d62ac0b6773dbdc20c8b23288@ec2-54-75-244-161.eu-west-1.compute.amazonaws.com:5432/d2usk0ojd1d3st')  
data.head()
