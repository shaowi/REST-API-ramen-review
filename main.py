from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class RamenRatings(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	country = db.Column(db.String(50), nullable=False)
	brand = db.Column(db.String(50), nullable=False)
	type = db.Column(db.String(50), nullable=True)
	package = db.Column(db.String(50), nullable=True)
	rating = db.Column(db.Float, nullable=True)

	def __repr__(self):
		return f"Ramen(Country = {country}, Brand = {brand}, Type= {type}, Package = {package}, Rating = {rating})"

ramen_put_args = reqparse.RequestParser()
ramen_put_args.add_argument("country", type=str, help="Country of the ramen is required", required=True)
ramen_put_args.add_argument("brand", type=str, help="Brand of the ramen")
ramen_put_args.add_argument("type", type=str, help="Type of ramen")
ramen_put_args.add_argument("package", type=str, help="Packaging of the ramen")
ramen_put_args.add_argument("rating", type=float, help="Rating of the ramen")

ramen_update_args = reqparse.RequestParser()
ramen_update_args.add_argument("country", type=str, help="Country of the ramen")
ramen_update_args.add_argument("brand", type=str, help="Brand of the ramen")
ramen_update_args.add_argument("type", type=str, help="Type of ramen")
ramen_update_args.add_argument("package", type=str, help="Packaging of the ramen")
ramen_update_args.add_argument("rating",  type=float, help="Rating of the ramen")

resource_fields = {
	'id': fields.Integer,
	'country': fields.String,
	'brand': fields.String,
	'type': fields.String,
	'package': fields.String,
	'rating': fields.Float
}

def abort_if_ramen_id_doesnt_exist(ramen_id):
  result = RamenRatings.query.filter_by(id=ramen_id).first()
  if not result:
    abort(404, message="Could not find Ramen with that id")

class Ramen(Resource):

	@marshal_with(resource_fields)
	def get(self, ramen_id):
		result = RamenRatings.query.filter_by(id=ramen_id).first()
		if not result:
			abort(404, message="Could not find Ramen with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, ramen_id):
		args = ramen_put_args.parse_args()
		result = RamenRatings.query.filter_by(id=ramen_id).first()
		if result:
			abort(409, message="Ramen id is taken...")

		ramen = RamenRatings(id=ramen_id, country=args['country'], 
      brand=args['brand'], type=args['type'], package=args['package'], rating=args['rating'])
		db.session.add(ramen)
		db.session.commit()
		return ramen, 201


	@marshal_with(resource_fields)
	def patch(self, ramen_id):
		args = ramen_update_args.parse_args()
		result = RamenRatings.query.filter_by(id=ramen_id).first()
		if not result:
			abort(404, message="Ramen doesn't exist, cannot update")

		if args['country']:
			result.country = args['country']
		if args['brand']:
			result.brand = args['brand']
		if args['type']:
			result.type = args['type']
		if args['package']:
			result.package = args['package']
		if args['rating']:
			result.rating = args['rating']

		db.session.commit()

		return result

	def delete(self, ramen_id):
		abort_if_ramen_id_doesnt_exist(ramen_id)
		RamenRatings.query.filter_by(id=ramen_id).delete()
		db.session.commit()
		return '', 204

class Ramens(Resource):

	@marshal_with(resource_fields)
	def get(self):
		args = request.args
		print(args)
		country = args['country']
		search = args['search']
		if search:
			searchField = "%{}%".format(search)
			if searchField:
				result = RamenRatings.query.filter(
					RamenRatings.country.like(searchField) | 
					RamenRatings.brand.like(searchField) | 
					RamenRatings.type.like(searchField) |
					RamenRatings.package.like(searchField) | 
					RamenRatings.rating.like(searchField) 
					).all()
				if not result:
					abort(404, message="Could not find Ramen with search input")
				return result
		if country:
			result = RamenRatings.query.filter_by(country=country).all()
			if not result:
				abort(404, message="Could not find Ramen with that country")
			return result
		

api.add_resource(Ramen, "/ramen/<int:ramen_id>")
api.add_resource(Ramens, "/ramens")

if __name__ == "__main__":
	app.run(debug=True)