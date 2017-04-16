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
