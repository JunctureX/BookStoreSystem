from flask_restful import Resource, reqparse
from app.service.order_service import (
    get_all_orders, get_order_by_id, create_order, update_order, delete_order
)
from sqlalchemy.exc import IntegrityError

class OrderList(Resource):
    def get(self):
        orders = get_all_orders()
        return [{"id": order.id, "user_id": order.user_id} for order in orders]

class OrderDetail(Resource):
    def get(self, order_id):
        order = get_order_by_id(order_id)
        if order:
            return {
                "id": order.id,
                "user_id": order.user_id,
                "total_amount": order.total_amount,
                "status": order.status
            }
        return {"message": "Order not found"}, 404

    def put(self, order_id):
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", type=int)
        parser.add_argument("shipping_address", type=str)
        parser.add_argument("payment_method", type=str)
        parser.add_argument("status", type=str)
        parser.add_argument("order_items", type=list, location="json")
        data = parser.parse_args()
        updated_order = update_order(order_id, data)
        if updated_order:
            return {"id": updated_order.id, "user_id": updated_order.user_id}
        return {"message": "Failed to update order"}, 400

    def delete(self, order_id):
        if delete_order(order_id):
            return {"message": "Order deleted successfully"}, 200
        return {"message": "Failed to delete order"}, 400


class CreateOrder(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", type=int, required=True)
        parser.add_argument("shipping_address", type=str, required=True)
        parser.add_argument("payment_method", type=str, required=True)
        parser.add_argument("order_items", type=list, location="json", required=True)
        data = parser.parse_args()
        print('createorder: ',data)
        try:
            new_order = create_order(data)
            return {"message": "Order created successfully", "order_id": new_order.id}, 201
        except IntegrityError as e:
            return {"message": "Failed to create order: {}".format(str(e))}, 400

