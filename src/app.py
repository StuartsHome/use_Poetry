from typing import Any

from flask import Flask, request
import logging
from use_poetry.health import health_blueprint
from use_poetry.message_sender import kafka_producer

app = Flask(__name__)
app.config["DEBUG"] = True

@app.before_first_request
def configure_logging():
    logging.info("Service started..")

@app.before_request
def set_logging_context():
    pass

@app.after.request
def clear_logging_context(response):
    pass

app.register_blueprint(health_blueprint)
app.register_blueprint(kafka_producer)

if __name__ == "__main__":
    app.run()