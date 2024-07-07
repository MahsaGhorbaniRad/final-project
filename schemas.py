
from pydantic import BaseModel


class course(BaseModel):
    cid : str
    cname : str
    department : str
    credit : int

class student(BaseModel):
    sid : str
    Fname : str
    Lname : str
    Father_name : str
    Birth_date : str
    IDS : str
    Born_city : str
    Address : str
    Postal_code : int
    Cphone : int
    Hphone : int
    department : str
    major : str
    Married : bool
    ID : str



class lecturer(BaseModel):
    Lid : str
    Fname : str
    Lname : str
    ID : str
    department : str
    major : str
    birth_date : str
    born_city : str
    Address : str
    postal_code : int
    Cphone : int
    Hphone : int
