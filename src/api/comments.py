from flask import Blueprint, jsonify, abort, request
from ..models import Post, Comment, db
import hashlib
import secrets
import sqlalchemy

bp = Blueprint('comments', __name__, url_prefix='comments')
