from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    posts = db.relationship('Post')
    def to_json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "Posts" : [p.to_json() for p in self.posts],
        }

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    tags = db.relationship("Tag",secondary="tag_posts" )
    def to__json(self):
        return{
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "category_id":self.category_id
            
        }

class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    #tag_posts is from sql table not the class
    posts = db.relationship("Post", secondary="tag_posts")
    def to__json(self):
        return {
            "id":self.id,
            "name":self.name
        }

class Tag_Posts(db.Model):
    __tablename__ = "tag_posts"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    def to__json(self):
        return {
            "id":self.id,
            "name":self.name,
            "tag_id":self.tag_id,
            "post_id":self.post_id
        }