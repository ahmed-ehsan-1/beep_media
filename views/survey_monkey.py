import urllib.parse
from flask import Request
from marshmallow import ValidationError
import requests
import os
import urllib

from util.enums import Status
from util.response import Response

from schemas.survey_monkey import (
    CreatePageSchema,
    CreateQuestionSchema,
    CreateSurveySchema,
    GetAuthTokenSchema,
    QuestionFamily,
)
import config


SM_API_BASE = "https://api.surveymonkey.com"


# ==================
# Useful Links
# ==================

# Survey Monkey Application
# https://www.surveymonkey.com/


# Survey Monkey API Documentation
# https://developer.surveymonkey.com/api/v3/

# Survey Monkey Developer Portal
# https://developer.surveymonkey.com/apps/


# ==================

# ============================================
# Authentication
# ============================================


def get_oauth_url(request) -> str:
    try:
        AUTH_CODE_ENDPOINT = "/oauth/authorize"

        url_params = {
            "redirect_uri": config.SURVEY_MONKEY_REDIRECT_URI,
            "client_id": config.SURVEY_MONKEY_CLIENT_ID,
            "response_type": "code",
        }

        auth_dialog_uri = (
            SM_API_BASE + AUTH_CODE_ENDPOINT + "?" + urllib.parse.urlencode(url_params)
        )

        return Response(
            "OAuth URL generated successfully",
            Status.HTTP_201_CREATED,
            {"uri": auth_dialog_uri},
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()

    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def exchange_code_for_token(request: Request) -> str:
    try:

        payload = request.get_json()
        auth_token_schema = GetAuthTokenSchema()
        payload = auth_token_schema.load(payload)

        ACCESS_TOKEN_ENDPOINT = "/oauth/token"

        data = {
            "client_secret": config.SURVEY_MONKEY_CLIENT_SECRET,
            "code": payload["code"],
            "redirect_uri": config.SURVEY_MONKEY_REDIRECT_URI,
            "client_id": config.SURVEY_MONKEY_CLIENT_ID,
            "grant_type": "authorization_code",
        }

        access_token_uri = SM_API_BASE + ACCESS_TOKEN_ENDPOINT
        access_token_response = requests.post(access_token_uri, data=data)
        access_json = access_token_response.json()

        return Response(
            "Token retrieved successfully", Status.HTTP_201_CREATED, access_json, None
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()

    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


# ============================================
# CRUD for Surveys
# ============================================


def get_survey_list(request: Request) -> str:
    try:

        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = SM_API_BASE + "/v3/surveys"
        response = requests.get(url, headers=headers)
        response_json = response.json()

        return Response(
            "Survey list retrieved successfully",
            Status.HTTP_200_OK,
            response_json,
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()

    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def get_survey_details(request: Request, survey_id: str) -> str:
    try:

        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = SM_API_BASE + "/v3/surveys/" + survey_id
        response = requests.get(url, headers=headers)
        response_json = response.json()

        return Response(
            "Survey details retrieved successfully",
            Status.HTTP_200_OK,
            response_json,
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()

    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def create_survey(request: Request) -> str:
    try:
        payload = request.get_json()
        create_survey_schema = CreateSurveySchema()
        payload = create_survey_schema.load(payload)

        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = SM_API_BASE + "/v3/surveys"
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code != 201:
            raise Exception(response.json()[0])

        return Response(
            "Survey created successfully",
            Status.HTTP_201_CREATED,
            response.json(),
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def update_survey(request: Request, survey_id: str):
    try:
        payload = request.get_json()
        create_survey_schema = CreateSurveySchema()
        payload = create_survey_schema.load(payload)

        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = SM_API_BASE + "/v3/surveys/" + survey_id
        response = requests.put(url, headers=headers, json=payload)
        print("response: ", response.json())

        if response.status_code != 200:
            raise Exception(response.json()[0])

        return Response(
            "Survey updated successfully",
            Status.HTTP_200_OK,
            response.json(),
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def delete_survey(request: Request, survey_id: str):
    try:
        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = SM_API_BASE + "/v3/surveys/" + survey_id
        response = requests.delete(url, headers=headers)

        return Response(
            "Survey deleted successfully",
            Status.HTTP_200_OK,
            None,
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


# ============================================
# CRUD for Pages
# ============================================


def create_page(request: Request, survey_id: str) -> str:
    try:
        payload = request.get_json()
        create_page_schema = CreatePageSchema()
        payload = create_page_schema.load(payload)

        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = SM_API_BASE + "/v3/surveys/" + survey_id + "/pages"
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code != 201:
            raise Exception(response.json()[0])

        return Response(
            "Page created successfully",
            Status.HTTP_201_CREATED,
            response.json(),
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def get_page_list(request: Request, survey_id: str) -> str:
    try:
        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = SM_API_BASE + "/v3/surveys/" + survey_id + "/pages"
        response = requests.get(url, headers=headers)

        return Response(
            "Pages retrieved successfully",
            Status.HTTP_200_OK,
            response.json(),
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def get_page(request: Request, survey_id: str, page_id: str) -> str:
    try:
        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = SM_API_BASE + "/v3/surveys/" + survey_id + "/pages/" + page_id
        response = requests.get(url, headers=headers)

        return Response(
            "Page retrieved successfully",
            Status.HTTP_200_OK,
            response.json(),
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def update_page(request: Request, survey_id: str, page_id: str) -> str:
    try:
        payload = request.get_json()
        create_page_schema = CreatePageSchema()
        payload = create_page_schema.load(payload)

        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = SM_API_BASE + "/v3/surveys/" + survey_id + "/pages/" + page_id
        response = requests.put(url, headers=headers, json=payload)
        print("response: ", response.json())

        if response.status_code != 200:
            raise Exception(response.json()[0])

        return Response(
            "Page updated successfully",
            Status.HTTP_200_OK,
            response.json(),
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def delete_page(request: Request, survey_id: str, page_id: str) -> str:
    try:
        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = SM_API_BASE + "/v3/surveys/" + survey_id + "/pages/" + page_id
        response = requests.delete(url, headers=headers)

        return Response(
            "Page deleted successfully",
            Status.HTTP_200_OK,
            None,
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


# ============================================
# CRUD for Questions
# ============================================


def get_question_list(request: Request, survey_id: str, page_id: str):
    try:
        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = (
            SM_API_BASE
            + "/v3/surveys/"
            + survey_id
            + "/pages/"
            + page_id
            + "/questions"
        )

        response = requests.get(url, headers=headers)

        return Response(
            "Questions retrieved successfully",
            Status.HTTP_200_OK,
            response.json(),
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def create_question(request: Request, survey_id: str, page_id: str):
    try:
        payload = request.get_json()
        create_question_schema = CreateQuestionSchema()
        payload = create_question_schema.load(payload)

        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        request_payload = {
            "headings": [
                {
                    "heading": payload["heading"],
                }
            ],
            "position": 0,
            "family": payload["family"].value,
            "subtype": (
                "single"
                if payload["family"] == QuestionFamily.OPEN_ENDED
                else "vertical"
            ),
            "required": None,
            "answers": (
                {"choices": [{"text": choice} for choice in payload["choices"]]}
                if payload["family"] != QuestionFamily.OPEN_ENDED
                else None
            ),
        }

        print("Payload: ", request_payload)

        url = (
            SM_API_BASE
            + "/v3/surveys/"
            + survey_id
            + "/pages/"
            + page_id
            + "/questions"
        )
        response = requests.post(url, headers=headers, json=request_payload)
        print("response: ", response.json())

        if response.status_code != 201:
            raise Exception(response.json()[0])

        return Response(
            "Question created successfully",
            Status.HTTP_201_CREATED,
            response.json(),
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def get_question(request: Request, survey_id: str, page_id: str, question_id: str):
    try:
        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = (
            SM_API_BASE
            + "/v3/surveys/"
            + survey_id
            + "/pages/"
            + page_id
            + "/questions/"
            + question_id
        )

        response = requests.get(url, headers=headers)
        response_json = response.json()

        return Response(
            "Question retrieved successfully",
            Status.HTTP_200_OK,
            response_json,
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def update_question(request: Request, survey_id: str, page_id: str, question_id: str):
    try:
        payload = request.get_json()
        create_question_schema = CreateQuestionSchema()
        payload = create_question_schema.load(payload)

        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        request_payload = {
            "headings": [
                {
                    "heading": payload["heading"],
                }
            ],
            "position": 0,
            "family": payload["family"].value,
            "subtype": (
                "single"
                if payload["family"] == QuestionFamily.OPEN_ENDED
                else "vertical"
            ),
            "required": None,
            "answers": (
                {"choices": [{"text": choice} for choice in payload["choices"]]}
                if payload["family"] != QuestionFamily.OPEN_ENDED
                else None
            ),
        }

        print("Payload: ", request_payload)

        url = (
            SM_API_BASE
            + "/v3/surveys/"
            + survey_id
            + "/pages/"
            + page_id
            + "/questions/"
            + question_id
        )
        response = requests.put(url, headers=headers, json=request_payload)
        print("response: ", response.json())

        if response.status_code != 200:
            raise Exception(response.json()[0])

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()


def delete_question(request: Request, survey_id: str, page_id: str, question_id: str):
    try:
        headers = {
            "Authorization": "Bearer " + config.SURVEY_MONKEY_ACCESS_TOKEN,
            "Content-Type": "application/json",
        }

        url = (
            SM_API_BASE
            + "/v3/surveys/"
            + survey_id
            + "/pages/"
            + page_id
            + "/questions/"
            + question_id
        )

        response = requests.delete(url, headers=headers)

        return Response(
            "Question deleted successfully",
            Status.HTTP_200_OK,
            None,
            None,
        ).to_json()

    except ValidationError as e:
        return Response(e, Status.HTTP_400_BAD_REQUEST, None, e.messages).to_json()
    except Exception as e:
        print("Error: ", e)
        return Response(e, Status.HTTP_500_INTERNAL_SERVER_ERROR, None, None).to_json()
