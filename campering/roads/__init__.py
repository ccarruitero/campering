from flask import Blueprint, jsonify
from campering.roads.models import Road

roads_app = Blueprint('roads',__name__,template_folder='templates')

@roads_app.route('/', methods = ['GET'])
def get_roads():
    roads = Road.query.all()
    return jsonify(roads)

@roads_app.route('/<roadid>', methods = ['GET'])
def get_road(road_id):
    road = Road.query.filter_by(id=road_id).first()
    if road is not None:
        return road
    return "we can't found this road, please check if `id` is correct"

#@app.route('/new', methods= ['POST'])
#@app.route('/<roadid>', methods= ['PUT'])
#@app.route('/<roadid>', methods= ['DELETE'])
