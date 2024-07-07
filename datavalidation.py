
import re

class course():


    def __init__(self , cid , department , cname , credit):
        self.cid = cid
        self.department = department
        self.cname = cname
        self.credit = credit


    def valid_cid(self):
        cid_regex = "^[0-9]{5}$"
        if re.search(cid_regex , self.cid):
            return True
        else:
            return False


    def valid_department(self):
        d = ["فنی و مهندسی" , "علوم پایه" , "علوم انسانی" , "دامپزشکی" , "اقتصاد" , "کشاورزی" , "منابع طبیعی"]
        for i in d:
            if self.department == i:
                a = 1
                return True
                break
            else:
                a = 0
        if a == 0:
            return False


    def valid_cname(self):
        cname_regex = "^[آ-ی]{1,10}$"
        if re.search(cname_regex , self.cname):
            return True
        else:
            return False

    
    def valid_credit(self):
        self.credit = str(self.credit)
        credit_regex = "^[1-4]{1}$"
        if re.search(credit_regex , self.credit):
            return True
        else:
            return False

class student:


    def __init__(self , sid , Fname , Lname , Father_name , Birth_date , IDS , Born_city ,
     Address , Postal_code , Cphone , Hphone , department , major , Married , ID):
     self.sid = sid
     self.Fname = Fname 
     self.Lname = Lname
     self.Father_name = Father_name
     self.Birth_date = Birth_date
     self.IDS = IDS
     self.Born_city = Born_city
     self.Address = Address
     self.Postal_code = Postal_code
     self.Cphone = Cphone
     self.Hphone = Hphone
     self.department = department
     self.major = major
     self.Married = Married
     self.ID = ID



    def valid_sid(self):
        sid_regex = "^40([0-2]{1})114150([0-9]{1}[1-9]{1})$"
        if re.search(sid_regex , self.sid):
            return True
        else:
            return False


    def valid_Fname(self):
        name_regex = "^[آ-ی]{1,10}$"
        if re.search(name_regex , self.Fname):
            return True
        else:
            return False

    
    def valid_Lname(self):
        name_regex = "^[آ-ی]{1,10}$"
        if re.search(name_regex , self.Lname):
            return True
        else:
            return False

    
    def valid_Father_name(self):
        name_regex = "^[آ-ی]{1,10}$"
        if re.search(name_regex , self.Fname):
            return True
        else:
            return False


    def valid_birth_date(self):
        birth_date_regex = "^1(3[0-9]{1}[0-9]{1}|40[0-3])/([1-9]{1}|1[0-2])/([1-9]{1}|[1-2]{1}[0-9]{1}|3[0-1])"
        if re.search(birth_date_regex , self.Birth_date):
            return True
        else:
            return False


    def valid_IDS(self):
        IDS_regex = "^[آ-ی]{1}[1-9]{2}/[1-9]{6}"
        if re.search(IDS_regex , self.IDS):
            return True
        else:
            return False



    def valid_born_city(self):
        a = ["خرم آباد" , "تهران" , "مشهد" , "اصفهان" , "شیراز" , "تبریز" , "ارومیه" , "ایلام" , "یزد" 
        , "کرمان" , "بیرجند" , "زاهدان" , "بندرعباس" , "بوشهر" , "شهرکرد" , "اراک", "گرگان" , "بجنورد" 
        , "ساری" , "سمنان" , "قم" , "قزوین" , "رشت" , "زنجان" , "سنندج" , "اردبیل" , "کرمانشاه" , "اهواز" 
        , "همدان" , "یاسوج" ,]
        for i in a:
            if self.Born_city == i:
                a = 1
                return True
                break
            else:
                a = 0
        if a == 0:
            return False


    def valid_Address(self):
        Address_regex = "^[\sآ-ی0-9]{1,100}$"
        if re.search(Address_regex , self.Address):
            return True
        else:
            return False


    def valid_postal_code(self):
        self.Postal_code = str(self.Postal_code)
        postal_code_regex = "^[0-9]{10}$"
        if re.search(postal_code_regex , self.Postal_code):
            return True
        else:
            return False


    def valid_mobile(self):
        self.Cphone = str(self.Cphone)
        mobile_regex = "^9(1[0-9]|3[1-9])-?[0-9]{3}-?[0-9]{4}$"
        if re.search(mobile_regex , self.Cphone):
            return True
        else:
            return False


    def valid_phone(self):
        self.Hphone = str(self.Hphone)
        phone_regex = "^[0-9]{8}$"
        if re.search(phone_regex , self.Hphone):
            return True
        else:
            return False


    def valid_department(self):
        d = ["فنی و مهندسی" , "علوم پایه" , "علوم انسانی" , "دامپزشکی" , "اقتصاد" , "کشاورزی" , "منابع طبیعی"]
        for i in d:
            if self.department == i:
                a = 1
                return True
                break
            else:
                a = 0
        if a == 0:
            return False


    def valid_major(self):
        m = ["مهندسی کامپیوتر" , "مهندسی صنایع" , "مهندسی پزشکی" , "مهندسی عمران" , "مهندسی مکانیک"
            , "مهندسی پلیمر" , "مهندسی نفت" , "مهندسی معدن"]
        for i in m:
            if self.major == i:
                a = 1
                return True
                break
            else:
                a = 0
        if a == 0:
            return False


    def married(self):
        if self.Married:
            return True
        else:
            return False


    def valid_ID(self):
        sum = 0
        if len(self.ID) == 10:
            for i in range(10 , 1 , -1):
                sum += int(self.ID[10 - i]) * i
            if (sum % 11) >= 2:
                if (11 - (sum % 11)) == int(self.ID[9]):
                    return True
            elif (sum % 11) < 2:
                if (sum % 11) == int(self.ID[9]):
                    return True
            else:
                return False
        else:
            return False


class lecturer:


    def __init__(self , Lid , Fname , Lname , ID , department , born_city , Address , postal_code 
    , Cphone , birth_date ,  major , Hphone):
        self.Lid = Lid
        self.Fname = Fname 
        self.Lname = Lname 
        self.ID = ID 
        self.department = department 
        self.born_city = born_city 
        self.Address = Address
        self.postal_code = postal_code
        self.Cphone = Cphone
        self.birth_date = birth_date
        self.major = major
        self.Hphone = Hphone



    def valid_lecturer_id(self):
        Lid_regex = "^[0-9]{6}$"
        if re.search(Lid_regex , self.Lid):
            return True
        else:
            return False


    def valid_Fname(self):
        name_regex = "^[آ-ی]{1,10}$"
        if re.search(name_regex , self.Fname):
            return True
        else:
            return False

    
    def valid_Lname(self):
        name_regex = "^[آ-ی]{1,10}$"
        if re.search(name_regex , self.Lname):
            return True
        else:
            return False


    
    def valid_ID(self):
        sum = 0
        if len(self.ID) == 10:
            for i in range(10 , 1 , -1):
                sum += int(self.ID[10 - i]) * i
            if (sum % 11) >= 2:
                if (11 - (sum % 11)) == int(self.ID[9]):
                    return True
            elif (sum % 11) < 2:
                if (sum % 11) == int(self.ID[9]):
                    return True
            else:
                return False
        else:
            return False  



    def valid_department(self):
        d = ["فنی و مهندسی" , "علوم پایه" , "علوم انسانی" , "دامپزشکی" , "اقتصاد" , "کشاورزی" , "منابع طبیعی"]
        for i in d:
            if self.department == i:
                a = 1
                return True
                break
            else:
                a = 0
        if a == 0:
            return False


    def valid_born_city(self):
        a = ["خرم آباد" , "تهران" , "مشهد" , "اصفهان" , "شیراز" , "تبریز" , "ارومیه" , "ایلام" , "یزد" 
        , "کرمان" , "بیرجند" , "زاهدان" , "بندرعباس" , "بوشهر" , "شهرکرد" , "اراک", "گرگان" , "بجنورد" 
        , "ساری" , "سمنان" , "قم" , "قزوین" , "رشت" , "زنجان" , "سنندج" , "اردبیل" , "کرمانشاه" , "اهواز" 
        , "همدان" , "یاسوج" ,]
        for i in a:
            if self.born_city == i:
                a = 1
                return True
                break
            else:
                a = 0
        if a == 0:
            return False


    def valid_Address(self):
        Address_regex = "^[\sآ-ی0-9]{1,100}$"
        if re.search(Address_regex , self.Address):
            return True
        else:
            return False


    def valid_postal_code(self):
        self.postal_code = str(self.postal_code)
        postal_code_regex = "^[0-9]{10}$"
        if re.search(postal_code_regex , self.postal_code):
            return True
        else:
            return False


    def valid_mobile(self):
        self.Cphone = str(self.Cphone)
        mobile_regex = "^9(1[0-9]|3[1-9])-?[0-9]{3}-?[0-9]{4}$"
        if re.search(mobile_regex , self.Cphone):
            return True
        else:
            return False


    def valid_birth_date(self):
        birth_date_regex = "^1(3[0-9]{1}[0-9]{1}|40[0-3])/([1-9]{1}|1[0-2])/([1-9]{1}|[1-2]{1}[0-9]{1}|3[0-1])"
        if re.search(birth_date_regex , self.birth_date):
            return True
        else:
            return False


    def valid_major(self):
        m = ["مهندسی کامپیوتر" , "مهندسی صنایع" , "مهندسی پزشکی" , "مهندسی عمران" , "مهندسی مکانیک"
            , "مهندسی پلیمر" , "مهندسی نفت" , "مهندسی معدن"]
        for i in m:
            if self.major == i:
                a = 1
                return True
                break
            else:
                a = 0
        if a == 0:
            return False


    def valid_phone(self):
        self.Hphone = str(self.Hphone)
        phone_regex = "^[0-9]{8}$"
        if re.search(phone_regex , self.Hphone):
            return True
        else:
            return False