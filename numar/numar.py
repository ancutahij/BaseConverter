'''
Created on Nov 12, 2017

@author: Ancuta Hij
'''


class Numar():
    """
        Clasa Numar are ca atribute pe "numar", ce reprezinta un numar sub forma unui sir de cifre, cifra maxima din sirul cifrelor este baza-1.
        Al doilea atribut este baza, care sugereaza in ce baza de numeratie se afla numarul(2-16).
    """

    def __init__(self, numar=None, baza=None):
        if numar is None:
            self.numar = []
        else:
            self.numar = numar
        if baza is None:
            self.baza = 10
        else:
            self.baza = baza

    def getNumar(self):
        return self.numar

    def getBaza(self):
        return self.baza



    def setNumar(self, newNumar):
        self.numar = newNumar

    def setBaza(self, newBase):
        self.baza = newBase



