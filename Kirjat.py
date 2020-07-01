

class Kirja(object):


    def __init__(self, kirja, author, varaus, paiva):
 
        self.kirja = kirja
        self.author = author
        self.varaus = varaus
        self.paiva = paiva
  
    def get_kirja(self):
        return self.kirja
        
    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author
    
    def set_varaus(self, varaus):
        self.varaus = varaus
        
    def get_varaus(self):
        return self.varaus
    
    def set_paiva(self, paiva):
        set.paiva = paiva
        
    def get_paiva(self):
        return self.paiva
    
    
    def __str__(self):
       
        return self.author + "\t" + self.varaus + "\t" + self.paiva
    
