from flask import Blueprint, request
from flask_restful import Api
from views import SurveyMonkeyView

SURVEY_MONKEY_BLUEPRINT = Blueprint("survey_monkey", __name__, url_prefix="/survey_monkey")

# ============================================
# Authentication
# ============================================

@SURVEY_MONKEY_BLUEPRINT.route("/oauth_url", methods=["GET"])
def get_oauth_url():
    """ Get the OAuth URL """

    response = SurveyMonkeyView.get_oauth_url(request)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/get_token", methods=["POST"])
def get_video_data():
    """ Get the token """

    response = SurveyMonkeyView.exchange_code_for_token(request)
    return response

# ============================================
# CRUD for Surveys
# ============================================

@SURVEY_MONKEY_BLUEPRINT.route("/get_survey_list", methods=["GET"])
def get_survey_list():
    """ Get the list of surveys """

    response = SurveyMonkeyView.get_survey_list(request)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/create_survey", methods=["POST"])
def create_survey():
    """ Create a survey """

    response = SurveyMonkeyView.create_survey(request)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/update_survey/<string:survey_id>", methods=["PUT"])
def update_survey(survey_id):
    """ Update a survey """

    response = SurveyMonkeyView.update_survey(request, survey_id)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/survey_detail/<string:survey_id>", methods=["GET"])
def get_survey_detail(survey_id):
    """ Get the detail of a survey """

    response = SurveyMonkeyView.get_survey_details(request, survey_id)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/delete_survey/<string:survey_id>", methods=["DELETE"])
def delete_survey(survey_id):
    """ Delete a survey """

    response = SurveyMonkeyView.delete_survey(request, survey_id)
    return response

# ============================================
# CRUD for Pages
# ============================================

@SURVEY_MONKEY_BLUEPRINT.route("/create_page/<string:survey_id>", methods=["POST"])
def create_page(survey_id):
    """ Create a page in a survey """

    response = SurveyMonkeyView.create_page(request, survey_id)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/get_page_list/<string:survey_id>", methods=["GET"])
def get_page_list(survey_id):
    """ Get the list of pages in a survey """

    response = SurveyMonkeyView.get_page_list(request, survey_id)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/get_page/<string:survey_id>/<string:page_id>", methods=["GET"])
def get_page(survey_id, page_id):
    """ Get a page in a survey """

    response = SurveyMonkeyView.get_page(request, survey_id, page_id)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/update_page/<string:survey_id>/<string:page_id>", methods=["PUT"])
def update_page(survey_id, page_id):
    """ Update a page in a survey """

    response = SurveyMonkeyView.update_page(request, survey_id, page_id)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/delete_page/<string:survey_id>/<string:page_id>", methods=["DELETE"])
def delete_page(survey_id, page_id):
    """ Delete a page in a survey """

    response = SurveyMonkeyView.delete_page(request, survey_id, page_id)
    return response

# ============================================
# CRUD for Questions
# ============================================

@SURVEY_MONKEY_BLUEPRINT.route("/get_question_list/<string:survey_id>/<string:page_id>", methods=["GET"])
def get_question_list(survey_id, page_id):
    """ Get the list of questions in a page """

    response = SurveyMonkeyView.get_question_list(request, survey_id, page_id)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/create_question/<string:survey_id>/<string:page_id>", methods=["POST"])
def create_question(survey_id, page_id):
    """ Create a question in a page """

    response = SurveyMonkeyView.create_question(request, survey_id, page_id)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/get_question/<string:survey_id>/<string:page_id>/<string:question_id>", methods=["GET"])
def get_question(survey_id, page_id, question_id):
    """ Get a question in a page """

    response = SurveyMonkeyView.get_question(request, survey_id, page_id, question_id)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/update_question/<string:survey_id>/<string:page_id>/<string:question_id>", methods=["PUT"])
def update_question(survey_id, page_id, question_id):
    """ Update a question in a page """

    response = SurveyMonkeyView.update_question(request, survey_id, page_id, question_id)
    return response

@SURVEY_MONKEY_BLUEPRINT.route("/delete_question/<string:survey_id>/<string:page_id>/<string:question_id>", methods=["DELETE"])
def delete_question(survey_id, page_id, question_id):
    """ Delete a question in a page """

    response = SurveyMonkeyView.delete_question(request, survey_id, page_id, question_id)
    return response