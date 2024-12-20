from marshmallow import Schema, fields
from marshmallow_enum import EnumField
import enum

class GetAuthTokenSchema(Schema):
    code = fields.String(required=True)
    
class CreateSurveySchema(Schema):
    title = fields.String(required=True)

class CreatePageSchema(Schema):
    title = fields.String(required=False)
    description = fields.String(required=False)
    position = fields.Integer(required=False)

class QuestionFamily(enum.Enum):
    SINGLE_CHOICE = "single_choice"
    MULTIPLE_CHOICE = "multiple_choice"
    OPEN_ENDED = "open_ended"

class CreateQuestionSchema(Schema):
    heading = fields.String(required=True)
    choices = fields.List(fields.String(), missing=[])
    family = EnumField(QuestionFamily, by_value=True, missing=QuestionFamily.OPEN_ENDED)

