from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from app.models import User

class AuthLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()
        
        user = User.query.filter_by(username=args['username']).first()
        if user :
            print('user:', user.username, args['password'])
        else :
            print('user not found')
        if not user or not user.check_password(args['password']):
            print('validation failed')
            return {'message': 'Invalid credentials'}, 401
        
        access_token = create_access_token(identity=user.id)
        ### to do：
        print('validation okay')
        return {'token': access_token, 'user_id': user.id}, 200

class AuthRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        
        args = parser.parse_args()
        
        if User.query.filter_by(username=args['username']).first():
            return {'message': 'Username exists'}, 400
        
        user = User(username=args['username'])
        user.set_password(args['password'])
        user.save()
        
        return {'message': 'User registered'}, 201