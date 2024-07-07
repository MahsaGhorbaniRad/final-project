
from sqlalchemy.orm import Session

import models , schemas


def get_course(course_id: str , db : Session):
    return db.query(models.course).filter(models.course.cid == course_id).one_or_none()


def get_student(student_id : str , db : Session):
    return db.query(models.student).filter(models.student.sid == student_id).first()


def get_lecturer(lecturer_id : str , db : Session):
    return db.query(models.lecturer).filter(models.lecturer.Lid == lecturer_id).first()


def create_course(db : Session , course : schemas.course):
    db_course = models.course(cid = course.cid , cname = course.cname , department = course.department
                               , credit = course.credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course



def create_student(db : Session , student : schemas.student):
    db_student = models.student(sid = student.sid , Fname = student.Fname , Lname = student.Lname
                                 , Father_name = student.Father_name , Birth_date = student.Birth_date
                                 , IDS = student.IDS , Born_city = student.Born_city
                                 , Address = student.Address , Postal_code = student.Postal_code
                                 , Cphone = student.Cphone , Hphone = student.Hphone 
                                 , department = student.department , major = student.major
                                 , Married = student.Married , ID = student.ID)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student



def create_lecturer(db : Session , lecturer : schemas.lecturer):
    db_lecturer = models.lecturer(Lid = lecturer.Lid , Fname = lecturer.Fname , Lname = lecturer.Lname
                                  , ID = lecturer.ID , department = lecturer.department 
                                  , major = lecturer.major , birth_date = lecturer.birth_date 
                                  , born_city = lecturer.born_city , Address = lecturer.Address
                                  , postal_code = lecturer.postal_code , Cphone = lecturer.Cphone
                                  , Hphone = lecturer.Hphone)
    db.add(db_lecturer)
    db.commit()
    db.refresh(db_lecturer)
    return db_lecturer


def delete_course(course_id : str , db : Session):
    data_to_delete = db.query(models.course).filter(models.course.cid == course_id).first()
    db.delete(data_to_delete)
    db.commit()
    

def delete_student(student_id : str , db : Session):
    data_to_delete = db.query(models.student).filter(models.student.sid == student_id).first()
    db.delete(data_to_delete)
    db.commit()


def delete_lecturer(lecturer_id : str , db : Session):
    data_to_delete = db.query(models.lecturer).filter(models.lecturer.Lid == lecturer_id).first()
    db.delete(data_to_delete)
    db.commit()
     


def update_course(course_id : str , db : Session , course : schemas.course):
    data_to_update = db.query(models.course).filter(models.course.cid == course_id).filter()
    if data_to_update:
        delete_course(course_id = course_id , db = db)
        new_data = models.course(cid = course.cid , cname = course.cname
        , department = course.department , credit = course.credit)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data


def update_student(student_id : str , db : Session , student : schemas.student):
    data_to_update = db.query(models.student).filter(models.student.sid == student_id).one_or_none()
    if data_to_update:
        delete_student(student_id = student_id , db = db)
        new_data = models.student(sid = student.sid , Fname = student.Fname , Lname = student.Lname
                                    , Father_name = student.Father_name , Birth_date = student.Birth_date
                                    , IDS = student.IDS , Born_city = student.Born_city
                                    , Address = student.Address , Postal_code = student.Postal_code
                                    , Cphone = student.Cphone , Hphone = student.Hphone 
                                    , department = student.department , major = student.major
                                    , Married = student.Married , ID = student.ID)
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data


def update_lecturer(lecturer_id : str , db : Session , lecturer : schemas.lecturer):
    data_to_update = db.query(models.lecturer).filter(models.lecturer.Lid == lecturer_id).one_or_none()
    if data_to_update:
        delete_lecturer(lecturer_id = lecturer_id , db = db)
        new_date = models.lecturer(Lid = lecturer.Lid , Fname = lecturer.Fname , Lname = lecturer.Lname
                                    , ID = lecturer.ID , department = lecturer.department 
                                    , major = lecturer.major , birth_date = lecturer.birth_date 
                                    , born_city = lecturer.born_city , Address = lecturer.Address
                                    , postal_code = lecturer.postal_code , Cphone = lecturer.Cphone
                                    , Hphone = lecturer.Hphone)
        db.add(new_date)
        db.commit()
        db.refresh(new_date)
        return new_date 