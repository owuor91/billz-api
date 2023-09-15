from marshmallow import fields, Schema
from marshmallow_enum import EnumField
from app.enums import FrequencyEnum

class BillSchema(Schema):
    bill_id = fields.UUID(required=True)
    name = fields.String(required=True)
    amount = fields.Float(required=True)
    frequency = EnumField(FrequencyEnum)
    due_date = fields.String(required=True)
    user_id = fields.UUID(required=True)


class UpcomingBillSchema(Schema):
    upcoming_bill_id = fields.UUID(required=True)
    bill_id = fields.UUID(required=True)
    name = fields.String(required=True)
    amount = fields.Float(required=True)
    frequency = EnumField(FrequencyEnum)
    due_date = fields.Date(required=True)
    user_id = fields.UUID(required=True)
    paid = fields.Boolean(required=True)