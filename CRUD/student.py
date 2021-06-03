from Database_model.app_model import Student, StudentSchema,db
from flask_restful import Resource
from flask import Flask, request, jsonify

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

class StudentInfo(Resource):

    def post(self):
        new_post = Student(

            s_name=request.json['s_name'],
            section=request.json['section'],
            address=request.json['address'],
            contact=request.json['contact'],
            p_id=request.json['p_id'],
            sem_id=request.json['sem_id']
        )
        db.session.add(new_post)
        db.session.commit()

        return student_schema.dump(new_post)

    def get(self):
        all_Student = Student.query.all()
        result = students_schema.dump(all_Student)
        return jsonify(result)


class StudentExtract(Resource):
    ########Get############
    def get(self, s_id):
        extract = Student.query.get_or_404(s_id)
        return student_schema.dump(extract)

    def delete(self, s_id):
        del_rec = Student.query.get_or_404(s_id)
        db.session.delete(del_rec)
        db.session.commit()
        return 'deleted', 204

    def put(self, s_id):
        change = Student.query.get_or_404(s_id)

        if 's_name' in request.json:
            change.s_name = request.json['s_name']
        if 'section' in request.json:
            change.section = request.json['section']
        if 'address' in request.json:
            change.address = request.json['address']
        if 'contact' in request.json:
            change.contact = request.json['contact']
        if 'sem_id' in request.json:
            change.sem_id = request.json['sem_id']
        if 'p_id' in request.json:
            change.p_id = request.json['p_id']

        db.session.commit()
        return student_schema.dump(change)





