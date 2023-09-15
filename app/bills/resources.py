from app.bills.schemas import BillSchema, UpcomingBillSchema
from app.bills.model import Bill, UpcomingBill
from app.base.resource import BaseResource
class BillResource(BaseResource):
    model = Bill
    schema = BillSchema()


class UpcomingBillResource(BaseResource):
    model = UpcomingBill
    schema = UpcomingBillSchema()