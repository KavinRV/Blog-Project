from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import requests
from main import BlogPost

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

all_post = requests.get("https://api.npoint.io/2cf48b7cb1b51c287265").json()

#
# class BlogPost(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     subtitle = db.Column(db.String(250), nullable=False)
#     date = db.Column(db.String(250), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     img_url = db.Column(db.String(250), nullable=False)


for blog in all_post:
    new_blog = BlogPost(
        title=blog['title'],
        subtitle=blog['subtitle'],
        date=blog['date'],
        body=blog['body'],
        author=blog['author'],
        img_url=blog["image_url"]
    )
    db.session.add(new_blog)
    db.session.commit()


