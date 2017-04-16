# Flask / SQLAlchemy / Graphene Demo

This project serves as a demo model to show what an implementation of GraphQL
with a typical Flask/SQLAlchemy setup might look like, and how the routing
can be simplified from a traditional REST approach.


## Accepted Requests

The project defines three types of URLs:

- Those implemented entirely without graphene
- Those implemented with Graphene-SQLAlchemy
- Those implemented with both Flask-GraphQL and Graphene-SQLAlchemy


### non-graphene (REST) routes:

/users/
- Accepts GET and POST
- GET returns all users
- POST creates a new user. Requires a "name" string field


/projects/
- Accepts GET and POST
- GET returns all projects
- POST creates a new project. Requires a "title" string field and an "owner_id" int field (foreign key to user)



### graphene-sqlalchemy routes

/query
- Accepts GET
- GET returns data specified by the GraphQL query
    - Requires a "query" param in the URL args



### flask-graphql routes

/graphql/
- Accepts GET
- GET returns data specified by the GrapQL query
    - Requires a "query" param in the URL args




# Suggested Quickstart

- Install dependencies with `pip install -r requirements.txt`
- Launch application via `python app.py` from within the `graphene-test` subdirectory.


Seed the database via

1. `POST localhost:5000/users/` with JSON payload `{ "name": "neal" }`
2. `POST localhost:5000/projects/` with JSON payload `{ "title": "project1", "owner_id": 1 }`


Then, to test the non-graphene routes:

- `GET localhost:5000/users/`
- `GET localhost:5000/projects/`

To test the routes using graphene:

- `GET locahost:5000/query?query=query+%7B+users+%7B+name+%7D+%7D`
- `GET localhost:5000/graphql/?query=query+%7B+users+%7B+name+%7D+%7D`

and then

- `GET localhost:5000/query?query=query+%7B+users+%7B+name%2C+projects+%7B+title+%7D+%7D+%7D`
- `GET localhost:5000/graphql/?query=query+%7B+users+%7B+name%2C+projects+%7B+title+%7D+%7D+%7D`

The above query strings are the URL-encoded
'query { users { name } }' and 'query { users { name, project { title } } }'




