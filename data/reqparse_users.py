from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('name', required=True)
parser.add_argument('about', required=False)
parser.add_argument('email', required=True)
parser.add_argument('created_date')
parser.add_argument('news', required=True)