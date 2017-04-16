from flask_sqlalchemy import SQLAlchemy
from graphene import List, ObjectType, Schema
from graphene_sqlalchemy import SQLAlchemyObjectType

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(64), unique=True)
    projects = db.relationship('ProjectModel', backref='owner')

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'projects': [p.json() for p in self.projects]
        }


class ProjectModel(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.VARCHAR(64), unique=True)

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'owner': self.owner_id
        }


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel


class Project(SQLAlchemyObjectType):
    class Meta:
        model = ProjectModel


class Query(ObjectType):
    users = List(User)
    projects = List(Project)

    def resolve_users(self, args, context, info):
        query = User.get_query(context)
        return query.all()

    def resolve_projects(self, args, context, info):
        query = Project.get_query(context)
        return query.all()

schema = Schema(query=Query)
