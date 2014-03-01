# -*- coding:Utf-8 -*-
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

from tkinter import *
import sys
#sys.path.append("C:\\Documents and Settings\\Utilisateur\\Mes documents\\Dropbox\\Prive\\02_PERSO\\01_INFORMATIQUE\\PYTHON\\PYTHON_TRAVAIL\\CRYPTO")
from CodeCesar import *

class TkCrypto(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Code César")
        # Code César
        self.machine=CodeCesar()
        # Column 0
        self.textDLabel=Label(self,text="texte décodé")
        self.textDtext=Text(self,background='grey')
        # Column 1
        self.clefLabel=Label(self,text="clef")
        self.clef=Spinbox(self,text="clef",from_=0, to=self.machine.getClefMax())
        self.coder=Button(self,text="coder",command=self.code)
        self.decoder=Button(self,text="décoder",command=self.decode)
        # Column 2
        self.textClabel=Label(self,text="texte codé")
        self.textCtext=Text(self,background='grey')
        # Layout column 0
        self.textDLabel.grid(column=0, row=0)
        self.textDtext.grid(column=0, row=1, rowspan=3)
        # Layout column 1
        self.clefLabel.grid(column=1, row=0)
        self.clef.grid(column=1, row=1,sticky=N)
        self.coder.grid(column=1, row=2)
        self.decoder.grid(column=1, row=3)
        # Layout column 2
        self.textClabel.grid(column=2, row=0)
        self.textCtext.grid(column=2, row=1, rowspan=3)
    def code(self):
        # nombre de lignes + 1
        self.nLigneD = int(self.textDtext.index('end').split('.')[0])
        self.nLigneC = int(self.textCtext.index('end').split('.')[0])
        # effacement
        self.textCtext.delete("1.0",END)
        # traduction
        for self.i in range(1,self.nLigneD):
            self.textD=self.textDtext.get(str(self.i)+".0",str(self.i)+".end")
            self.textC=self.machine.code(int(self.clef.get()),self.textD)
            self.textCtext.insert(str(self.i)+".0",self.textC)
            self.textCtext.insert(str(self.i)+".end","\n")
    def decode(self):
        # nombre de lignes + 1
        self.nLigneC = int(self.textCtext.index('end').split('.')[0])
        self.nLigneD = int(self.textDtext.index('end').split('.')[0])
        # effacement
        self.textDtext.delete("1.0",END)
        # traduction
        for self.i in range(1,self.nLigneC):
            self.textC=self.textCtext.get(str(self.i)+".0",str(self.i)+".end")
            self.textD=self.machine.decode(int(self.clef.get()),self.textC)
            self.textDtext.insert(str(self.i)+".0",self.textD)
            self.textDtext.insert(str(self.i)+".end","\n")

if __name__ == '__main__':
    fen=TkCrypto()
    fen.mainloop()
    try:
        fen.destroy()
        print("Fin")
    except:
        print("Fin")
