from flask_sqlalchemy import SQLAlchemy
import datetime
import sqlalchemy

db = SQLAlchemy()

# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True)
    # backref to see a user's posts
    posts = db.relationship('Post', backref='user_posts', cascade="all,delete")

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email
        }


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.String(), nullable=False)
    timestamp = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments = db.relationship(
        'Comment', backref='post_comments', cascade="all,delete")
    #categories = db.relationship('Comment', backref='post_categories')

    def __init__(self, title: str, content: str, user_id: int):
        self.title = title
        self.content = content
        self.user_id = user_id

    def serialize(self):
        return{
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

    def add_category(self, new_category_id):
        # try:
        stmt = sqlalchemy.insert(posts_categories).values(
            post_id=self.id, category_id=new_category_id
        )
        db.session.execute(stmt)
        db.session.commit()
        #     return jsonify(True)
        # except:
        #     return jsonify(False)


posts_categories = db.Table(
    'posts_categories',
    db.Column(
        'post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True
    ),
    db.Column(
        'category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True
    )
)


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(128), unique=True, nullable=False)
    category_posts = db.relationship(
        'Post', secondary=posts_categories,
        lazy='subquery',
        backref=db.backref('relevant_categories', lazy=True)
    )

    def __init__(self, description: str):
        self.description = description

    def serialize(self):
        return{
            'description': self.description
        }


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    content = db.Column(db.String(), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    parent_post = db.relationship('Post', lazy='subquery',
                                  backref=db.backref('replies', lazy=True))
    # backref for children
    children = db.relationship(
        'Comment', backref='comment_children', remote_side='Comment.id')

    def __init__(self, timestamp, content, post_id):
        self.timestamp = timestamp,
        self.content = content,
        self.post_id = post_id

    def serialize(self):
        return{
            'id': self.id,
            'timestamp': self.timestamp,
            'content': self.content
        }
