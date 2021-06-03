from Database_model.app_model import Course,CourseSchema,db
from flask_restful import Resource
from flask import Flask, request, jsonify


course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

class CourseInfo(Resource):

    def post(self):
        new_post = Course(

            c_name=request.json['c_name'],
            c_hour=request.json['c_hour'],
            ins_id=request.json['ins_id'],
            sem_id=request.json['sem_id']
        )
        db.session.add(new_post)
        db.session.commit()

        return course_schema.dump(new_post)

    def get(self):
        all_course = Course.query.all()
        result = courses_schema.dump(all_course)
        return jsonify(result)


class CourseExtract(Resource):
    ########Get############
    def get(self, c_id):
        extract = Course.query.get_or_404(c_id)
        return course_schema.dump(extract)

    def delete(self, c_id):
        del_rec = Course.query.get_or_404(c_id)
        db.session.delete(del_rec)
        db.session.commit()
        return 'deleted', 204

    def put(self, c_id):
        change = Course.query.get_or_404(c_id)

        if 'c_name' in request.json:
            change.c_name = request.json['c_name']
        if 'c_hour' in request.json:
            change.c_hour = request.json['c_hour']
        if 'sem_id' in request.json:
            change.sem_id = request.json['sem_id']
        if 'ins_id' in request.json:
            change.ins_id = request.json['ins_id']

        db.session.commit()
        return course_schema.dump(change)

