from flask import Blueprint, request
from flask_restful import Api
from views import WistiaView

WISTIA_BLUEPRINT = Blueprint("wistia", __name__, url_prefix="/wistia")

@WISTIA_BLUEPRINT.route("/", methods=["POST"])
def add_video():
    """ Add a video to the wistia """

    response = WistiaView.upload_video(request)
    return response

@WISTIA_BLUEPRINT.route("/<string:video_id>", methods=["GET"])
def get_video_data(video_id):
    """ Get the data of a video """

    response = WistiaView.get_video_data(request, video_id)
    return response

@WISTIA_BLUEPRINT.route("/<string:video_id>", methods=["PUT"])
def update_video_data(video_id):
    """ Update the data of a video """

    response = WistiaView.update_video_data(request, video_id)
    return response

@WISTIA_BLUEPRINT.route("/<string:video_id>", methods=["DELETE"])
def delete_video(video_id):
    """ Delete a video from wistia """

    response = WistiaView.delete_video(request, video_id)
    return response
