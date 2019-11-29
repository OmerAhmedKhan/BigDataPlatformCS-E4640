import logging
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import request
from flask import jsonify
from helper import execute_batch_script, execute_stream_ingest_script, execute_stream_analytics

logging.basicConfig(filename='error.log',level=logging.ERROR)
from pymongo import MongoClient

client = MongoClient('34.69.192.142', 27017, username='root', password='FoSezeYin7Qr', authSource='admin')


app = Flask(__name__)
api = Api(app)


class Status(Resource):
    """ Get status of Webserver """
    def get(self):
        response = {'status': 'Active'}
        return jsonify(response)


class BatchAnalyticsManager(Resource):
    """ Batch Analytics API  """

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
    """ API data Ingestion """

    def get(self):

        tenant = request.args.get('tenant')
        operation = request.args.get('operation')
        if not all([operation, tenant]):
            error = "Required parameters are not provided"
            logging.error(error)
            return {"error": error}, 400

        if not execute_stream_ingest_script(tenant, operation):
            error = "Unable to execute script"
            logging.error(error)
            return {"error": error}, 500

        return

class StreamAnalytics(Resource):
    """ Stream Analytics API  """

    def get(self):

        tenant = request.args.get('tenant')
        window_size = request.args.get('windowSize')
        if not all([window_size, tenant]):
            error = "Required parameters are not provided"
            logging.error(error)
            return {"error": error}, 400

        if not execute_stream_analytics(client, tenant, window_size):
            error = "Unable to execute stream analytics"
            logging.error(error)
            return {"error": error}, 500

        return



api.add_resource(Status, '/status/')
api.add_resource(BatchAnalyticsManager, '/executeBatch/')
api.add_resource(StreamIngestManager, '/executeStream/')
api.add_resource(StreamAnalytics, '/executeStreamAnaytics/')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0', threaded=True)