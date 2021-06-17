from flask import Blueprint
from methods import article
from . import is_api, protected, cors_allow
import constants.messages

article_blueprint = Blueprint('Article', __name__)


@article_blueprint.route('/<int:example>', methods=['GET', 'OPTIONS'])
@cors_allow()
@is_api()
@protected()
def get_article(user_uuid, user_token, is_admin, data, example: int):
    '''
    status, result = method.example_method(*data)

    if not status:
        return {'error': constants.messages.exception_occurred}, 404

    else:
        return result
    '''


@article_blueprint.route('', methods=['POST', 'OPTIONS'])
@cors_allow()
@is_api(required_keys=['board', 'title', 'content'], acceptable_keys=['prefix'], input_type='json')
@protected()
def create_article(is_login, user_uuid, user_token, checked_actions, data):
    '''
    status, message, status_code = article.create_article(checked_actions, **data)

    if not status:
        return {'error': message}, status_code

    else:
        return {'created': message}
    '''
