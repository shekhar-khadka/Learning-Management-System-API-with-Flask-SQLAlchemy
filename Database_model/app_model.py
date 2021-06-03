from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource


# Init app
app = Flask(__name__)

# local
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shekhar:khadka553@localhost/test'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#1
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lhfweknhhieeih:5ddd68841699300c1020be476d3140e50d895aaef8331f240e2940e5f88899cd@ec2-23-23-128-222.compute-1.amazonaws.com:5432/d8lqgq3a0t9kn5'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#2
x='postgresql://rsfwridkcgquwr:64de090139967e662807b1a29f0e5fcd6028fc614fb7856c2c90c6a7906084ba@ec2-54-155-226-153.eu-west-1.compute.amazonaws.com:5432/dapcbcacg9rutd'
app.config['SQLALCHEMY_DATABASE_URI']=x

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)



class Program(db.Model):
    p_id=db.Column(db.Integer,primary_key=True)
    p_name=db.Column(db.String(20),nullable=False,unique=True)
    semesters = db.relationship("Semester",cascade="all,delete", backref="program", lazy=True)
    instructors=db.relationship("Instructor",cascade="all,delete",backref="program",lazy=True)
    p_students = db.relationship("Student", cascade="all,delete", backref="program", lazy=True)
    def __init__(self,p_name,):
        self.p_name=p_name

    def __repr__(self):
        return'<p_id {} >'.format(self.p_id)

class ProgramSchema(ma.Schema):
    class Meta:
        fields = ("p_id", "p_name")
        model = Program



#********************************************************************************************************#
#------------------Semester----------------------------------------------------
#*******************************************************************************************#

class Semester(db.Model):
    sem_id=db.Column(db.Integer,primary_key=True)
    sem_name=db.Column(db.String(20),nullable=False)
    p_id=db.Column(db.Integer, db.ForeignKey('program.p_id'),nullable=False)
    courses = db.relationship("Course", cascade="all,delete", backref="semester", lazy=True)
    s_students = db.relationship("Student", cascade="all,delete", backref="semester", lazy=True)



class SemesterSchema(ma.Schema):
    class Meta:
        fields = ("sem_id", "sem_name", "p_id")
        model = Semester



#*********************************************************************************************#
#------------------ Instructor----------------------------------------------------------------#
#*********************************************************************************************#

class Instructor(db.Model):
    ins_id=db.Column(db.Integer,primary_key=True)
    ins_name=db.Column(db.String(20),nullable=False)
    contact=db.Column(db.String(10),nullable=False,unique=True)
    p_id=db.Column(db.Integer,db.ForeignKey('program.p_id'), nullable=False)
    i_courses = db.relationship("Course", cascade="all,delete", backref="instructor", lazy=True)
    
    
    def __init__(self,ins_name,contact,p_id):
        self.ins_name=ins_name
        self.contact=contact
        self.contact=contact
        self.p_id=p_id
        

    def __repr__(self):
        return'<ins_id {} >'.format(self.ins_id)
    
class InstructorSchema(ma.Schema):
    class Meta:
        fields=("ins_id","ins_name","contact","p_id")
        model=Instructor



class Course(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(20), nullable=False)
    c_hour = db.Column(db.Integer, nullable=False)
    ins_id = db.Column(db.Integer, db.ForeignKey('instructor.ins_id'), nullable=False)
    sem_id = db.Column(db.Integer, db.ForeignKey('semester.sem_id'), nullable=False)

    def __init__(self, c_name, c_hour, ins_id,sem_id):
        self.c_name = c_name
        self.c_hour = c_hour
        self.ins_id = ins_id
        self.sem_id = sem_id

    def __repr__(self):
        return '<c_id {} >'.format(self.c_id)


class CourseSchema(ma.Schema):
    class Meta:
        fields = ("c_id","c_name","c_hour","ins_id","sem_id")
        model = Course


class Student(db.Model):
    s_id = db.Column(db.Integer, primary_key=True)
    s_name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), nullable=False)
    contact = db.Column(db.String(10),unique=True,nullable=False)
    section=db.Column(db.String(1),nullable=False)
    sem_id = db.Column(db.Integer, db.ForeignKey('semester.sem_id'), nullable=False)
    p_id = db.Column(db.Integer, db.ForeignKey('program.p_id'), nullable=False)

    def __init__(self, s_name,section, address,contact, p_id,sem_id):
        self.s_name = s_name
        self.section = section
        self.address=address
        self.contact=contact
        self.p_id = p_id
        self.sem_id = sem_id

    def __repr__(self):
        return '<s_id {} >'.format(self.s_id)


class StudentSchema(ma.Schema):
    class Meta:
        fields = ("s_id","s_name","section", "address","contact", "p_id","sem_id")
        model = Student



