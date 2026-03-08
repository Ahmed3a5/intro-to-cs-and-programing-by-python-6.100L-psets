class Radiology(object):
    def __init__(self , system ,modality_type ,Maximum=None ,report= None):
        self.system = system
        self.Maximum = Maximum
        self.report = report
        self.modality = modality_type

        if self.modality.lower() == 'ct':
            self.Maximum = 15
        elif self.modality.lower() == 'mri':
            self.Maximum = 5
        elif self.modality.lower() == 'ultrasound':
            self.Maximum = 10
    
    
    def get_system(self):
        return self.system 
    
    def get_limit(self):
        return self.Maximum
    
    def get_report(self):
        if self.report == None:
            mes = 'no report yet'
            return mes
        return self.report
    
    def get_modality(self):
        return self.modality.lower()
    
    def change_modality(self , newmodality):
        self.modality = newmodality
    
    def change_maximum(self , newMax):
        self.Maximum = newMax


    def change_system(self , newsystem):
        self.system = newsystem

    def make_report(self , report):
        self.report = report

    def __eq__(self,other):
        if type(self) != type(other):
            return False
        return True
    

    def confirmation(self):

        if self.Maximum <= 0:
            self.Maximum = None
        else:
            self.Maximum -=1
    

            