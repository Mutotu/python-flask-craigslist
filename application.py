
from flask import Flask, request
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
import os
from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

import models
models.db.init_app(app)



@app.route("/", methods=["GET"])
def root():
    return {"message": "ok"}

@app.route('/categories', methods=["GET", "POST"])
def get_categories():
    if request.method == "GET":
        categories = models.Category.query.all()
        return {"categories": [c.to__json() for c in categories]}

    elif request.method == "POST":
        category = models.Category(
            name = request.json['name']
        )
        models.db.session.add(category)
        models.db.session.commit()

        return {"category": category.to__json()}

@app.route('/categories/<int:id>', methods=["GET","POST"])
def get_category(id):
    try:
        category = models.Category.query.filter_by(id=id).first()
        if request.method == "GET":
            return {"categories": category.to__json()}
        elif request.method == "POST":
            post = models.Post(
                title= request.json["title"],
                description = request.json["description"]
            )
            category.posts.append(post)
            models.db.session.add(category)
            models.db.session.add(post)
            models.db.session.commit()
          
            return {
                "category": category.to__json()
            }
    except Exception as e:
        return {"error": e}

@app.route("/categories/<int:tag_id>/posts/<int:post_id>", methods=["PUT"])
def create_post(tag_id, post_id):
    try:
        tag = models.Tag.query.filter_by(id=tag_id).first()
        post = models.Post.query.filter_by(id=post_id).first()

        tag.posts.append(post)
        post.tags.append(tag)

        models.db.session.add(post, tag)

        models.db.session.commit()

        return {"tag": tag.to__json(), "post": post.to__json()}
    except Exception as e:
        return {"error": f'{e}'}
    
    
@app.route("/tag", methods=["GET", "POST"])
def get_all_tags():
    try:
        if request.method == "GET":
            tags = models.Tag.query.all()
            return {"tags": [t.to__json() for t in tags]}

        elif request.method == "POST":
            tag = models.Tag(
                name = request.json['name']
            )
            models.db.session.add(tag)
            models.db.session.commit()
            return {"tag" : tag.to__json()}
    except Exception as e:
        return {"error": f"{e}"}

#  GET | /tags/:tagId/posts |
# @app.route("/tags/<int:tag_id>/posts", methods=["GET"])
# def get_tag():
#     try:
#         tags = models.Tag.query.filter_by(id=tag_id).first()
        
#         return {"tags_posts": [p.to__json() for p in tags.posts]}
#     except Exception as e:
#         return {"error": f"{e}"}

@app.route('/tag/<int:tag_id>/posts', methods=["GET"])
def get_all_tag_posts(tag_id):
    try:
        tag = models.Tag.query.filter_by(id=tag_id).first()
        
        return {"tag_posts": [p.to__json() for p in tag.posts]}
    except Exception as e:
        return {"error": f"{e}"}


@app.route('/post/<int:post_id>/tags', methods=["GET"])
def get_all_post_tags(post_id):
    try:
        post = models.Post.query.filter_by(id=post_id).first()
        
        return {"post_tags": [t.to__json() for t in post.tags]}
    except Exception as e:
        return {"error": f"{e}"}


@app.route('/post/<int:id>', methods=["DELETE"])
def delete_post(id):
    post = models.Post.query.filter_by(id=id).first()

    models.db.session.delete(post)
    models.db.session.commit()

    return {'deleted successfully' : post.to__json()}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)