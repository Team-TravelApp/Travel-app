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
|POST|[/auth/users/me/](#users-info)|User's info|
|GET|[auth/users/](#all_users)|List of all users|
|POST|[/auth/token/logout/](#logout-user)|Logout user|

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
    "id": 4,
    "username": "Luke",
    "email": "",
}
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