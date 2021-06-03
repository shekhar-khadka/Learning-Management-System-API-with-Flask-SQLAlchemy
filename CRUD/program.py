from Database_model.app_model import Program, ProgramSchema,db
from flask_restful import Resource
from flask import Flask, request, jsonify



#*********************************************************************************************#
#------------------ ProgramCURD----------------------------------------------------------------#
#*********************************************************************************************#

program_schema = ProgramSchema()
programs_schema=ProgramSchema(many=True)

class ProgramInfo(Resource):
#########Post_Program#########################
    def post(self):
        new_post = Program(
            p_name=request.json['p_name']

        )
        db.session.add(new_post)
        db.session.commit()
        return program_schema.dump(new_post)

    def get(self):
        all_products = Program.query.all()
        result = programs_schema.dump(all_products)
        return jsonify(result)


class ProgramExtract(Resource):
    ########Get_Program############
    def get(self, p_id):
        extract = Program.query.get_or_404(p_id)
        return program_schema.dump(extract)

    def delete(self, p_id):
        del_rec = Program.query.get_or_404(p_id)
        db.session.delete(del_rec)
        db.session.commit()
        return '', 204

    def put(self, p_id):
        change = Program.query.get_or_404(p_id)

        if 'p_name' in request.json:
            change.p_name = request.json['p_name']


        db.session.commit()
        return program_schema.dump(change)
