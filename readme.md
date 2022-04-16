# Rereddit (working title)

This purpose of this project is to build the backend for a hypothetical forum. Work in progress and subject to change.

During development, I opted to build this database via an ORM approach in order to get more comfortable with flask and to simplify entries which involve multiple tables. Future changes will include full implementation of comments to allow for each comment to have a parent and multiple children and the development of additional API endpoints, including those which would facilitate the creation, editing, and deletion of comments.

As of the date of this document (2022-04-16), available API functionality is as follows:

| Method    | Description                                                                           | Path                        | JSON Input Parameters     |
|:-------   |:------------                                                                          |:----------------------------|:------------              |
| GET       | Returns a list of all registered users.                                               | /users/                     | N/A                       |
| GET       | Returns specified user's id, email, and username.                                     | /users/<int: id>            | N/A                       |
| PUT       | Edits the specified user's email and password. Password is hashed prior to storage.   | /users/<int: id>            | password, email           |
| POST      | Registers a new user. Password is hashed prior to storage.                            | /users/register             | username, password, email |
| DELETE    | Deletes specified user.                                                               | /users/<int: id>            | N/A                       |
| GET       | Returns a list of all forum posts (does not include replies/comments).                | /posts/                     | N/A                       |
| GET       | Returns the id, title, and content of specified post.                                 | /posts/<int: id>            | N/A                       |
| GET       | Returns the categories/topics associated with the specified forum post, if any exist. | /posts/<int: id>/categories | N/A                       |
| GET       | Returns any replies to the specified forum post.                                      | /posts/<int: id>/replies    | N/A                       |
| POST      | Creates a new forum post.                                                             | /posts/new                  | user_id, title, content   |
| POST      | Assigns a category/topic to the specified forum post.                                 | /posts/<int: id>/categories/new | category_id           |
| DELETE    | Deletes the specified forum post.                                                     | /posts/<int: id>            | N/A                       |
| GET       | Returns all of the forum posts associated with the specified category/topic.          | /categories/<int: id>/posts | N/A                       |
