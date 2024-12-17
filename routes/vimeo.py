from flask import Blueprint, request
from flask_restful import Api
from views import VimeoView

VIMEO_BLUEPRINT = Blueprint("vimeo", __name__, url_prefix="/vimeo")

@VIMEO_BLUEPRINT.route("/add", methods=["POST"])
def add_video():
    """ Add a video to the vimeo """

    response = VimeoView.upload_video(request)
    return response