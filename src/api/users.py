from flask import Blueprint, jsonify, abort, request
from ..models import User, db
import hashlib
import secrets
import sqlalchemy


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('users', __name__, url_prefix='/users')


# user index


@bp.route('', methods=['GET'])
def index():
    users = User.query.all()
    result = []
    for u in users:
        result.append(u.serialize())
    return jsonify(result)

# show user


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())

# delete user/account


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

# edit user info


@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    u = User.query.get_or_404(id)
    if 'password' not in request.json and 'email' not in request.json:
        return abort(400)
    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        u.password = scramble(request.json['password'])
    if 'email' in request.json:
        if '@' not in request.json['email']:
            return abort(400)
        u.email = request.json['email']
    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)

# user registration


@bp.route('/register', methods=['POST'])
def create():
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    if len(request.json['password']) < 8:
        return abort(400)
    u = User(request.json['username'], scramble(request.json['password']))
    if 'email' in request.json:
        u.email = request.json['email']
    db.session.add(u)
    db.session.commit()
    return jsonify(u.serialize())
