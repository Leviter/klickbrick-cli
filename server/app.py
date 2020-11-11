#!/usr/bin/env python3
import connexion
from connexion import NoContent


def add_event():
    print("ADDING EVENT")
    return NoContent, 202


app = connexion.App(__name__, specification_dir='../openapi/')
app.add_api('events.yml')
application = app.app

if __name__ == '__main__':
    app.run(port=8080)
