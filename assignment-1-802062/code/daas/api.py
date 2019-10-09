import logging
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import request
from flask import jsonify
from dataIngestion.helper import read_db, write_to_db

logging.basicConfig(filename='error.log',level=logging.ERROR)
from pymongo import MongoClient

client = MongoClient('34.69.192.142', 27017, username='root', password='FoSezeYin7Qr', authSource='admin')


app = Flask(__name__)
api = Api(app)



def basic_validations(args):
    """Basic validations for arguments"""

    for k, v in args.items():
        if not k:
            if not isinstance(v, str):
                error = 'Argument parameter should only be String'
                return error

        if k not in ['app', 'category', 'rating', 'reviews', 'size', 'installs', 'type', 'price', 'content_rating', 'genres', 'last_updated',
                     'current_ver', 'android _ver']:
            error = 'Invalid Argument parameter'
            logging.error(error)
            return error

        if not v:
            error = 'Argument parameter should not be empty'
            logging.error(error)
            return error

    return ""


class Status(Resource):
    """ Get status of Webserver """
    def get(self):
        response = {'status': 'Active'}
        return jsonify(response)

class Read(Resource):
    """ API for Shorten URL """

    def get(self, count):

        limit = 0
        if count:
            try:
                limit = int(count)
            except Exception:
                return {"error": "Non Integer parameter"}, 400

        result = read_db(client, False, limit)
        return jsonify(result)


class Write(Resource):
    """ API for Redirect URL """

    def post(self):
        """Overriding get method for creating todo task"""
        data_dict = {}
        data = request.form.copy()
        error = basic_validations(data)
        if error:
            return {"error": error}, 400

        for k, v in data.items():
            data_dict[k] = v

        is_success = write_to_db(client, data_dict)
        if not is_success:
            return {"error": 'Unable to write to CoreDMS'}, 500

        return {}, 201



api.add_resource(Status, '/status/')
api.add_resource(Read, '/read/<count>')
api.add_resource(Write, '/write/')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0', threaded=True)