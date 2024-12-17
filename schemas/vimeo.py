from marshmallow import Schema, fields


class AddVimeoSchema(Schema):
    video_name = fields.String(required=True)
    video_description = fields.String(required=False)

class UpdateVimeoSchema(Schema):
    video_name = fields.String(required=False)
    video_description = fields.String(required=False)