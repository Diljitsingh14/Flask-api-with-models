from flask import Flask
from flask_restful import Resource,Api,reqparse
import ast
from migration import users

app = Flask("crud")
api = Api(app)

# users.insert({"name":"Diljit","class":"BCA"})
# users.get_all()
# users.describe()
# users.filter({"id":1})

class User(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id",required=False)
        args = parser.parse_args()
        if args['id']:
            try:
                user = users.filter({"id":args['id']})
                return user,200
            except:
                return "not found",204
        return users.get_all(),200
    def post(self):
        parser = reqparse.RequestParser()
        # parser.add_argument("id",required=True)
        parser.add_argument("name",required=True)
        parser.add_argument("class",required=True)
        args = parser.parse_args()
        # users[args['id']] = args
        users.insert({"name":args['name'],"class":args['class']})
        return users.get_all(),200
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id",required=True)
        parser.add_argument("name",required=True)
        parser.add_argument("class",required=True)
        args = parser.parse_args()
        try:
            result = users.update(args["id"], {"name":args["name"],"class":args["class"]})
            print("result ",result)
            if result:
                user = users.filter({"id":args["id"]})
                return user,200
            else:
                return "not modified",304
        except:
            return "not modified",304
    
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id",required=True)
        args = parser.parse_args()
        res = users.delete(args['id'])
        if res:
            return "success",200
        else:
            return "not deleted",400



api.add_resource(User,"/users")
app.run()