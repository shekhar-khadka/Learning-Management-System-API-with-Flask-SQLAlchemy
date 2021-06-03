from Database_model.app_model import Instructor, InstructorSchema,db
from flask_restful import Resource
from flask import Flask, request, jsonify

instructor_schema=InstructorSchema()
instructors_schema=InstructorSchema(many=True)

class InstructorInfo(Resource):

  def post(self):
    new_post = Instructor(

      ins_name=request.json['ins_name'],
      contact=request.json['contact'],
      p_id=request.json['p_id']
    )
    db.session.add(new_post)
    db.session.commit()

    return instructor_schema.dump(new_post)

  def get(self):
    all_instructors = Instructor.query.all()
    result = instructors_schema.dump(all_instructors)
    return jsonify(result)


class InstructorExtract(Resource):
  ########Get############
  def get(self, ins_id):
    extract = Instructor.query.get_or_404(ins_id)
    return instructor_schema.dump(extract)

  def delete(self, ins_id):
    del_rec = Instructor.query.get_or_404(ins_id)
    db.session.delete(del_rec)
    db.session.commit()
    return 'deleted', 204

  def put(self, ins_id):
    change = Instructor.query.get_or_404(ins_id)

    if 'ins_name' in request.json:
      change.ins_name = request.json['ins_name']
    if 'contact' in request.json:
      change.contact = request.json['contact']
    if 'p_id' in request.json:
      change.p_id = request.json['p_id']

    db.session.commit()
    return instructor_schema.dump(change)
