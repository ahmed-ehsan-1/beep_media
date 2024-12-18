from marshmallow import Schema, fields


class AddWistiaSchema(Schema):
    video_name = fields.String(required=True)

class UpdateWistiaSchema(Schema):
    video_name = fields.String(required=False)
    video_description = fields.String(required=False)