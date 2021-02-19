from flask import (
    Blueprint, jsonify, render_template
)
from log import log

default_blueprint = Blueprint('default', __name__)

#api.init_app(default_blueprint)

@default_blueprint.route('/index')
def index():
    log.info('API call index')
    return render_template('index.html')

@default_blueprint.route('/api/v1/test')
def test():
    log.info('API call test')
    return jsonify(
        status=True,
        message="Ok, It's alive!!"
    )