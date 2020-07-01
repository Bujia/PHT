
import pickle


TIEDOSTO = 'Kirjasto.dat'

def lue_tiedosto():   
#Funktio tiedoston jos on olemassa muuten palauttaa tyhjän sanakirjan
    try: 
        kirjasto = open(TIEDOSTO, 'rb')
        kirjat = pickle.load(kirjasto)
        kirjasto.close()
        return kirjat

    except IOError:
        return {}
        

def tallenna_kirjat(kirjat):
    #Avaa tiedoston ja tallentaa sen
    try: 
        kirjasto = open(TIEDOSTO, 'wb')
        pickle.dump(kirjat, kirjasto)
        kirjasto.close()
        return True
        
    except IOError:
        return False 
        
    
def lisaa_kirja(kirjat, uusi_kirja):
    #Funktio lisää uuden kirjan tietokantaan

    kirjat[uusi_kirja.get_kirja()] = uusi_kirja
    
def hae_kirja(kirjat, kirja):
    #Funktio hakee käyttäjän haluamansa kirjan ja sen tiedot
    if kirja in kirjat:
        kirja = kirjat[kirja]
    else:
        kirja = None
        
    return kirja

def poista_kirja(kirjat, kirja): 
    #Funktio poistaa kirjan tiedot tietokannasta
  
    if kirja in kirjat: 
        del kirjat[kirja]
        return True
    else:
        return False
    
