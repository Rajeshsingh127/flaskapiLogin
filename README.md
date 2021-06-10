# flaskapiLogin
Basic flask login signup system using flask to create API endpoints

## Table Of Content
- [Database Structure](#database-structure)

- [API endpoints](#api-endpoints)
    - [Login endpoint](#login-endpoint)
    - [Signup endpoint](#signup-endpoint)

## Database Structure 
  1. A User Table which stores user Info:
     - id ```primary key```
     - username ```unique```
     - password ```hashed password```
     - email ```unique email```

## API Endpoints
### Login Endpoint
POST request to the ```http://127.0.0.1:5000/login/``` endpoint with username and password field in json format. 
```
{
      "message": "welcome",
      "username": "rajesh",
      "email": "rajesh@gmail.com"

}
```
### Signup Endpoint
POST request to ```http://127.0.0.1:5000/signup/``` endpoint with username, password, email in json format will result in user creation in database. New user data will be returned if user is created

```
Output on successful user creation include everything except password field

{
    "message": "user created",
    "id": 6,
    "email": "sample@gmail.com",
    "username": "sample",
  
}
```
