from flask import Config, Request
from flask_restful.reqparse import Argument
from marshmallow import ValidationError
from schemas.wistia import AddWistiaSchema, UpdateWistiaSchema
from util.enums import Status
from util.response import Response
import requests
import config


def upload_video(request: Request):
    try:
        payload = request.get_json()
        wistia_add_video_schema = AddWistiaSchema()
        payload = wistia_add_video_schema.load(payload)

        video_file_path = "test_video.mp4"

        # Here I want to upload video to wistia
        wistia_api_token = config.WISTIA_API_TOKEN
        wistia_url = "https://upload.wistia.com"

        with open(video_file_path, "rb") as video_file:
            response = requests.post(
                wistia_url,
                headers={
                    # "Content-Type": "application/x-www-form-urlencoded",
                    "Authorization": f"Bearer {wistia_api_token}",
                },
                files={"file": video_file},
                data={"name": payload["video_name"]},
            )

        if response.status_code != 200:
            raise Exception("Failed to upload video to Wistia")

        response_data = response.json()

        return Response(
            "Video uploaded successfully", Status.HTTP_201_CREATED, response_data, None
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()

    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def get_video_data(request: Request, video_id: str):
    try:
       
        wistia_api_token = config.WISTIA_API_TOKEN
        wistia_url = f"https://api.wistia.com/v1/medias/{video_id}.json"

        response = requests.get(
            wistia_url,
            headers={
            "Authorization": f"Bearer {wistia_api_token}",
            },
        )

        if response.status_code != 200:
            raise Exception("Failed to retrieve video data from Wistia")

        response_data = response.json()

        return Response(
            "Video data retrieved successfully",
            Status.HTTP_200_OK,
            response_data,
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def update_video_data(request: Request, video_id: str):
    try:
        payload = request.get_json()
        wistia_update_video_schema = UpdateWistiaSchema()
        payload = wistia_update_video_schema.load(payload)

        wistia_api_token = config.WISTIA_API_TOKEN
        wistia_url = f"https://api.wistia.com/v1/medias/{video_id}.json"

        update_data = {}
        if "video_name" in payload:
            update_data["name"] = payload["video_name"]
        if "video_description" in payload:
            update_data["description"] = payload["video_description"]

        response = requests.put(
            wistia_url,
            headers={
            "Authorization": f"Bearer {wistia_api_token}",
            "Content-Type": "application/json",
            },
            json=update_data,
        )

        if response.status_code != 200:
            raise Exception("Failed to update video data on Wistia")

        payload = response.json()

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
        wistia_api_token = config.WISTIA_API_TOKEN
        wistia_url = f"https://api.wistia.com/v1/medias/{video_id}.json"

        response = requests.delete(
            wistia_url,
            headers={
                "Authorization": f"Bearer {wistia_api_token}",
            },
        )

        if response.status_code != 200:
            raise Exception("Failed to delete video from Wistia")

        return Response(
            "Video deleted successfully", Status.HTTP_200_OK, None, None
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()

    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()

