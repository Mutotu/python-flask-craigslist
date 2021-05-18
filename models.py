from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    categories = db.relationship('Category')

class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Tag_Posts(db.Model):
    __tablename__ = "tag_posts"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
