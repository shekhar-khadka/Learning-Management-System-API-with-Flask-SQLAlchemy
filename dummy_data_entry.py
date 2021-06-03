from Database_model.app_model import db, Program, Semester, Instructor, Course, Student


def program_entry():
    P1 = Program(p_name="IT")
    P2 = Program(p_name="BCE")
    db.session.add_all([P1, P2])
    db.session.commit()


program_entry()


def semester_entry():
    S1 = Semester(sem_name="First", p_id=1)
    S2 = Semester(sem_name="Second", p_id=1)
    S3 = Semester(sem_name="Third", p_id=1)

    S4 = Semester(sem_name="First", p_id=2)
    S5 = Semester(sem_name="Second", p_id=2)
    S6 = Semester(sem_name="Third", p_id=2)
    db.session.add_all([S1, S2, S3, S4, S5, S6])
    db.session.commit()


semester_entry()


def instructor_entry():
    I1 = Instructor(ins_name="Aarati", contact="9824586781", p_id=1)
    I2 = Instructor(ins_name="Ujjwal", contact="9824586682", p_id=1)
    I3 = Instructor(ins_name="tchiring", contact="9824586783", p_id=2)
    I4 = Instructor(ins_name="Ram", contact="9864586784", p_id=2)

    db.session.add_all([I1, I2, I3, I4])
    db.session.commit()


instructor_entry()


def course_entry():
    C1 = Course(c_name="math", c_hour=15, ins_id=1, sem_id=1)
    C2 = Course(c_name="c_programming", c_hour=12, ins_id=1, sem_id=2)
    C3 = Course(c_name="network", c_hour=13, ins_id=2, sem_id=3)

    C4 = Course(c_name="stat", c_hour=10, ins_id=2, sem_id=1)
    C5 = Course(c_name="OOP", c_hour=12, ins_id=1, sem_id=2)
    C6 = Course(c_name="DataStructure", c_hour=13, ins_id=2, sem_id=3)

    C7 = Course(c_name="math", c_hour=15, ins_id=3, sem_id=4)
    C8 = Course(c_name="stat", c_hour=15, ins_id=3, sem_id=5)
    C9 = Course(c_name="physic", c_hour=15, ins_id=4, sem_id=6)

    C10 = Course(c_name="Electrical", c_hour=15, ins_id=3, sem_id=4)
    C11 = Course(c_name="DataMining", c_hour=15, ins_id=4, sem_id=5)
    C12 = Course(c_name="Bigdata", c_hour=15, ins_id=4, sem_id=6)

    db.session.add_all([C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12])
    db.session.commit()


course_entry()


def student_entry():
    S1 = Student(s_name="shekhar", address="morang", contact="9869135861", section="A", sem_id=1, p_id=1)
    S2 = Student(s_name="biplove", address="Butwal", contact="9869135862", section="B", sem_id=1, p_id=1)
    S8 = Student(s_name="suresh", address="Butwal", contact="9869130862", section="B", sem_id=2, p_id=1)
    S3 = Student(s_name="Nishan", address="bhaktapur", contact="9869135863", section="A", sem_id=3, p_id=1)
    S4 = Student(s_name="umesh", address="morang", contact="9869135864", section="A", sem_id=4, p_id=2)
    S5 = Student(s_name="shirish", address="kathmandu", contact="9869135865", section="A", sem_id=4, p_id=2)
    S6 = Student(s_name="suyesh", address="kathmandu", contact="9869135866", section="B", sem_id=4, p_id=2)
    S7 = Student(s_name="shrijal", address="morang", contact="9869135867", section="B", sem_id=5, p_id=2)
    S9 = Student(s_name="shri", address="dang", contact="9809135867", section="A", sem_id=5, p_id=2)
    S10 = Student(s_name="niroj", address="palpa", contact="9809135800", section="A", sem_id=5, p_id=2)
    S11 = Student(s_name="tanke", address="dhangadi", contact="9809135000", section="A", sem_id=6, p_id=2)

    db.session.add_all([S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11])
    db.session.commit()


student_entry()