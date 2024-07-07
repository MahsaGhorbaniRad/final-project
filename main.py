
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas , datavalidation
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/createcourse/", response_model=schemas.course)
def create_course(course: schemas.course, db: Session = Depends(get_db)):
    DV = datavalidation.course(cid = course.cid , department = course.department 
    , cname = course.cname, credit = course.credit)
    if DV.valid_cid() and DV.valid_cname() and DV.valid_credit() and DV.valid_department():
        db_course = crud.get_course(course_id = course.cid , db = db)
        if db_course:
            raise HTTPException(status_code=400, detail="course is already existed")
        return crud.create_course(db=db, course = course)
    else:
        raise HTTPException(status_code=400 , detail="problem")


@app.post("/createstudent/" , response_model=schemas.student)
def create_student(student: schemas.student , db : Session = Depends(get_db)):

    DV = datavalidation.student(sid = student.sid , Fname = student.Fname , Lname = student.Lname 
    , Father_name = student.Father_name , Birth_date = student.Birth_date , IDS = student.IDS 
    , Born_city = student.Born_city , Address = student.Address , Postal_code = student.Postal_code 
    , Cphone = student.Cphone , Hphone = student.Hphone , department = student.department , major = student.major
    , Married = student.Married , ID = student.ID)

    if DV.valid_Address() and DV.valid_birth_date() and DV.valid_born_city() and DV.valid_department() and \
    DV.valid_Father_name() and DV.valid_Fname() and DV.valid_ID() and DV.valid_IDS and DV.valid_Lname()\
    and DV.valid_major() and DV.valid_mobile() and DV.valid_phone() and DV.valid_postal_code() and \
    DV.valid_sid() and DV.married():

        db_student = crud.get_student(student_id = student.sid , db = db)
        if db_student:
            raise HTTPException(status_code=400 , detail="student is already existed")
        return crud.create_student(db=db , student = student)
    else:
        raise HTTPException(status_code=400 , detail="problem")

@app.post("/createlecturer/" , response_model=schemas.lecturer)
def create_lecturer(lecturer : schemas.lecturer , db : Session = Depends(get_db)):

    dv = datavalidation.lecturer(Lid = lecturer.Lid , Fname = lecturer.Fname , Lname = lecturer.Lname 
    , ID = lecturer.ID , department = lecturer.department , born_city = lecturer.born_city 
    , Address = lecturer.Address , postal_code = lecturer.postal_code , Cphone = lecturer.Cphone 
    , birth_date = lecturer.birth_date , major = lecturer.major , Hphone = lecturer.Hphone)

    if dv.valid_Address() and dv.valid_birth_date() and dv.valid_born_city() and dv.valid_department() \
    and dv.valid_Fname() and dv.valid_ID() and dv.valid_lecturer_id() and dv.valid_Lname() and dv.valid_major() \
    and dv.valid_mobile() and dv.valid_phone() and dv.valid_postal_code():
        
        db_lecturer = crud.get_lecturer(lecturer_id = lecturer.Lid , db = db)
        if db_lecturer:
            raise HTTPException(status_code=400 , detail="lecturer is already existed")
        return crud.create_lecturer(db=db , lecturer = lecturer)
    else:
        raise HTTPException(status_code=404 , detail="problem")


@app.get("/readcourse/{course_id}", response_model=schemas.course)
def read_course(course_id: str , db: Session = Depends(get_db)):
    db_course = crud.get_course(course_id = course_id , db = db)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course


@app.get("/readstudent/{student_id}")
def read_student(student_id : str , db : Session = Depends(get_db)):
    db_student = crud.get_student(student_id = student_id , db = db)
    if db_student is None:
        raise HTTPException(status_code=404 , detail="student not found")
    return db_student


@app.get("/readlecturer/{lecturer_id}" , response_model=schemas.lecturer)
def read_lecturer(lecturer_id : str , db : Session = Depends(get_db)):
    db_lecturer = crud.get_lecturer(lecturer_id = lecturer_id , db = db)
    if db_lecturer is None:
        raise HTTPException(status_code=404 , detail="lecturer not found")
    return db


@app.get("/deletecourse/{course_id}")
def delete_course(course_id : int , db : Session = Depends(get_db)):
    db_course = crud.get_course(course_id = course_id , db = db)
    if db_course:
        crud.delete_course(db = db , course_id = course_id)
        return f"successfuly done"
    else:
        raise HTTPException(status_code=404 , detail="course not found")


@app.get("/deletestudent/{student_id}")
def delete_student(student_id : int , db : Session = Depends(get_db)):
    db_student = crud.get_student(student_id = student_id , db = db)
    if db_student:
        crud.delete_student(db = db , student_id = student_id)
        return f"succsessfuly done"
    else:
        raise HTTPException(status_code=404 , detail="student not found")


@app.get("/deletelecturer/{lecturer_id}")
def delete_lecturer(lecturer_id : int , db : Session = Depends(get_db)):
    db_lecturer = crud.get_lecturer(lecturer_id = lecturer_id , db = db)
    if db_lecturer:
        crud.delete_lecturer(db = db , lecturer_id = lecturer_id)
        return f"successfuly done"
    else:
        raise HTTPException(status_code=404 , detail="lecturer not found")


@app.post("/updatecourse/" , response_model=schemas.course)
def update_course(course : schemas.course , db : Session = Depends(get_db)):
    db_course = crud.get_course(course_id = course.cid , db = db)
    if db_course:
        crud.update_course(course_id = course.cid , db = db , course = course)
    else:
        raise HTTPException(status_code=404 , detail="course not found")


@app.post("/updatestudent/" , response_model=schemas.student)
def update_student(student : schemas.student , db : Session = Depends(get_db)):
    db_student = crud.get_student(student_id = student.sid , db = db)
    if db_student:
        crud.update_student(student_id = student.sid , db = db , student = student)
    else:
        raise HTTPException(status_code=404 , detail="student not found")


@app.post("/lecturerupdate/" , response_model=schemas.lecturer)
def update_lecturer(lecturer : schemas.lecturer , db : Session = Depends(get_db)):
    db_lecturer = crud.get_lecturer(lecturer_id = lecturer.Lid , db = db)
    if db_lecturer:
        crud.update_lecturer(lecturer_id = lecturer.Lid , db = db , lecturer = lecturer)
    else:
        raise HTTPException(status_code=404 , detail="course not found")