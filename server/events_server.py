#!/usr/bin/env python3
import connexion
from connexion import NoContent
from flask import request


app = connexion.FlaskApp(__name__, specification_dir='openapi/')


def add_event():
    print("ADDING EVENT")
    print(request.get_data())
    return NoContent, 202


def run(actually_run=True):
    app.add_api('events.yml')
    if actually_run:
        app.run(port=8080, debug=True)
    else:
        return app


if __name__ == '__main__':
    run()
