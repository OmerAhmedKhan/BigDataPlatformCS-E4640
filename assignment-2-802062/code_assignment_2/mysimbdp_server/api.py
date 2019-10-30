import logging
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import request
from flask import jsonify
from helper import get_config, execute_batch_script, get_data_files, execute_stream_script, monitor_stream_ingestion

logging.basicConfig(filename='error.log',level=logging.ERROR)
from pymongo import MongoClient

client = MongoClient('34.69.192.142', 27017, username='root', password='FoSezeYin7Qr', authSource='admin')


app = Flask(__name__)
api = Api(app)


@app.route('/getFiles')
def create_file():
    tenant = request.args.get('tenant')
    return jsonify(get_data_files(tenant))


class Status(Resource):
    """ Get status of Webserver """
    def get(self):
        response = {'status': 'Active'}
        return jsonify(response)

class Config(Resource):
    """ Get status of Webserver """

    def get(self, tenant_id):

        if not tenant_id:
            error = "Tenant not provided"
            logging.error(error)
            return {"error": error}, 400

        response = {'config': get_config('configuration.json', tenant_id)}
        return jsonify(response)

class BatchIngestManager(Resource):
    """ API for Shorten URL """

    def post(self):
        """Overriding get method for creating todo task"""
        data_dict = {}
        data = request.form.copy()
        file_name = data.get('file_name')
        tenant = data.get('tenant_id')
        if not all([file_name, tenant]):
            error = "Required parameters are not provided"
            logging.error(error)
            return {"error": error}, 400

        if not execute_batch_script(file_name, tenant):
            error = "Unable to execute script"
            logging.error(error)
            return {"error": error}, 500

        return


class StreamIngestManager(Resource):
    """ API for Shorten URL """

    def get(self):

        tenant = request.args.get('tenant')
        operation = request.args.get('operation')
        if not all([operation, tenant]):
            error = "Required parameters are not provided"
            logging.error(error)
            return {"error": error}, 400

        if not execute_stream_script(tenant, operation):
            error = "Unable to execute script"
            logging.error(error)
            return {"error": error}, 500

        return

class DataFIles(Resource):
    """ API for Shorten URL """

    def get(self):

        tenant = request.args.get('tenant')
        if not tenant:
            error = "Required parameters are not provided"
            logging.error(error)
            return {"error": error}, 400

        return jsonify(get_data_files(tenant))

class MonitorQueue(Resource):
    """ API for Shorten URL """

    def get(self):

        tenant = request.args.get('tenant')
        if not tenant:
            error = "Required parameters are not provided"
            logging.error(error)
            return {"error": error}, 400

        return jsonify(monitor_stream_ingestion(tenant))

#
#
# class Write(Resource):
#     """ API for Redirect URL """
#
#     def post(self):
#         """Overriding get method for creating todo task"""
#         data_dict = {}
#         data = request.form.copy()
#         error = basic_validations(data)
#         if error:
#             return {"error": error}, 400
#
#         for k, v in data.items():
#             data_dict[k] = v
#
#         is_success = write_to_db(client, data_dict)
#         if not is_success:
#             return {"error": 'Unable to write to CoreDMS'}, 500
#
#         return {}, 201



api.add_resource(Status, '/status/')
api.add_resource(Config, '/getConfig/<tenant_id>')
api.add_resource(BatchIngestManager, '/executeBatch/')
api.add_resource(StreamIngestManager, '/executeStream/')
api.add_resource(DataFIles, '/getDataFiles/')
api.add_resource(MonitorQueue, '/monitor/')
# api.add_resource(Write, '/write/')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0', threaded=True)