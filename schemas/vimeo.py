from marshmallow import Schema, fields


class AddVimeoSchema(Schema):
    video_name = fields.String(required=True)