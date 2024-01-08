from flask import request, jsonify
from config import *
from init_app import app
from blueprints import actors, company, directors, genres, movies, quotes

app.register_blueprint(movies.mod)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=APP_PORT, debug=True, use_reloader=False)
