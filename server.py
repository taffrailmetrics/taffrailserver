import json
import os
from flask import Flask, request, Response
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from kubernetes import client, config
from taffrail.taffrail_client import MetricsClient

config.load_incluster_config()
metrics_client = MetricsClient(client)

app = Flask(__name__)
api = Api(app)

class Root(Resource):
    def get(self):
        return 'Taffrail-Server is sailing happily, clearly looking at the ocean ahead'

class Metrics(Resource):
    def get(self):
        source = request.args.get('source')
        metrics_response = None

        if source:
            metrics_response = metrics_client.get_metrics_with_source(source).to_dict()
        else:
            metrics_response = metrics_client.get_metrics(True)

        response = Response()
        response.status_code = 200
        response.content_type = "application/json"
        response.data = json.dumps(metrics_response)

        return response


class Sources(Resource):
    def get(self):
        sources = metrics_client.get_sources()
        return jsonify(**sources)


api.add_resource(Root, '/')
api.add_resource(Metrics, '/metrics')
api.add_resource(Sources, '/sources')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("HTTP_PORT") or 5000)
