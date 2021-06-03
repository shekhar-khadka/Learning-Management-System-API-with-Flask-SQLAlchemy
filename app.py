from flask import Flask, request, jsonify
from CRUD.program import ProgramInfo,ProgramExtract
from CRUD.instructor import InstructorInfo,InstructorExtract
from CRUD.student import StudentInfo,StudentExtract
from CRUD.semester import SemesterInfo,SemesterExtract
from CRUD.course import CourseInfo,CourseExtract
from flask_restful import Api, Resource
from Database_model.app_model import *
from sqlalchemy import distinct, func


api=Api(app)

#-------------------studentCount--------------#
@app.route('/sc',methods=['GET'])
def std_count():
    counts=db.session.query(func.count(Student.s_id))
    for i in counts:
        result=i[0]
    result={"Total Number of students is":result}
    return jsonify(result)



#-------------------No.Of.std.in.each.semester.by.program--------
@app.route('/StdSem/<string:prg_name>',methods=['GET'])
def std_by_program(prg_name):
    results = db.session.query(Semester.sem_name,func.count(Semester.sem_name)). \
     select_from(Program).join(Semester).join(Student).group_by(Semester.sem_name).filter(Program.p_name==prg_name).all()
    buffer=[]
    for i in results:
        x = {"Semester ": i[0], "Student_Number ": i[1]}
        buffer.append(x)
    return jsonify(buffer)

#--------------FindingCourse------------------
@app.route('/CourseFind/<string:prg_name>',methods=['GET'])
def find_course(prg_name):
    result = db.session.query(Semester.sem_name, Course.c_name). \
        select_from(Program).join(Semester).join(Course).filter(Program.p_name == prg_name).order_by(Semester.sem_name)
    buffer = []
    for i in result:
        x = {"semester ": i[0], "Course ": i[1]}
        buffer.append(x)
    return jsonify(buffer)


# #-------------------    SectionInEachSemester--------
# @app.route('/SectionFind/<string:prg_name>',methods=['GET'])
# def Find_Section(prg_name):
#     results = db.session.query(Semester.sem_name,Student.section). \
#      select_from(Program).join(Semester).join(Student).filter(Program.p_name==prg_name).order_by(Semester.sem_name)
#     buffer=[]
#     for i in results:
#         x = {"Semester ": i[0], "Section ": i[1]}
#         buffer.append(x)
#     return jsonify(buffer)

#------------------------------StudentCountByProgram-------------------
@app.route('/StdCBPrg',methods=['GET'])
def StdCountByProgram():
    result = db.session.query(Program.p_name, func.count(Student.s_id)).join(Student).group_by(Program.p_name)

    buffer = []

    for i in result:
        x = {"program ": i[0], "Total_students ": i[1]}
        buffer.append(x)
    return jsonify(buffer)



#*********************************************************************************************#
#------------------ StudentCountBySection----------------------------------------------------------------#
#*********************************************************************************************#

@app.route('/stdCBSec/<string:prg_name>',methods=['GET'])
def StdCountBySection(prg_name):
    result = db.session.query(Semester.sem_name, Student.section, func.count(Student.s_id)). \
        select_from(Program).join(Semester).join(Student).group_by(Semester.sem_name, Student.section).filter(
        Program.p_name ==prg_name).all()

    print(result)
    buffer = []

    for i in result:
        x = {"semester ": i[0], "Section ": i[1], "Total_Students ": i[2]}
        buffer.append(x)

    return jsonify(buffer)

#*********************************************************************************************#
#------------------Instructor List In Each Sem By Program----------------------------------------------------------------#
#*********************************************************************************************#
@app.route('/InsList/<string:prg_name>',methods=['GET'])

def InstructorList(prg_name):
    result = db.session.query(Semester.sem_name, Instructor.ins_name). \
        select_from(Instructor).join(Program).join(Semester).filter(Program.p_name == 'IT').order_by(
        Semester.sem_name).all()

    buffer = []

    for i in result:
        x = {"semester ": i[0], "Instructor ": i[1]}
        buffer.append(x)

    return jsonify(buffer)


#*********************************************************************************************#
#------------------SectionCountBySemester----------------------------------------------------------------#
#*********************************************************************************************#

@app.route('/SecCBSem/<string:prg_name>',methods=['GET'])
def SectionCountBySem(prg_name):
    result = db.session.query(Semester.sem_name, func.count(distinct(Student.section))). \
        select_from(Program).join(Semester).join(Student).group_by(Semester.sem_name).filter(
        Program.p_name == prg_name).order_by(Semester.sem_name).all()

    buffer=[]
    for i in result:
        x = {"semester ": i[0], "Total_Section ": i[1]}
        buffer.append(x)

    return jsonify(buffer)


#------------------ProgramRoute-----------------------
api.add_resource(ProgramInfo, '/program')
api.add_resource(ProgramExtract, '/program/<int:p_id>')
#------------------SemesterRoute-----------------------
api.add_resource(SemesterInfo, '/semester')
api.add_resource(SemesterExtract, '/semester/<int:sem_id>')
#------------------InstructorRoute---------------------------
api.add_resource(InstructorInfo,'/instructor')
api.add_resource(InstructorExtract,'/instructor/<int:ins_id>')
#------------------CourseRoute---------------------------
api.add_resource(CourseInfo,'/course')
api.add_resource(CourseExtract,'/course/<int:c_id>')
#------------------StudentRoute---------------------------
api.add_resource(StudentInfo,'/student')
api.add_resource(StudentExtract,'/student/<int:s_id>')

if __name__ == '__main__':
  app.run(port=5000, debug=True)
