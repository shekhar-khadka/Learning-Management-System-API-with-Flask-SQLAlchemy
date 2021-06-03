from Database_model.app_model import Semester, SemesterSchema,db
from flask_restful import Resource
from flask import Flask, request, jsonify

semester_schema = SemesterSchema()
semesters_schema = SemesterSchema(many=True)


class SemesterInfo(Resource):
#########Post#########################
    def post(self):
        new_post = Semester(

            sem_name=request.json['sem_name'],
            p_id=request.json['p_id']

        )
        db.session.add(new_post)
        db.session.commit()
        return semester_schema.dump(new_post)

    def get(self):
        all_products = Semester.query.all()
        result = semesters_schema.dump(all_products)
        return jsonify(result)

class SemesterExtract(Resource):
    ########Get############
    def get(self, sem_id):
        extract = Semester.query.get_or_404(sem_id)
        return semester_schema.dump(extract)
    def delete(self, sem_id):
        del_rec = Semester.query.get_or_404(sem_id)
        db.session.delete(del_rec)
        db.session.commit()
        return '', 204

    def put(self, sem_id):
        change = Semester.query.get_or_404(sem_id)

        if 'p_name' in request.json:
            change.sem_name = request.json['sem_name']
        if 'p_id' in request.json:
            change.p_id=request.json['p_id']

        db.session.commit()
        return semester_schema.dump(change)
