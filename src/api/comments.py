from flask import Blueprint, jsonify, abort, request
from ..models import Post, Comment, db
import hashlib
import secrets
import sqlalchemy

bp = Blueprint('comments', __name__, url_prefix='/comments')

# index


@bp.route('', methods=['GET'])
def index():
    comments = Comment.query.all()
    result = []
    for c in comments:
        result.append(c.serialize())
    return jsonify(result)

# show comment


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    c = Comment.query.get_or_404(id)
    return jsonify(c.serialize())

# reply to comment


@bp.route('/<int:id>/reply', methods=['POST'])
def reply(id: int):
    parent = Comment.query.get_or_404(id)
    if 'content' not in request.json or 'user_id' not in request.json:
        return abort(400)
    # p = Post.query.get_or_404(id)
    c = Comment(content=request.json['content'],
                post_id=parent.post_id, user_id=request.json['user_id'])
    c.parent_id = id
    try:
        db.session.add(c)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

# show replies


@ bp.route('/<int:id>/replies', methods=['GET'])
def display_replies(id: int):
    c = Comment.query.get_or_404(id)
    result = []
    for r in c.comment_children:
        result.append(r.serialize())
    return jsonify(result)

# delete comment


@ bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    c = Comment.query.get_or_404(id)
    try:
        db.session.delete(c)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
