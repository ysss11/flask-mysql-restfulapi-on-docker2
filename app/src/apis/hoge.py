from datetime import datetime

from flask_restful import Resource, reqparse, abort

from flask import jsonify

from src.models.hoge import HogeModel, HogeSchema


class HogeListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', required=True)
        self.reqparse.add_argument('state', required=True)
        super(HogeListAPI, self).__init__()

    def get(self):
        results = HogeModel.select().order_by(HogeModel.createTime.asc())
        print('HogeListAPI get:', HogeSchema(many=True).dump(results))
        jsonData = HogeSchema(many=True).dump(results)
        return jsonify({'items': jsonData})

    def post(self):
        args = self.reqparse.parse_args()
        hoge = HogeModel.create(name=args['name'], state=args['state'])
        print('HogeListAPI post', HogeSchema().dump(hoge))
        res = HogeSchema().dump(hoge)
        return res, 201


class HogeAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name')
        self.reqparse.add_argument('state')
        super(HogeAPI, self).__init__()

    def get(self, id):
        hoge = HogeModel.select().where(HogeModel.id==id).first()
        if hoge is None:
            abort(404)

        print('HogeAPI get:', HogeSchema().dump(hoge))
        res = HogeSchema().dump(hoge)
        return res

    def put(self, id):
        hoge = HogeModel.select().where(HogeModel.id==id).first()
        if hoge is None:
            abort(404)
        args = self.reqparse.parse_args()
        for name, value in args.items():
            if value is not None:
                setattr(hoge, name, value)

        # save前にupdateTimeを現在時刻で更新する
        hoge.updateTime = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        hoge.save()
        return None, 204

    def delete(self, id):
        hoge = HogeModel.select().where(HogeModel.id==id).first()
        if hoge is not None:
            hoge.delete_instance()
        return None, 204
