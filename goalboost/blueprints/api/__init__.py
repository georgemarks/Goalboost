from flask import Blueprint
from flask_restful import Api

from goalboost.blueprints.api.controllers import People, Person, UserResource, UserTimerResource, EnvironmentLogger


def init_api(app):
    bp_api = Blueprint('api', __name__, url_prefix='/api')
    api = Api(bp_api)

    api.add_resource(People, '/people')
    api.add_resource(Person,  '/people/<string:id>')
    api.add_resource(UserResource, '/users/<string:id>')
    api.add_resource(UserTimerResource, '/users/<string:id>/timer')
    api.add_resource(EnvironmentLogger, "/env", )
    app.register_blueprint(bp_api)
