# Rereddit

This project represent the backend for a hypothetical forum and was constructed via an ORM approach. Work in progress and subject to change.

Current available API functionality is as follows:

| Method    | Description                                                                           | Path                        | JSON Input Parameters    |
|:-------   |:------------                                                                          |:----------------------------|:------------             |
| GET       | Returns a list of all registered users.                                               | /users                      | N/A                      |
| GET       | Returns specified user's id, email, and username.                                     | /users/<int:id>             | N/A                       |
| PUT, PATCH| Edits the specified user's email and password. Password is hashed prior to storage.   | /users/<int:id>             | password, email           |
| POST      | Registers a new user. Password is hashed prior to storage.                            | /users/register             | username, password, email |
| DELETE    | Deletes specified user.                                                               | /users/<int:id>             | N/A                       |
| GET       | Returns a list of all forum posts (does not include replies/comments).                | /posts                      | N/A                       |
| GET       | Returns the id, title, and content of specified post.                                 | /posts/<int:id>             | N/A                       |
| GET       | Returns the categories/topics associated with the specified forum post, if any exist. | /posts/<int:id>/categories  | N/A                       |
| GET       | Returns any replies to the specified forum post.                                      | /posts/<int:id>/replies     | N/A                       |
| POST      | Creates a new forum post.                                                             | /posts/new                  | user_id, title, content   |
| POST      | Assigns a category/topic to the specified forum post.                                 | /posts/<int:id>/categories/new | category_id            |
| POST      | Replies to an existing forum post.                                                    | /posts/<int:id>/reply       | user_id, content          |
| DELETE    | Deletes the specified forum post.                                                     | /posts/<int:id>             | N/A                       |
| GET       | Returns a list of all comments.                                                       | /comments                   | N/A                       |
| GET       | Returns the id, parent id, post id, user id, timestamp, and content of the specified comment. | /comments/<int:id>  | N/A                       |
| GET       | Returns all replies to the specified comment.                                         | /comments/<int:id>/replies  | N/A                       |
| POST      | Creates a reply to the specified comment.                                             | /comments/<int:id>/reply    | N/A                       |
| GET       | Returns all of the forum posts associated with the specified category/topic.          | /categories/<int: id>/posts | N/A                       |
