from app.bills.schemas import BillSchema, UpcomingBillSchema
from app.bills.model import Bill, UpcomingBill
from app.base.resource import BaseResource
from flask import request
from db import db
from flask_jwt_extended import jwt_required
class BillResource(BaseResource):
    model = Bill
    schema = BillSchema()


class UpcomingBillResource(BaseResource):
    model = UpcomingBill
    schema = UpcomingBillSchema()

    @jwt_required()
    def post(self):
        session = db.session
        data = request.get_json()
        upcoming = UpcomingBill(**data)
        existing = session.query(UpcomingBill).get(upcoming.upcoming_bill_id)
        if existing is None:
            return super().post()
        else:
            return super().put(upcoming.upcoming_bill_id)