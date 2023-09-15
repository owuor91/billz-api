from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
import jwt

import app.settings
from app.base.models import save, get, set_model_dict, get_user_items


class BaseResource(Resource):
    schema = None
    model = None

    @jwt_required()
    def post(self):
        data = request.get_json()

        errors = self.schema.validate(data)
        if errors:
            return {"error": True, "errors": str(errors)}, 400

        user_id = self.get_user_id_from_token(request)
        data['created_by'] = user_id
        data['updated_by'] = user_id

        item = self.model(**data)
        try:
            save(item)
            return self.schema.dump(item), 201
        except Exception as e:
            return {"error": e.args}, 500

    @jwt_required()
    def get(self, pk=None):
        if pk:
            item = get(self.model, pk)
            if item is not None:
                return self.schema.dump(item), 200
        else:
            user_id = self.get_user_id_from_token(request)
            user_items = get_user_items(self.model, user_id)
            return self.schema.dump(user_items, many=True), 200
        return {"error": f"{self.model.__class__} not found"}, 404

    @jwt_required()
    def put(self, pk):
        item = get(self.model, pk)
        if item is not None:
            data = request.get_json()
            user_id = self.get_user_id_from_token(request)
            data['updated_by'] = user_id
            item = set_model_dict(item, data)
            try:
                save(item)
                return self.schema.dump(item), 200
            except Exception as e:
                return {"error": e.args}, 500
        return {"error": f"{self.model.__class__} not found"}, 404


    def get_user_id_from_token(self, request):
        token = request.headers.get("Authorization")
        token = token.split(' ')[1]
        secret = app.settings.JWT_SECRET_KEY
        decoded = jwt.decode(token, secret, algorithms=["HS256"])
        return decoded['sub']

