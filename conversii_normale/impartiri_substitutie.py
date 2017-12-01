'''
Created on Nov 14, 2017

@author: Ancuta Hij
'''
from operatii_elementare.operatii import Operatii


class Conversii(Operatii):
    #                    *** ALGORITMUL DE IMPARTIRI SUCCESIVE ***
    @staticmethod
    def impartiriSuccesive(nr, baza):
        """
            Algoritmul de impartiri succesive dintr-o baza mai mica in alta baza mai mare

            :INPUTS: - nr- o instanta a clasei Operatii din modulul operatiiElementare.
                     - baza- baza in care vrem sa convertim numarul

            :OUTPUTS: rezultat- rezultatul convertirii numarului in baza ceruta.


            Daca nr=244(7), acesta va fi o instanta a clasei Operatii, deci se va afla sub forma Operatii([2,4,4],7)
            Unde:    [2,4,4]- sirul cifrelor numarului
                     7      - baza in care se afla numarul



            Algoritmul de impartiri succesive se foloseste de algoritmul de impartire a unui numar dat la o cifra.
            Se ia numarul dat si se imparte la baza in care vrem sa il convertim   ==>   cat+rest
            Se ia catul si se imparte la baza in care vrem sa convertim numarul    ==>   cat+rest
            ...............................
            Se ia catul si se imparte la baza in care vrem sa convertim numarul    ==>   0 si rest

            Resturile care se obtin se adauga in ordinea aparitiei lor intr-o lista numita rezultat.
            La final lista rezultat este inversata pentru a putea obtine rezultatul corect.

            ex:  173(8) -> ? (7)

            173(8): 7 = 21, rest 4 (ne-am folosit de algoritmul de impartire unui numar la o cifra)
                Se adauga progresiv resturile in lista rezultat
                rezultat= [4]
            21(8) : 7 = 2,  rest 3
                rezultat= [4,3]
            2(8)  : 7 = 0,  rest 2
                rezultat= [4,3,2]

            Lista rezultat este inversata pentru a obtine rezultatul corect.

        """
        rezultat = []

        while nr.getNumar() != [0]:
            lista = nr.impartire(baza)
            rezultat.append(lista[1])
            nr.setNumar(lista[0])

        return list(reversed(rezultat))




    #                *** ALGORITMUL DE SUBSTITUTIE ***


    def substitutie(nr, baza):
        """
             Algoritmul de conversie a unui numar dintr-o baza mai mica intr-o baza mai mare folosind metoda substitutiei.

            :INPUTS: - nr- o instanta a clasei Operatii din modulul operatiiElementare.
                     - baza- baza in care vrem sa convertim numarul

            :OUTPUTS: rezultat- rezultatul convertirii numarului in baza ceruta.


            Daca nr=244(7), acesta va fi o instanta a clasei Operatii, deci se va afla sub forma Operatii([2,4,4],7)
            Unde:    [2,4,4]- sirul cifrelor numarului
                     7      - baza in care se afla numarul

            Pentru numarul 332(6) -> ? (7)  ,avem lista cifrelor [3,3,2]
            Se parcurge lista cifrelor de la stanga spre dreapta
                            [3, 3 ,2]
            ordine puteri:  2  1   0
            Se imnulteste fiecare cifra cu baza in care se afla numarul curent  ridicata la o putere ( vezi ordinea puterilor).
            Trebuie sa fim atenti la faptul ca calculele se vor efectua in baza destinatie

            rezultat= 3*6^2 + 3*6 + 2
            6^2 in baza 7 va fi egal cu 51 (ne folosim de algoritmul de inmultire a unui numar cu o cifra)
            rezultat= 3*51 + 3*6 + 2
            3*51 in baza 7 va fi egal cu 213
            3*6 in baza 7 va fi egal cu 24
            rezultat= 213 + 24 +2  (ne folosim de algoritmul de adunare a doua numere in aceeasi baza de numeratie)
            rezultat = 213+ 26= 242 (7)

        """

        rezultat=Operatii([0],baza)

        listaCifre = nr.getNumar()
        for index in range(len(listaCifre)):
            x=Operatii([nr.getBaza()],baza )   #baza= baza in care vrem sa trecem numarul
            if index ==len(listaCifre)-1:
                x=Operatii([1], baza)
            else:
                for putere in range(len(nr.getNumar())-index-2,0,-1):
                    x=Operatii.inmultire(x,nr.getBaza())
                    x=Operatii(x,baza)

            x=Operatii.inmultire(x,listaCifre[index])
            x=Operatii(x,baza)
            rezultat=Operatii.adunare(x,rezultat)
            rezultat=Operatii(rezultat,baza)

        x=rezultat.getNumar()


        return rezultat.getNumar()

    #                       *** ALGORITMUL DE CONVERSIE UTILIZAND O BAZA INTERMEDIARA ***

    @staticmethod
    def conversieBazaIntermediara(numar, baza):
        """
            Algoritmul de conversie a unui numar dintr-o baza data in alta baza folosind o baza intermediara.

            :INPUTS: - nr- o instanta a clasei Operatii din modulul operatiiElementare.
                     - baza- baza in care vrem sa convertim numarul

            :OUTPUTS: rezultat- rezultatul convertirii numarului in baza ceruta.


            Daca nr=244(7), acesta va fi o instanta a clasei Operatii, deci se va afla sub forma Operatii([2,4,4],7)
            Unde:    [2,4,4]- sirul cifrelor numarului
                     7      - baza in care se afla numarul

            Algoritmul converteste numarul in baza 10 folosindu-se de metoda substitutiei. Calculele se realizeaza in baza destinatie
            173(8) -> 123(10)
            In acest caz baza destinatie este baza 10, iar baza sursa este baza 8.

            Urmatorul pas al algoritmului este convertirea numarului din baza intermediara, in baza destinatie.
            In acest caz se folosete metoda prin impartiri succesive, unde calculele se fac in baza sursa.
            123(10) -> 234(7)
            Baza sursa este baza 10, iar baza destinatie este baza 7.
        """

        rezultat=0
        listaCifre=numar.getNumar()
        for index in range(len(listaCifre)):
            rezultat+=listaCifre[index]*(numar.getBaza()**(len(listaCifre)-index-1))

        cat=rezultat
        rezultat=[]
        while cat>0:
            rezultat.append(cat%baza)
            cat=cat//baza
        if rezultat== []:
            return [0]
        return  list(reversed(rezultat))

