#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from flask_cors import CORS, cross_origin


@app.route('/add', methods=['POST'])
@cross_origin()
def add_garden():
    _json = request.json
    _access_code = _json['access_code']

    # validate the received values

    if _access_code and request.method == 'POST':

        # do not save password as a plain text
        # save details

        id = mongo.db.gardens.insert({'access_code': _access_code,
                                      'plants': 0, 'carbon_offset': 0})
        resp = jsonify('Garden added successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()


@app.route('/gardens/<access_code>')
@cross_origin()
def get_garden(access_code):
    user = mongo.db.gardens.find_one({'access_code': access_code})
    resp = dumps(user)
    return resp


@app.route('/update_plants', methods=['PUT'])
@cross_origin()
def update_plants():
    _json = request.json
    _access_code = _json['access_code']
    _plants = int(_json['plants'])

    # validate the received values

    if _access_code and _plants and request.method == 'PUT':
        mongo.db.gardens.update_one(
            {'access_code': _access_code},
            [
                {"$project": {'access_code': 1, 'carbon_offset': 1, 'plants': {
                    "$add": ["$plants", _plants]}}}
            ]
        )
        resp = jsonify('Garden updated successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()


@app.errorhandler(404)
@cross_origin()
def not_found(error=None):
    message = {'status': 404, 'message': 'Not Found: ' + request.url}
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run()
