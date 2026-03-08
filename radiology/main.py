import Radiology
import Person 
import Date
import pickle
## main data structue for 
##  dictionary  = {'date':{'ct':[patients] , 'Mri':[patients] , 'ultrasound':[patients]}}
## text  ----> 28/2/2026 ----> [patients] ----> [patients] ----> [patients] 
## after read text we will take a list of dates 



def convertpatienttext(filename):
    """
        read the file exist and make each line as list which is a patient except the [0] in the text
    """
    text = open(filename,'r')
    string_lines = []
    for line in text:
        line = line.split(' ----> ')
        string_lines.append(line)

    for line in string_lines:
        for word in line:
            if word == '':
                line.remove(word)
    
    return string_lines

# filename = '//home/ahmed/vscode/radiology/patients.txt'
# print(convertpatienttext(filename))

def add_patient_data(filename , patient):
    """
        this function return a new write in the txt file as patient 
        filename :  is the path of the file
        patient : is the patient object type 
    """
    file = open(filename , 'a')  ## 'a'  append mode 
    # print(str(file))
    file.write(str(patient)+'\n')



# filename = '/home/ahmed/vscode/radiology/patients.txt'
# patient = Person.Patient('ahmed' , 25 , 'male' , 'gg' , 'cvs' , 'ct')
# add_patient_data(filename , patient)


def read_dates(filename):

    with open(filename , 'rb') as file:
        loaded_dict = pickle.load(file)
    
    return loaded_dict

def add_dates(filename , dates_dict):
    
    with open(filename , 'ab') as file:
        pickle.dump(dates_dict , file)




def search_patient(filename , patient):
    """"""
    lines = convertpatienttext(filename)
    for line in lines:
        if patient == line[0]:
            mes = 'found'
            return mes , line
        else:
            mes = 'not found'
            return mes , None



def valid_date(date,dates):
    """
     this function is to see if the date in the dictionary of dates if in return True 
     else False
    """
    if date not in dates:
        return False
    return True




def valid_modality(modality, date , dates):
    """
       modality : is the type of imaging we use 
       date : is the date we will see its validity 
       dates : is adictionary of dates 

       return the confiramtion of validty of the modality of test
    """
    ## intialize or boolean flags
    ctvalid = False
    mrivalid = False
    ultrasoundvalid = False

    ## see if the date is valid or not exist in the dictionary or not
    if valid_date(date , dates):
        ## if valid date 
        ## iterate through its value which is dictionary also 

        for k ,v in  dates[date].items():
                ## if the key is ct 
                if k == 'ct':
                    ## we see if the lenght of the list of patients associated with it is still not full or not
                    if len(v) < 15:
                        ## if not full we change the bool to ture 
                        ctvalid = True
                ## if the modalitity is mri
                if k == 'mri':
                    ## and the lenght of the patient lists associated with it is not full
                    if len(v) < 5:
                        ## we change the bool to true 
                        mrivalid = True
                ## if the modality is ultrasound
                if k == 'ultrasound':
                    ## if the lenght not full 
                    if len(v) < 10:
                        ## change the bool
                        ultrasoundvalid = True
    
    ## we return the bool associated with modality of test 
    if modality == 'ct':
        return ctvalid
    elif modality == 'mri':
        return mrivalid
    elif modality == 'ultrasound':
        return ultrasoundvalid
    






def make_date_dict(dates):
    """
        dates is a list of date object type 
        return a dictionary of the dates with official format which is 
        dates_dict = {date(str):{'ct':[] , 'mri':[] , 'ultrasound':[]}}
    """
    ## intailize an empty dictionary 
    dates_dict = {}
    ## iterate through the dates list 
    for date in dates:
        ## we convert the date to str formate first if not in the dates dictionary 
        if date.__str__() not in dates_dict:
            ## we make the new format in the dates_dictionary
            dates_dict[Date.convertdatestring(date)] = {'ct':[] , 'mri':[] , 'ultrasound':[]}
    ## return the dictionary
    return dates_dict
            


def confirm_patient(patient , dates_dict):
    """
        patient: is patient object type
        dates_dict : is a dictionary we made as date

        return the date and the confirm message the the patients appended to the date of modality
    """
    
    ## we iterate through the dictionary items
    for date , modalities in dates_dict.items():
        ## we iterate through the vlaue which is dictionary itself
        for modality , patiens_list in modalities.items():
            ## if the modality patient need to reserve equal to the modality in the dictionat 
            if patient.get_imaging() == modality:
                ## if the modality is available and valid in this date 
                if valid_modality(modality,date,dates_dict):
                    ## we add the patient to the modality list in specific date 
                    patiens_list.append(patient)
                    mes = 'confirmed'
                else:
                    mes = 'unconfirmed'
                return date ,mes

## unit test for date module 
# date = Date.Date(28 , 2 , 2026)
# dates = date.generate_dates(30)
# # # for date in dates:
# # #     print(date)

# # ## unit test for mak dict function 
# date_dict = make_date_dict(dates)

# # ## unit test for valid date 
# # print(valid_date(date.__str__(), date_dict))

# # ## unit test for valid modality function 
# ultrasoundvalid= valid_modality('ultrasound' , date.__str__() ,date_dict)
# print(ultrasoundvalid)

# # # print(date_dict)
# ahmed = Person.Patient('ahmed' , 25 , 'male', 'depres' , 'psych' , 'ct')
# date , mes = confirm_patient(ahmed ,date_dict )
# print(date , mes)
        


def radiology_system():

    ## intialize the filename 
    patient_file = 'patients.txt'
    dates_file = 'dates.txt'
    ## loop 
    while True:
        ## the welcome meesage 
        print(70*'/')
        print( 10*'= ' + 'WELCOM TO RADIOLOGY DEPATMENT' + 10*' =')
        print(70*'/')

        ## choose what to do with the programe
        print('1-add new patient')
        print('2-search patient')
        print('3-exit')
        sys = int(input())

        ## if the choose is search or 
        if sys == 2:
            search = input('enter patien name: ')
            ## 
            mes , pt = search_patient(patient_file , search)
            print(mes , pt)
        elif sys == 3:
            print('TTHANK YOU')
            break

        else:

        ## take the patien data 
            name = input('patient name: ')
            age = int(input('age: '))
            gender = input('gender of the patient: ')
            department = input('department: ')
            diagnosis = input('what is the diagnosis?: ')
            print('choose the imaging type')
            print('1- CT')
            print('2-MRI')
            print('3-ultrasound')
            imaging = int(input('choose: '))
            system = input('system to do imaging on: ')
            ## doctor who ask for imaging 
            physician = input('name of the doctor ')

            ## make the radiology object acording to the type of the imaging physician ask for 
            if imaging == 1:
                ## ct radiology
                modality = Radiology.Radiology(system ,'ct')
            elif imaging == 2:
                ## MRI radiology 
                modality = Radiology.Radiology(system ,'mri')
            elif imaging== 3:
                ## ultrasound radiology 
                modality = Radiology.Radiology(system , 'ultrasound')



            ## make our objects 

            patient = Person.Patient(name , age , gender , diagnosis  ,department ,modality.get_modality() )  ## each patient have an ID 
            doctor = Person.Doctor(physician ,department)
               ## see if the patient confirmation 

            dates_dict = read_dates(dates_file)

        ## 2. IF NO FILE EXISTS YET, MAKE A NEW EMPTY ONE
            if dates_dict is None:
                print("Creating a brand new calendar...")
                current_date = Date.Date(28, 2, 2026)
                dates = current_date.generate_dates(30)
                dates_dict = make_date_dict(dates)

            ## 3. CONFIRM THE PATIENT (MODIFY)
            ## Notice: Pass dates_dict here, NOT dates_file!
            date, confirmation = confirm_patient(patient, dates_dict)

            ## 4. SAVE THE UPDATED DICTIONARY (SAVE)

            ## final simple message 
            if confirmation == 'confirmed':   
                print(f'your modality is confirmed in {date}for the patient {patient.get_name}')
                add_dates(dates_file , dates_dict)
            else:
                print(confirmation)



## unit text 
# date = Date.Date(8 , 3 , 2026)
# dates = date.generate_dates(9)
# dates_dict = make_date_dict(dates)
# filename = '/home/ahmed/vscode/radiology/dates.txt'
# add_dates(filename , dates_dict)
# print(read_dates(filename))


radiology_system()