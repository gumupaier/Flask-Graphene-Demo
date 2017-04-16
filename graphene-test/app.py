from flask import Flask, request, jsonify
from flask_graphql import GraphQLView

from models import db, Project, ProjectModel, User, UserModel, schema

# create and configure application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/graphene.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create and configure database
# clear tables
db.init_app(app)
db.drop_all(app=app)
db.create_all(app=app)


## Just Flask-SQLALchemy ##
@app.route('/users/', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = UserModel.query.all()
        users = [u.json() for u in users]
        return jsonify(users=users)
    elif request.method == 'POST':
        js = request.get_json()
        u = UserModel(name=js['name'])
        db.session.add(u)
        db.session.commit()
        return jsonify(u.json())


@app.route('/projects/', methods=['GET', 'POST'])
def projects():
    if request.method == 'GET':
        projects = ProjectModel.query.all()
        projects = [p.json() for p in projects]
        return jsonify(projects=projects)
    elif request.method == 'POST':
        js = request.get_json()
        p = ProjectModel(title=js['title'], owner_id=js['owner_id'])
        db.session.add(p)
        db.session.commit()
        return jsonify(p.json())


## With GraphQL-SQLAlchemy ##
@app.route('/query', methods=['GET'])
def usersgraph():
    if request.method == 'GET':
        querystr = request.args.get('query')
        result = schema.execute(querystr, context_value=request)
        return jsonify(result.data)


## With Flask-GraphQL ##
app.add_url_rule('/graphql/', view_func=GraphQLView.as_view('graphql', schema=schema))

if __name__ == '__main__':
    app.run()
