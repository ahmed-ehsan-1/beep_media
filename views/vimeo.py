from flask import Config, Request
from flask_restful.reqparse import Argument
from marshmallow import ValidationError
from schemas.vimeo import AddVimeoSchema, UpdateVimeoSchema
from util.enums import Status
from util.response import Response
import vimeo
import config


def upload_video(request: Request):
    try:
        payload = request.get_json()
        vimeo_add_video_schema = AddVimeoSchema()
        payload = vimeo_add_video_schema.load(payload)

        video_file_path = "test_video.mp4"

        # upload the video to the vimeo
        client = vimeo.VimeoClient(
            token=config.VIMEO_ACCESS_TOKEN,
            key=config.VIMEO_CLIENT_ID,
            secret=config.VIMEO_CLIENT_SECRET,
        )

        uri = client.upload(
            video_file_path,
            data={
                "name": payload["video_name"],
                "description": (
                    payload["video_description"]
                    if "video_description" in payload
                    else None
                ),
            },
        )

        payload["vimeo_video_id"] = uri

        return Response(
            "Video uploaded successfully", Status.HTTP_200_OK, payload, None
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()

    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()

def get_video_data(request: Request, video_id: str):
    try:
        client = vimeo.VimeoClient(
            token=config.VIMEO_ACCESS_TOKEN,
            key=config.VIMEO_CLIENT_ID,
            secret=config.VIMEO_CLIENT_SECRET,
        )

        video_uri = "/videos/" + video_id
        response = client.get(video_uri)

        return Response(
            "Video data retrieved successfully", Status.HTTP_200_OK, response.json(), None
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def update_video_data(request: Request, video_id: str):
    try:
        payload = request.get_json()
        vimeo_add_video_schema = UpdateVimeoSchema()
        payload = vimeo_add_video_schema.load(payload)

        client = vimeo.VimeoClient(
            token=config.VIMEO_ACCESS_TOKEN,
            key=config.VIMEO_CLIENT_ID,
            secret=config.VIMEO_CLIENT_SECRET,
        )

        # update the video data
        video_data = {}

        if "video_name" in payload:
            video_data["name"] = payload["video_name"]
        if "video_description" in payload:
            video_data["description"] = payload["video_description"]


        video_uri = "/videos/" + video_id
        response = client.patch(video_uri, data=video_data)
        
        return Response(
            "Video data updated successfully", Status.HTTP_200_OK, payload, None
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def delete_video(request: Request, video_id: str):
    try:

        client = vimeo.VimeoClient(
            token=config.VIMEO_ACCESS_TOKEN,
            key=config.VIMEO_CLIENT_ID,
            secret=config.VIMEO_CLIENT_SECRET,
        )

        # delete the video from the vimeo
        client.delete(video_id)

        return Response(
            "Video deleted successfully", Status.HTTP_200_OK, None, None
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()

    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()