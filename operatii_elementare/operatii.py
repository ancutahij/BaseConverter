'''
Created on Nov 12, 2017

@author: Ancuta
'''


# from numar.numar import Numar
from numar.numar import Numar


class Operatii(Numar):
    def __init__(self, numar, baza):
        super().__init__(numar, baza)
        self.transport = 0

    def getNumar(self):
        return self.numar

    def getBaza(self):
        return self.baza

    def getTransport(self):
        return self.transport

    def setNumar(self, newNumar):
        self.numar = newNumar

    def __repr__(self):
        return "Numarul este {}".format(self.numar)

    #                          *** ALGORITMUL DE ADUNARE A DOUA NUMERE IN ACEEASI BAZA ***
    def adunare(self, other):
        '''
            Algoritmul de adunare a doua numere in aceeasi baza.
            Numerele reprezinta instante ale clasei Numar.

            ex: Daca avem numarul x=1246(7), el se gaseste sub forma unei instante in clasa Numar:   x=Numar([1,2,4,6],7)

            input:
                    self- reprezinta o instanta caracterizata prin sirul cifrelor care compun un numar si baza in care se afla numarul
                    other- o alta instanta caracterizata de aceleasi atribute

            output: rezultatul va fi tot o instanta a clasei numar si reprezinta adunarea celor 2 numere.

        '''

        rezultat = []
        self.transport = 0
        for digit1, digit2 in zip(reversed(self.numar), reversed(other.numar)):
            rezultat.append((digit1 + digit2 + self.transport) % self.baza)
            self.transport = (digit1 + digit2 + self.transport) // self.baza

        if len(self.numar) < len(other.numar):
            for digit in (other.numar[len(other.numar) - len(self.numar) - 1::-1]):  # cifrele ramase libere adaugate si ele la rezultat
                rezultat.append((digit + self.transport) % self.baza)
                self.transport = (digit + self.transport) // self.baza
            if self.transport > 0:
                rezultat.append(self.transport)

        elif len(other.numar) < len(self.numar):
            for digit in (self.numar[len(self.numar) - len(
                    other.numar) - 1::-1]):  # cifrele ramase libere sunt adaugate si ele la rezultat, se tine cont de transport
                rezultat.append((digit + self.transport) % self.baza)
                self.transport = (digit + self.transport) // self.baza
            if self.transport > 0:
                rezultat.append(self.transport)

        else:
            if self.transport > 0:
                rezultat.append(self.transport)

        rezultat = list(reversed(rezultat))
        return rezultat

    #                            *** ALGORITMUL DE SCADERE A DOUA NUMERE IN ACEEASI BAZA ***
    def scadere(self, other):

        '''
            Algoritmul de scadere a doua numere in aceeasi baza (2-16).
            Numerele reprezinta instante ale clasei Numar.

            ex:   Daca avem numarul x=1246(7), el se gaseste sub forma unei instante in clasa Numar:   x=Numar([1,2,4,6],7)


           input:
                    self- reprezinta o instanta caracterizata prin sirul cifrelor care compun un numar si baza in care se afla numarul
                    other- o alta instanta caracterizata de aceleasi atribute

            output: rezultatul va fi tot o instanta a clasei numar si reprezinta adunarea celor 2 numere.
        '''
        self.transport = 0
        rezultat = []
        for digit1, digit2 in zip(reversed(self.numar), reversed(other.numar)):
            if digit2 - digit1 + self.transport < 0:
                rezultat.append(self.transport + self.baza + digit2 - digit1)
                self.transport = -1
            else:
                rezultat.append(digit2 - digit1 + self.transport)
                self.transport = 0

        if len(other.numar) > len(self.numar):
            for digit in (other.numar[len(other.numar) - len(self.numar) - 1::-1]):
                if self.transport+digit<0:
                    rezultat.append(self.transport + digit+self.baza)
                    self.transport = -1
                else:
                    rezultat.append(self.transport+digit)
                    self.transport=0

        rezultat=list(reversed(rezultat))
        while rezultat[0]==0:
            rezultat=rezultat[1:]
        return rezultat

    #                                    *** Algoritmul de inmultire a unui numar dat cu o cifra***:

    def inmultire(self, digit):
        '''

            Algoritmul de inmultire a unui numar cu o cifra intr-o baza data.
            Numerele reprezinta instante ale clasei Numar.

                ex:   Daca avem numarul x=1246(7), el se gaseste sub forma unei instante in clasa Numar:   x=Numar([1,2,4,6],7)

            :INPUTS:   self- reprezinta o instanta caracterizata prin sirul cifrelor care compun un numar si baza in care se afla numarul
                       digit- cifra cu care se va inmulti numarul

            :OUTPUTS:   rezultat- rezultatul inmultirii numarului cu o cifra data
        '''
        self.transport = 0
        rezultat = []
        for digitNr in reversed(self.numar):
            rezultat.append((self.transport + digit * digitNr) % self.baza)
            self.transport = (self.transport + digit * digitNr) // self.baza
        if self.transport != 0:
            rezultat.append(self.transport)
        return list(reversed(rezultat))

    #                        *** Algoritmul de impartire a unui numar dat la o cifra. ***
    def impartire(self, digit):
        '''
            Algoritmul de impartire a unui numar dat  la o cifra intr-o baza data.
            Numerele reprezinta instante ale clasei Numar.

                    ex:   Daca avem numarul x=1246(7), el se gaseste sub forma unei instante in clasa Numar:   x=Numar([1,2,4,6],7)


            :INPUTS:   self- reprezinta o instanta caracterizata prin sirul cifrelor care compun un numar si baza in care se afla numaruL

            :OUTPUTS:  rezultat- rezultatul impartirii numarului la o cifra data

        '''

        cat = []

        self.transport = 0
        for digitNr in self.numar:
            cat.append((self.transport * self.baza + digitNr) // digit)
            self.transport = (self.transport * self.baza + digitNr) % digit
        while cat[0] == 0 and len(cat) > 1:
            cat = cat[1:]
        return [cat, self.transport]

