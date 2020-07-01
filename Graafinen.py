import tkinter
import tkinter.messagebox
from Kirjat import *
from Koodi import *

class OmaGUI:
    def __init__(self, kirjat):

        self.paa = tkinter.Tk()

        #kehykset
        self.yla = tkinter.Frame(self.paa)
        self.yla1 = tkinter.Frame(self.paa)
        self.keski = tkinter.Frame(self.paa)
        self.ala = tkinter.Frame(self.paa)
        self.painikkeet = tkinter.Frame(self.paa)
        #muuttujat
        self.kirjat = kirjat
        self.kirja = tkinter.StringVar()
        self.kirjailija = tkinter.StringVar()
        self.varaus = tkinter.StringVar()  
        self.paiva = tkinter.StringVar()    
        #Kommennut/nappulat/syötekentät
        self.haku = tkinter.Button(self.yla, text = "Haku", command = self.etsi)
        self.lisaa = tkinter.Button(self.yla, text = "Lisää/päivitä", command = self.lis_kirja)
        self.tyhjenna = tkinter.Button(self.yla, text = "Tyhjennä", command = self.empty)
        self.lainaa = tkinter.Button(self.yla1, text = "Lainaa", command = self.lai_kirja)
        self.palauta = tkinter.Button(self.yla1, text = "Palauta", command = self.pal_kirja)
        self.poista = tkinter.Button(self.yla1, text = "Poista", command = self.del_kirja)
        self.kirjatieto = tkinter.Label(self.keski, text="Kirjan nimi :")
        self.kirjasyote = tkinter.Entry(self.keski, text = self.kirja)
        self.kirjailija_ = tkinter.Label(self.keski, text="Kirjailijan nimi :")
        self.kirjailijasyote = tkinter.Entry(self.keski, text = self.kirjailija)
        self.varaus_ = tkinter.Label(self.keski, text = "Varaus :")
        self.varaussyote = tkinter.Entry(self.keski, text = self.varaus)
        self.paivasyote = tkinter.Label(self.keski, text = "Palautus päivämäärä :")
        self.paivakentta = tkinter.Entry(self.keski, text = self.paiva)
        self.tuhoa = tkinter.Button(self.painikkeet, text = "lopeta", \
                                    command = self.tuhoa)
          
    #Pakkaus
        self.lainaa.pack(side = "left")
        self.lisaa.pack(side= "left")
        self.tyhjenna.pack(side = "left")
        self.palauta.pack(side = "right")
        self.haku.pack(side = "left")
        self.poista.pack(side = "left")
        self.kirjatieto.pack()
        self.kirjasyote.pack()
        self.kirjailija_.pack()
        self.kirjailijasyote.pack()
        self.varaus_.pack()
        self.varaussyote.pack()
        self.paivasyote.pack()
        self.paivakentta.pack()
        self.tuhoa.pack()
        self.yla.pack()
        self.yla1.pack()
        self.keski.pack()
        self.ala.pack()
        self.painikkeet.pack()
        tkinter.mainloop()
        
    def lis_kirja(self):
        #Funktio lisää uuden kirjan ja sen tiedot tietojärjestelmään
        
        uusi_kirja = Kirja(self.kirja.get(), self.kirjailija.get(), self.varaus.get(), self.paiva.get())
        lisaa_kirja(self.kirjat, uusi_kirja)
        tkinter.messagebox.showinfo("Vastaus", "Kirja on lisätty/lainattu/palautettu")
        self.kirja.set('')
        self.kirjailija.set('')
        self.varaus.set('')
        self.paiva.set('')
        
        
    def etsi(self):
    #"Funktio etsii kirjan ja kirjan tiedot 
        etsittava = self.kirja.get()
    
        kirja = hae_kirja(self.kirjat, etsittava)
        #yrittää etsiä kirjantietoja jos ei löydy ilmoittaa käyttäjälle
        if kirja == None: 
            tkinter.messagebox.showinfo("Vastaus", "Kirjan tietoja ei löytynyt")
        else: 
            self.kirja.set(kirja.get_kirja())
            self.kirjailija.set(kirja.get_author())
            self.varaus.set(kirja.get_varaus())
            self.paiva.set(kirja.get_paiva())

    
    def lai_kirja(self):
        #Funktio varaa kirjan
        self.varaus.set("Varattu")
        
    def pal_kirja(self):
       #Funktio palauttaa kirjan
        self.varaus.set("Vapaa")
        
    def empty(self):
        # Tyhjennetään kentät
        self.kirja.set('')
        self.kirjailija.set('')
        self.varaus.set('')
        self.paiva.set('')

        
    def del_kirja(self):
       #Funktio poistaa kirjan tiedot 
        poistettava = self.kirja.get()
        poistettu = poista_kirja(self.kirjat, poistettava)
        #Ilmoittaa käyttäjää jos kirjaa ei ollut tietokannassa   
        if poistettu:
            tkinter.messagebox.showinfo("Vastaus", "Kirja on poistettu")
        else:
            tkinter.messagebox.showinfo("Vastaus", "Kirja ei ollut tietokannassa")
        self.empty()
   
     
    def tuhoa(self):
        #Funktio lopettaa ohjelman ja tallentaa ne binääritiedostoon
         tallenna_kirjat(self.kirjat)
         self.paa.destroy()
          
def main():
    #kutsuu funktiota joka lukee tiedoston
    kirja_tiedot = lue_tiedosto()
    
    kirjakanta = OmaGUI(kirja_tiedot)

main()
