#!/usr/bin/env python3
import http

from flask import Flask, request

app = Flask(__name__)


@app.route('/event', methods=['POST'])
def add_event():
    print("ADDING EVENT")
    print(request.get_data())
    return '', http.HTTPStatus.ACCEPTED


def create_app():
    return app


if __name__ == "__main__":
    create_app().run(port=8080)
