from flask import Blueprint, jsonify, abort, request
from ..models import Category, Post, db  # , Tweet, likes_table
import hashlib
import secrets
import sqlalchemy

bp = Blueprint('categories', __name__, url_prefix='/categories')


# display posts in given category

@bp.route('/<int:id>/posts', methods=['GET'])
def display_posts(id: int):
    c = Category.query.get_or_404(id)
    result = []
    for p in c.category_posts:
        result.append(p.serialize())
    return jsonify(result)
