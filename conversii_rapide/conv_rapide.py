'''
Created on Nov 13, 2017

@author: Ancuta Hij
'''
from numar.numar import Numar


class Conversie():
    @staticmethod
    def getNumar(numar, lungime, sens):
        '''

            Algoritmul are 2 sensuri:

               *Daca sens==1 inseamna ca noi convertim din baza 2 in baza 4, 8 sau 16.
                Ca input pentru numar va fi un numar binar  de forma unei liste ( de exemplu 11(2)==[1,1]==3(4) )
                Lungimea se refera la puterile lui 2:
                    4=2^2 ->  lungime== 2
                    8=2^3 ->  lungime== 3
                    16=2^4 -> lungime ==4

                Chiar daca in dictionarul posibilitati avem ca cheie un numar in baza 16, iar ca valoare avem echivalentul in baza 2, putem observa faptul ca:
                    -pentru {'0':[0,0,0,0],'1':[0,0,0,1],'2':[0,0,1,0],'3':[0,0,1,1]} avem : - toate cheiile exista in baza 4
                                                                                             - iar ultimele 2 elemente din fiecare valoare reprezinta
                                                                                               corespondentul cheii in baza 2

                    de exemplu: 1(4)=01(2)
                    Daca ne uitam la ultimele 2 elemente din valoarea de la cheia "1" ( [0,0,0,1] ) observam ca [0,1] reprezinta numarul nostru in baza 2.

                Analog pentru baza 8 .
                In baza 16 nu e nevoie sa alegem o portiune de lista. Se ia intreaga valoare.


                * Daca sens este diferit de 1 atunci inseamna ca noi convertim din baza 4,8 sau 16 in baza 2.
                 Ca input pentru numar va fi un numar in baza 4, 8 sau 16
                 Lungimea se refera la puterile lui 2:
                    4=2^2 ->  lungime== 2
                    8=2^3 ->  lungime== 3
                    16=2^4 -> lungime ==4

                Algoritmul are urmatorul efect: Strabatem numarul dat cifra cu cifra de la stanga spre dreapta. Strabatem dictionarul pana cand cifra
                numarului este egala cu o cheie a dictionarului. Intr-o variabila numita rezultat, vom adauga progresiv echivalentul cifrei din baza data
                in baza 2.
                exemplu: daca convertim din baza 8 in baza 2: avem cifra 7(8) => cheia este 7, valoarea este [0,1,1,1], dar pentru ca noi lucram in baza 8=2^3
                , ne intereseaza doar 3 cifre.  [1,1,1]

        '''
        posibilitati = {'0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1], '4': [0, 1, 0, 0],
                        '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1], '8': [1, 0, 0, 0], \
                        '9': [1, 0, 0, 1], 'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1], 'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1],
                        'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}

        if sens == 1:
            for key, value in posibilitati.items():
                if value[4 - lungime:] == numar:
                    return key
        else:
            rezultat = []

            for digit in numar:
                for key, value in posibilitati.items():
                    if digit.upper() == key:
                        rezultat.extend(value[4 - lungime:])
                        break
            return rezultat

    @staticmethod
    def getGrupuri(numarList, grup):

        l = []
        list = []
        start = 0
        if len(numarList) % grup != 0:
            for i in range(grup):
                list.append(0)
            start = len(numarList) % grup
            for i in range(len(numarList) % grup):
                list[grup - len(numarList) % grup + i] = numarList[i]
            l.append(list)

        for i in range(start, len(numarList), grup):
            l.append(numarList[i:i + grup])

        return l
    @staticmethod
    def fromString_toInt(list):
        return [int(
            i) if i.isdigit() else 10 if i.upper() == 'A' else 11 if i.upper() == 'B' else 12 if i.upper() == 'C' else 13 if i.upper() == 'D' \
            else 14 if i.upper() == 'E' else 15 for i in list]

    @staticmethod
    def Base2to4(nr):
        '''
            Algoritimul de convertire a unui numar din baza 2 in baza 4.
            Numerele reprezinta instante ale clasei Numar.

            ex: Daca avem numarul x=101011(2), el se gaseste sub forma unei instante in clasa Numar:   x=Numar([1,0,1,0,1,1],2)

            Daca avem x=101011(2) si vrem sa il trecem in baza 4 se grupeaza cifrele in grupuri de cate doua cifre de la dreapta stanga
            ex :x=101011(2)    =>   [1,0],[1,0],[1,1]

            ex: x=1010111(2)    =>  [0,1],[0,1],[0,1],[1,1]
                Pentru ca nu putem grupa cifrele in grupuri de cate doua cifre, adaugam 0 in fata pana cand putem grupa cifrele in grupuri de cate doua.

            Pentru fiecare grup de cifre format, functia getNumar returneaza numarul corespunzator in baza ceruta.
            [1,0]=2    [1,0]=2    [1,1]=3

            La final toate cifrele sunt adaugate in lists rezultat.

            rezultat=[2,2,3]
        '''
        grupuri = Conversie.getGrupuri(nr.getNumar(), 2)
        rezultat = []
        for grup in grupuri:
            rezultat.append(Conversie.getNumar(grup, 2, 1))

        return Conversie.fromString_toInt(rezultat)

    @staticmethod
    def Base2to8(nr):
        """
            Principiul de functionare al algoritmului e acelasi ca cel de la Functia Base2to4.
            Se recomanda a se citi intructiunile de acolo.

        """
        grupuri = Conversie.getGrupuri(nr.getNumar(), 3)
        rezultat = []
        for grup in grupuri:
            rezultat.append(Conversie.getNumar(grup, 3, 1))
        return Conversie.fromString_toInt(rezultat)

    @staticmethod
    def Base2to16(nr):
        """
            Principiul de functionare al algoritmului e acelasi ca cel de la Functia Base2to4.
            Se recomanda a se citi intructiunile de acolo.

        """
        grupuri = Conversie.getGrupuri(nr.getNumar(), 4)
        rezultat = []
        for grup in grupuri:
            rezultat.append(Conversie.getNumar(grup, 4, 1))

        return Conversie.fromString_toInt(rezultat)


    @staticmethod
    def convertor(list):
        """
            Converteste o lista din [1,5,10] in ['1', '5', 'A']

        """
        return [str(x) if x<10 else "A" if x==10 else "B" if x==11 else "C" if x==12 else "D" if x==13 else "E" if x==14 else "F" for x in list]
    @staticmethod
    def Base4to2(nr):

        rezultat = Conversie.getNumar(Conversie.convertor(nr.getNumar()), 2, -1)
        return rezultat

    @staticmethod
    def Base8to2(nr):
        rezultat = []
        rezultat = Conversie.getNumar(Conversie.convertor(nr.getNumar()), 3, -1)
        return rezultat

    @staticmethod
    def Base16to2(nr):
        rezultat = []
        rezultat = Conversie.getNumar(Conversie.convertor(nr.getNumar()), 4, -1)
        return rezultat


