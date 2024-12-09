from flask import Flask, jsonify
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from foundation.foundation import Foundation

class APIEndpoint(Foundation):
    def run(self):
        app = Flask(__name__)
        app.add_url_rule("/my_endpoint", view_func=self.my_endpoint_handler)

        self.logger.info(f"Starting API endpoint: /my_endpoint")
        app.run(host="0.0.0.0", port=5000)

    def my_endpoint_handler(self):
        self.logger.info("Handling API request.")
        return jsonify({"message": "Hello from /my_endpoint"})

if __name__ == "__main__":
    service = APIEndpoint(service_name="my_endpoint")
    service.serve(service.run)