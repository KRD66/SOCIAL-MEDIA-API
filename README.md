Social Media API

Overview

This is a Django-based social media API that allows users to register, authenticate, create posts, follow/unfollow users, and view a personalized feed. The API is built using Django and Django REST Framework (DRF).

Features
 User & Authentication
	•	User registration and login (using Django’s default User model)
	•	Token-based authentication (e.g. via djangorestframework-simplejwt or similar)
	•	User profile management

 Post System (CRUD)
	•	Create new posts
	•	Retrieve all posts or single post detail
	•	Update a post (only by the author)
	•	Delete a post (only by the author)
	•	Like/unlike posts
	•	Count number of likes on a post

 Comment System (CRUD)
	•	Add comments to a post
	•	Retrieve all comments for a post
	•	Update a comment (only by the author)
	•	Delete a comment (only by the author)

 User Following System
	•	Follow/unfollow other users
	•	Count number of followers
	•	Access following/followers list through profiles