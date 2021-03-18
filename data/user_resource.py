from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.users import User
from data.reqparse_users import parser


def abort_if_news_not_found(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message=f"User {user_id} not found")


class UserResource(Resource):
    def get(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({'users': users.to_dict(
            only=('id', 'name', 'email', 'about'))})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'name', 'email', 'about')) for item in news]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            id=args['id'],
            name=args['name'],
            about=args['about'],
            email=args['email'],
            created_date=args['created_date'],
            news=args['news']
        )
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})
