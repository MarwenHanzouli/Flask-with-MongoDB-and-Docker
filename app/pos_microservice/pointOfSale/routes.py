from pos_microservice import app, bcrypt
from flask import request, jsonify, Blueprint
from flask_marshmallow import Marshmallow
from pos_microservice.pointOfSale.models import PointOfSale


# Init bluebripnt
pos = Blueprint('pos', __name__)

# Init marshmallow
ma = Marshmallow(pos)


# PointOfSaleClass schema
class PointOfSaleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('designation', 'localisation', 'address', 'email', 'phone_number')


# Init schema
pointOfSale_schema = PointOfSaleSchema()
pointsOfSale_schema = PointOfSaleSchema(many=True)


# Get all points of sales
@pos.route('/pointsOfSale', methods=['GET'])
def get_points_of_Sale():
    all_point_of_sales = PointOfSale.query.all()
    result = pointsOfSale_schema.dump(all_point_of_sales)
    return jsonify(result.data)


# Complete your routes here
