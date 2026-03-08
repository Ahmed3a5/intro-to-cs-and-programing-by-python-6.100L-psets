class Person(object):

    def __init__(self ,name,gender ,department):
        self.name = name 
        self.department = department
        self.gender = gender

    

    def get_name(self):
        return self.name

    def get_department(self):
        return self.department
    
    def get_gender(self):
        return self.gender
    
    
    def change_name(self , newname):
        self.name = newname

    def change_department(self , newdepart):
        self.department = newdepart

    def change_gender(self , newgender):
        self.gender = newgender




class Doctor(Person):

    def __init__(self, name , department , gender=None):
       Person.__init__(self  ,name, gender, department)


class Patient(Person):
    count = 0

    def __init__(self , name , age ,gender , Dx , department ,imaging , date=None , report=None):
        Person.__init__(self ,name ,gender ,department)
        self.age = age
        self.diagnosis = Dx
        Patient.count += 1
        self.ID = Patient.count
        self.imaging = imaging
        self.date = date
        self.report = report
    
    def get_age(self):
        return self.age

    def get_diagnosis(self):
        return self.diagnosis
    
    def get_ID(self):
        return self.ID
    
    def get_imaging(self):
        return self.imaging
    
    def get_date(self):
        if self.date == None:
            mes = 'no date reserved yet'
            return mes
        return self.date
    
    def get_report(self):
        if self.report == None:
            mes = 'no report yet'
            return mes
        return self.report
    
    def change_age(self , newage):
        self.age = newage
    
    def change_imaging(self , newimaging):
        self.imaging = newimaging

    def __str__(self):
        mes = ' ----> ' + self.name +\
        ' ----> '+str(self.ID)+' ----> ' +\
        str(self.age) + ' ----> '+ \
        self.gender + ' ----> ' + \
        self.diagnosis + ' ----> ' + \
        self.department + ' ----> '+ \
        self.imaging + ' ----> ' + \
        str(self.date) + ' ----> ' + str(self.report)

        return mes
    