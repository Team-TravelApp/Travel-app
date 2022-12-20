# Travel-app
This application is a travel bucket list. 

*Travel-app is an Application Programming Interface (API) built using Django Rest Framework (DRF)
All requests require authentication.
## Base URL:
All endpoints begin with `http://127.0.0.1:8000/`
NOTE: API Root is /api/
|  Method  |  Endpoint  |  Description |
| -------- | ---------- | ------------ |
|POST|[/auth/users/](#create-a-new-user)|Create a new user|
|POST|[/auth/token/login/](#login-user)|Login user|
|GET|[/auth/users/me/](#users-info)|User's info|
|GET|[auth/users/](#all_users)|List of all users|
|POST|[/auth/token/logout/](#logout-user)|Logout user|
|GET|[api/attractionposts/](#list-of-all-attraction-posts)|returns a list of all attraction-posts|
|GET|[api/attractionposts/{pk}/](#details-of-one-attraction-post)|details of one attraction-post|
|POST|[api/questions/](#create-a-question)|create a question|
|PATCH|[api/attractionposts/{pk}/](#update-a-attraction-post)|update a attraction-post|
|DELETE|[api/attractionposts/{pk}/](#delete-a-attraction-post)|delete a attraction-post|
|GET|[api/questions?search=<search_term>](#search-questions)|search question title and text|
|GET|[api/questions/<int:question_pk>/answers/](#list-answers-per-question)|list answers per question|


## Create a new user
### Request
Required fields: username and password
Optional fields: email
```json
POST auth/users/
{
  "username": "Luke",
  "password": "Momentum1"
}
```
### Response
Response: If you receive the same info you provided, user creation was successful!
```json
201 Created
{
  "email": "",
  "username": "Luke",
  "id": 4,
}
```
## Login user
### Request
Required fields: username, password
```json
POST auth/token/login/
{
    "username": "Luke",
    "password": "Momentum1"
}
```
### Response
```json
200 OK
{
    "auth_token": "d99a2de1b0a09db0fc2da23c9fdb1fc2447fff5d"
}
```
NOTE: auth_token must be passed for all requests with the logged in user. It remains active till user is [logged out](#logout-user).
## User's info
Requirement: user must be logged in.
```json
GET /auth/users/me/
```
### Response
```json
200 OK
{
	"email": "",
	"id": 1,
	"username": "tim"
}
```
## List of User's 
Requirement: user must be logged in.
```json
GET /auth/users/
```
### Response
```json
200 OK
[
	{
		"email": "",
		"id": 1,
		"username": "tim"
	},
	{
		"email": "",
		"id": 2,
		"username": "user1"
	},
	{
		"email": "",
		"id": 3,
		"username": "user2"
	},
	{
		"email": "",
		"id": 4,
		"username": "user3"
	},
	{
		"email": "",
		"id": 5,
		"username": "user4"
	}
]
```
## Logout user
### Request
Required fields: None
```json
POST /auth/token/logout/
```
### Response
```json
204 No Content
```
## list of all attraction-posts
Returns list of all attraction-posts.
### Request
Required fields: None
```json
GET api/questions/
```
### Response
```json
200 OK
[
	{
		"pk": 4,
		"user": "tim",
		"title": "post 3",
		"country": "GP",
		"description": "post 3",
		"created_at": "2022-12-20T15:08:35.321137",
		"interest_rating": 1,
		"comments": [
			8,
			10
		],
		"total_comments": 2
	},
	{
		"pk": 6,
		"user": "tim",
		"title": "post 3",
		"country": "GP",
		"description": "post 3",
		"created_at": "2022-12-20T15:29:37.541000",
		"interest_rating": 2,
		"comments": [],
		"total_comments": 0
	},
	{
		"pk": 2,
		"user": "tim",
		"title": "post 1",
		"country": "AD",
		"description": "post 1",
		"created_at": "2022-12-20T15:07:30.046038",
		"interest_rating": 7,
		"comments": [
			4,
			5,
			6
		],
		"total_comments": 3
	},
	{
		"pk": 3,
		"user": "tim",
		"title": "post 2",
		"country": "CW",
		"description": "post 2",
		"created_at": "2022-12-20T15:08:06.122249",
		"interest_rating": 5,
		"comments": [
			7
		],
		"total_comments": 1
	},
	{
		"pk": 1,
		"user": "tim",
		"title": "new post",
		"country": "AM",
		"description": "asdfasdf",
		"created_at": "2022-12-20T14:25:49.645179",
		"interest_rating": 1,
		"comments": [
			1,
			2,
			3
		],
		"total_comments": 3
	},
	{
		"pk": 5,
		"user": "tim",
		"title": "post 4",
		"country": "NI",
		"description": "post 4",
		"created_at": "2022-12-20T15:09:02.464600",
		"interest_rating": 1,
		"comments": [
			9,
			11
		],
		"total_comments": 2
	}
]
```
## details of one attraction-post
Returns detail of one attraction-post.
### Request
Required fields: None
```json
GET api/questions/<pk>/
```
### Response
```json
200 OK
{
	"pk": 5,
	"user": "tim",
	"title": "post 4",
	"country": "NI",
	"description": "post 4",
	"created_at": "2022-12-20T15:09:02.464600",
	"interest_rating": 1,
	"comments": [
		9,
		11
	],
	"total_comments": 2
}
```
## update a attraction-post
update a attraction-post.
### Request
Required fields:
```json
PATCH api/attractionposts/<pk>/
{
   "title": "post 12"
}
```
### Response
```json
200 Created
{{
	"pk": 4,
	"user": "tim",
	"title": "post 12",
	"country": "GP",
	"description": "post 3",
	"created_at": "2022-12-20T15:08:35.321137",
	"interest_rating": 1,
	"comments": [
		8,
		10
	],
	"total_comments": 2
}
```
## delete a attraction-post
delete a attraction-post.
### Request
Required fields:None
```json
DELETE api/questions/<pk>/

```
### Response
```json
204 No Content

```