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
	•	Access following/followers list through   profiles


 🔐 Security & Production Hardening
	•	JWT Authentication (stateless and secure)
	•	Permissions: Only authors can edit/delete their own content
	•	Rate limiting to prevent abuse
	•	CORS support for cross-origin requests
	•	Environment-based configuration using .env and python-decouple
	•	Secure production settings:
	•	DEBUG=False
	•	Strict ALLOWED_HOSTS
	•	HTTPS redirection (SECURE_SSL_REDIRECT)
	•	XSS protection (SECURE_BROWSER_XSS_FILTER)
	•	Clickjacking protection (X_FRAME_OPTIONS)
	•	MIME sniffing protection (SECURE_CONTENT_TYPE_NOSNIFF)
	•	Secure cookies (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE)
	•	HSTS (SECURE_HSTS_SECONDS, etc.)   




	1. User Authentication Endpoints
	•	Register (Create a new user)
	•	POST /api/auth/register/
	•	Login (Obtain JWT tokens)
	•	POST /api/auth/login/
	•	Logout (Revoke JWT tokens)
	•	POST /api/auth/logout/
	•	Token Refresh (Get new access token using refresh token)
	•	POST /api/auth/token/refresh/

2. User Profile Endpoints
	•	Get Profile (View user profile)
	•	GET /api/profiles/<username>/
	•	Update Profile (Update user profile)
	•	PUT /api/profiles/<username>/
	•	Follow a User
	•	POST /api/profiles/<username>/follow/
	•	Unfollow a User
	•	POST /api/profiles/<username>/unfollow/

3. Post Endpoints
	•	Create a Post
	•	POST /api/posts/
	•	View All Posts
	•	GET /api/posts/
	•	View a Single Post
	•	GET /api/posts/<post_id>/
	•	Update a Post
	•	PUT /api/posts/<post_id>/
	•	Delete a Post
	•	DELETE /api/posts/<post_id>/

4. Comment Endpoints
	•	Add a Comment to a Post
	•	POST /api/posts/<post_id>/comments/
	•	View Comments for a Post
	•	GET /api/posts/<post_id>/comments/
	•	Update a Comment
	•	PUT /api/posts/<post_id>/comments/<comment_id>/
	•	Delete a Comment
	•	DELETE /api/posts/<post_id>/comments/<comment_id>/

5. Like Feature Endpoints
	•	Like a Post
	•	POST /api/posts/<post_id>/like/
	•	Unlike a Post
	•	POST /api/posts/<post_id>/unlike/

6. Follow System Endpoints
	•	Follow a User
	•	POST /api/profiles/<username>/follow/
	•	Unfollow a User
	•	POST /api/profiles/<username>/unfollow/

	final!!!
	