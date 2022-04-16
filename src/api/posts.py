from flask import Blueprint, jsonify, abort, request
from ..models import Post, Comment, db
import hashlib
import secrets
import sqlalchemy

bp = Blueprint('posts', __name__, url_prefix='/posts')


# index
@bp.route('', methods=['GET'])
def index():
    posts = Post.query.all()
    result = []
    for p in posts:
        result.append(p.serialize())
    return jsonify(result)

# show post


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Post.query.get_or_404(id)
    return jsonify(p.serialize())

# create post


@bp.route('/new', methods=['POST'])
def create():
    if 'user_id' not in request.json or 'title' not in request.json or 'content' not in request.json:
        return abort(400)
    p = Post(request.json['title'],
             request.json['content'], request.json['user_id'])

    db.session.add(p)
    db.session.commit()
    return jsonify(p.serialize())

# show categories/topics


@ bp.route('/<int:id>/categories', methods=['GET'])
def display_categories(id: int):
    p = Post.query.get_or_404(id)
    result = []
    for c in p.relevant_categories:
        print("categories: ", p.relevant_categories)
        result.append(c.serialize())
    return jsonify(result)

# add new category/topic


@bp.route('/<int:id>/categories/new', methods=['POST'])
def new_category(id: int):
    if 'category_id' not in request.json:
        return abort(400)
    p = Post.query.get_or_404(id)
    try:
        p.add_category(request.json['category_id'])
        return jsonify(True)
    except:
        return jsonify(False)

# show replies


@ bp.route('/<int:id>/replies', methods=['GET'])
def display_replies(id: int):
    p = Post.query.get_or_404(id)
    result = []
    for r in p.replies:
        result.append(r.serialize())
    return jsonify(result)

# delete post


@ bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Post.query.get_or_404(id)
    try:
        db.session.delete(p)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
