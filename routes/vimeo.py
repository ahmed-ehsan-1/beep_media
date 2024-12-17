from flask import Blueprint, request
from flask_restful import Api
from views import VimeoView

VIMEO_BLUEPRINT = Blueprint("vimeo", __name__, url_prefix="/vimeo")

@VIMEO_BLUEPRINT.route("/", methods=["POST"])
def add_video():
    """ Add a video to the vimeo """

    response = VimeoView.upload_video(request)
    return response

@VIMEO_BLUEPRINT.route("/<string:video_id>", methods=["GET"])
def get_video_data(video_id):
    """ Get the data of a video """

    response = VimeoView.get_video_data(request, video_id)
    return response

@VIMEO_BLUEPRINT.route("/<string:video_id>", methods=["PUT"])
def update_video_data(video_id):
    """ Update the data of a video """

    response = VimeoView.update_video_data(request, video_id)
    return response

@VIMEO_BLUEPRINT.route("/<string:video_id>", methods=["DELETE"])
def delete_video(video_id):
    """ Delete a video from vimeo """

    response = VimeoView.delete_video(request, video_id)
    return response
