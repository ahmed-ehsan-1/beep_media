from flask import Config, Request
from flask_restful.reqparse import Argument
from marshmallow import ValidationError
from schemas.vimeo import AddVimeoSchema
from util.enums import Status
from util.response import Response
import vimeo
import config

def upload_video(request: Request):
    try:
        payload = request.get_json()
        vimeo_add_video_schema = AddVimeoSchema()
        payload = vimeo_add_video_schema.load(payload)

        # get the video file from the root directory present with name "test_video"
        video_file_path = "test_video.mp4"
        
        # upload the video to the vimeo
        client = vimeo.VimeoClient(
            token=config.VIMEO_ACCESS_TOKEN,
            key=config.VIMEO_CLIENT_ID,
            secret=config.VIMEO_CLIENT_SECRET
        )

        print(client)
        
        with open(video_file_path, 'rb') as video_file:
            response = client.upload(video_file, data={
                'name': payload['video_name']
            })
        
        payload['vimeo_video_id'] = response

        return Response("Video uploaded successfully", Status.HTTP_200_OK, payload, None).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()

    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()