from marshmallow import fields, Schema


class UserSchema(Schema):
    user_id = fields.UUID(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    phone_number = fields.String(required=True)
    password = fields.String(required=True)
