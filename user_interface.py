'''
Created on Nov 12, 2017

@author: Ancuta Hij
'''
import os
from conversii_normale.impartiri_substitutie import Conversii
from numar.numar import Numar
from operatii_elementare.operatii import Operatii
from user_interface_validator import Validator
from conversii_rapide.conv_rapide import Conversie
from conversii_rapide import tests
from conversii_normale import tests
from numar import tests
from operatii_elementare import tests

class Console(Numar):
    def __init__(self, numar=None, baza=None):
        super().__init__(numar, baza)
        self.runUI()

    @staticmethod
    def fromString_toList(numar):
        """
            Se da un numar pozitiv si se converteste in sirul cifrelor.
            Toate datele sunt validate de inainte.

            ex: numar=12AF(16) se returneaza [1,2,10,15]

            :INPUTS:
                -numar: numarul care trebuie convertit

            :OUTPUTS:
                -numarul convertit sub forma de lista

        """
        #return [int(
        #    i) if i.isdigit() else 10 if i.upper() == 'A' else 11 if i.upper() == 'B' else 12 if i.upper() == 'C' else 13 if i.upper() == 'D' \
        #    else 14 if i.upper() == 'E' else 15 for i in numar]


        list= [int(
        i) if i.isdigit() else 10 if i.upper() == 'A' else 11 if i.upper() == 'B' else 12 if i.upper() == 'C' else 13 if i.upper() == 'D' \
        else 14 if i.upper() == 'E' else 15 if i.upper() == 'F' else "*" for i in numar]
        if "*" in list:
            raise ValueError ("\n           Numarul trebuie sa se afle in baza citita si sa fie pozitiv. \n".upper())
        return list


    @staticmethod
    def fromList_toString(list):
        """
            Se da o lista care reprezinta lista cifrelor unui numar si se returneaza string-ul caracteristic.
            Toate datele sunt validate de inainte.

            ex: Nu exista in lista cifrelor elemente mai mari ca 15 sau mai mici ca 0

        :param list: lista cifrelor unui numar
        :return:     string-ul caracteristic
        """
        while len(list)>1 and list[0]==0:
            list=list[1:]

        rezultat=""
        for digit in list:
            if digit<10:
                rezultat+=str(digit)
            elif digit==10:
                rezultat+='A'
            elif digit == 11:
                rezultat += 'B'
            elif digit == 12:
                rezultat += 'C'
            elif digit == 13:
                rezultat += 'D'
            elif digit == 14:
                rezultat += 'E'
            else:
                rezultat+='F'

        return rezultat


    @staticmethod
    def citesteInstanta(baza=None):
        """
            Citeste o instanta din clasa Numar (se citeste o baza si un numar)
        """
        while True:
            try:
                if baza is None:
                    while  True:
                        try:
                            baza = input("Citeste o baza sursa de la 2 la 16 in care vrei sa se afle numarul: ")
                            Validator.eBazaValida(baza)
                            baza = int(baza)
                            break
                        except ValueError as msg:
                            print(msg)

                numar = input("Citeste un numar natural care se afla in baza citita anterior: ")
                numar = Console.fromString_toList(numar)
                Validator.eNumarValid(Numar(numar, baza))
                break
            except ValueError as msg:
                print(msg)

        return [numar, baza]



    @staticmethod
    def citesteCifra(baza):
        """
            Citeste o cifra care se afla in aceeasi baza ca numarul.
        """
        while True:
            try:
                cifra = (input("Citeste o cifra care se afla in aceeasi baza ca numarul citit anterior: "))
                Validator.eCifraValida(cifra,baza)
                cifra=Console.fromString_toList(cifra)

                break

            except ValueError as msg:
                print(msg)
        return cifra[0]

    @staticmethod
    def converteste(numar, baza):
        """
            Se converteste un numar dintr-o baza data in alta baza, folosindu-se baza intermediara 10
        :param numar:   numarul de convertit
        :param baza:    baza in care vrem sa convertim numarul
        :return:        numarul convertit in baza ceruta
        """
        if numar.getBaza()!= baza:
            numar=Conversii.conversieBazaIntermediara(numar,baza)
            numar=Operatii(numar,baza)
        return numar

    @staticmethod
    def adunare():
        """
           Adunarea a doua numere naturale intr-o baza citita de la tastatura(2-16).
           Numerele pot sa fie in aceeasi baza sau nu.
        """
        print  ("\nPrimul numar: ".upper())
        numar1 = Console.citesteInstanta()
        numar1 = Operatii(numar1[0], numar1[1])

        print  ("\nAl doilea numar: ".upper())
        numar2 = Console.citesteInstanta()
        numar2 = Operatii(numar2[0], numar2[1])

        print ("\nBaza destinatie: ".upper())
        baza =Console.citesteBaza("Citeste o baza destinatie de la 2 la 16 in care vrei sa se afle rezultatul: ")

        nr1 = Console.fromList_toString(numar1.getNumar())
        nr2 = Console.fromList_toString(numar2.getNumar())
        baza1 = numar1.getBaza()
        baza2 = numar2.getBaza()

        numar1=Console.converteste(numar1,baza)
        numar2=Console.converteste(numar2,baza)




        return "\nREZULTAT: {}({}) + {}({}) = {}({})".format(nr1, baza1, nr2, baza2,Console.fromList_toString(Operatii.adunare(numar1,numar2)), baza )
        #return "Rezultatul adunarii este: {}".format(Console.fromList_toString(Operatii.adunare(numar1,numar2)))

    @staticmethod
    def scadere():
        """
            Scaderea a noua numere in baze identice sau diferite, si afisarea rezultatului intr-o a treia baza.
            Se face verificarea ca descazutul sa fie mai mare decat scazatorul, altfel utilizatorul este atentionat cu un mesaj.
        """
        print("\nDescazutul: ".upper())
        numar1 = Console.citesteInstanta()
        numar1 = Operatii(numar1[0], numar1[1])

        while True:
            try:

                print("\nScazatorul: ".upper())
                numar2 = Console.citesteInstanta()
                numar2 = Operatii(numar2[0], numar2[1])
                print("\nBaza destinatie: ".upper())
                baza = Console.citesteBaza("Cisteste o baza in care vrei sa se afle rezultatul: ")

                nr1 = Console.fromList_toString(numar1.getNumar())
                nr2 = Console.fromList_toString(numar2.getNumar())
                baza1 = numar1.getBaza()
                baza2 = numar2.getBaza()

                numar1 = Console.converteste(numar1, baza)
                numar2 = Console.converteste(numar2, baza)
                Validator.compare(numar1.getNumar(), numar2.getNumar())
                break
            except ValueError as msg:
                print (msg)



        #return "Rezultatul scaderii este: {}".format(Console.fromList_toString(Operatii.scadere(numar2, numar1)))
        return "\nREZULTAT: {}({}) - {}({}) = {}({})".format(nr1, baza1, nr2, baza2,Console.fromList_toString(Operatii.scadere(numar2,numar1)), baza )



    @staticmethod
    def inmultire():
        """
            Inmulteste un numar  care se afla intr-o baza de la 2 la 16, cu o cifra care se afla in aceeasi baza ca numarul.
        """
        print("\nNumarul: ".upper())
        numar = Console.citesteInstanta()
        numar = Operatii(numar[0], numar[1])
        nr = Console.fromList_toString(numar.getNumar())
        baza =numar.getBaza()

        print("\nCifra: ".upper())
        cifra=Console.citesteCifra(numar.getBaza())

        #return "Rezultatul inmultirii este: {}".format(Console.fromList_toString(Operatii.inmultire(numar,cifra)))
        return "\nREZULTAT: {}({}) * {}({}) = {}({})".format(nr, baza, cifra, baza,Console.fromList_toString(Operatii.inmultire(numar, cifra)), baza )


    @staticmethod
    def impartire():
        """
            Imparteste un numar care se afla intr-o baza de la 2 la 16, la o cifra care se afla in aceeazi baza ca numarul.

        """
        print("\nNumarul: ".upper())
        numar = Console.citesteInstanta()
        numar = Operatii(numar[0], numar[1])

        nr = Console.fromList_toString(numar.getNumar())
        baza = numar.getBaza()

        while True:

            print("\nCifra: ".upper())
            cifra = Console.citesteCifra(numar.getBaza())
            if cifra==0:
                print ("\n           Cifra trebuie sa fie diferita de 0.\n".upper())
            else:
                break

        rez=Operatii.impartire(numar,cifra)
        #return "Catul impartirii este {}, iar restul este {}".format(Console.fromList_toString(cifra[0]), cifra[1])
        return "\nREZULTAT: {}({}) / {}({}) = {} rest {}".format(nr, baza, cifra, baza, Console.fromList_toString(rez[0]), rez[1])


    @staticmethod
    def citesteBaza(mesaj, mesaj2="\n           Baza trebuie sa fie un numar intre 2 si 16 \n".upper(), minim=2, maxim=16):
        """
            Citeste o baza intre 2 si 16.
        """
        while True:
            try:
                baza = (input(mesaj))  # "Citeste o baza de la 2 la 16 in care vrei sa se afle rezultatul: "))
                Validator.eBazaValida(baza,mesaj2, minim, maxim, )
                break

            except ValueError as msg:
                print(msg)
        return int(baza)

    @staticmethod
    def substitutie():
        """

            Apeleaza functiile de converitire a unui numar dintr-o baza mai mica intr-o alta mare prin substitutie.
        """


        print("\nNumarul: ".upper())
        mesaj_citire="Citeste o baza strict mai mica decat 16: "
        mesaj_atentionare="\n           Baza sursa trebuie sa fie un numar strict mai mic decat 16, dar mai mare sau egal decat 2\n".upper()
        baza=Console.citesteBaza(mesaj_citire, mesaj_atentionare, 2, 15)
        numar = Console.citesteInstanta(baza)
        numar = Operatii(numar[0], numar[1])
        nr=Console.fromList_toString(numar.getNumar())
        bz= numar.getBaza()

        print("\nbaza destinatie: ".upper())
        mesaj1="Citeste o baza mai mare decat baza data in care vrei sa fie convertit numarul: "
        mesaj2="\n           Baza trebuie sa fie un numar mai mare decat baza numarului citit si mai mica  sau egala decat 16\n".upper()
        baza=Console.citesteBaza(mesaj1, mesaj2,  numar.getBaza(), 16)

        numar=Conversii.substitutie(numar, baza)
        #return "Rezultatul este: {}".format(Console.fromList_toString(numar))
        return "\nREZULTAT: {}({})  = {}({})".format(nr, bz,Console.fromList_toString(numar), baza )

    @staticmethod
    def impartiriSuccesive():
        """
            Citeste o baza si un numar in acea baza
            Citeste baza destinatie, baza care este mai mica decat baza in care a fost citit numarul
            Gesticuleaza procesul de convertire a numarul in baza destinatie folosind algoritmul de impartiri succesive

        """
        print("\nNumarul: ".upper())
        mesaj_citire = "Citeste o baza strict mai mare decat 2: "
        mesaj_atentionare = "\n           Baza sursa trebuie sa fie un numar strict mai mare decat 2, dar mai mic decat egal decat 16\n".upper()
        baza = Console.citesteBaza(mesaj_citire, mesaj_atentionare, 3, 16)
        numar = Console.citesteInstanta(baza)
        numar = Operatii(numar[0], numar[1])
        nr = Console.fromList_toString(numar.getNumar())
        bz = numar.getBaza()

        print("\nbaza destinatie: ".upper())
        mesaj1 = "Citeste o baza mai mica decat baza sursa in care vrei sa fie convertit rezultatul: "
        mesaj2 = "\n           Baza trebuie sa fie un numar mai mic decat baza numarului citit si mai mare egala decat 2\n".upper()
        baza = Console.citesteBaza(mesaj1, mesaj2, 2, numar.getBaza())

        numar=Conversii.impartiriSuccesive(numar, baza)
        #return "Rezultatul este: {}".format(Console.fromList_toString(numar))
        return "\nREZULTAT: {}({})  = {}({})".format(nr, bz,Console.fromList_toString(numar), baza )

    @staticmethod
    def bazaIntermediara():

        """
            Citeste o baza(2-16) si un numar in aceeasi baza
            Citeste o baza destinatie cuprinsa intre 2 si 16
            Gesticuleaza procesul de convertire a numarului folosindu-se de algoritmul de convertire folosind o baza intermediara
        :return:
        """

        print("\nNumarul: ".upper())
        numar = Console.citesteInstanta()
        numar = Operatii(numar[0], numar[1])
        nr = Console.fromList_toString(numar.getNumar())
        bz = numar.getBaza()

        print("\nbaza destinatie: ".upper())
        baza =Console.citesteBaza("Citeste o baza de la 2 la 16 in care vrei sa se afle numarul: ")

        numar=Conversii.conversieBazaIntermediara(numar,baza)
        #return "Rezultatul este: {}".format(Console.fromList_toString(numar))
        return "\nREZULTAT: {}({})  = {}({})".format(nr, bz,Console.fromList_toString(numar), baza )


    @staticmethod
    def citireBazaConversiiDirecte():
        while True:
            try:
                baza=input("Alege una din bazele 2, 4, 8 sau 16: ")
                Validator.eBazaValidaConversiiDirecte(baza)
                baza=int(baza)
                return baza
            except ValueError as msg:
                print (msg)


    @staticmethod
    def conversiiDirecte():
        print ("\nNumarul: ".upper())
        numar =Console.citesteInstanta(Console.citireBazaConversiiDirecte())
        numar =Numar(numar[0], numar[1])
        nr = Console.fromList_toString(numar.getNumar())
        bz = numar.getBaza()

        print ("\nBaza:".upper())
        baza=Console.citireBazaConversiiDirecte()
        if numar.getBaza()!=baza:
            if numar.getBaza()==2:
                if baza==4:
                    numar=Conversie.Base2to4(numar)
                elif baza==8:
                    numar=Conversie.Base2to8(numar)
                else:
                    numar=Conversie.Base2to16(numar)
            elif numar.getBaza()==4:
                if baza==2:
                    numar=Conversie.Base4to2(numar)
                elif baza==8:
                    numar=Conversie.Base4to2(numar)
                    numar=Numar(numar,2)
                    numar=Conversie.Base2to8(numar)
                else:
                    numar=Conversie.Base4to2(numar)
                    numar = Numar(numar, 2)
                    numar=Conversie.Base2to16(numar)
            elif numar.getBaza()==8:
                if baza==2:
                    numar=Conversie.Base8to2(numar)
                elif baza==4:
                    numar=Conversie.Base8to2(numar)
                    numar = Numar(numar, 2)
                    numar=Conversie.Base2to4(numar)
                else:
                    numar=Conversie.Base8to2(numar)
                    numar = Numar(numar, 2)
                    numar=Conversie.Base2to16(numar)
            else:
                if baza==2:
                    numar=Conversie.Base16to2(numar)
                elif baza==4:
                    numar=Conversie.Base16to2(numar)
                    numar = Numar(numar, 2)
                    numar=Conversie.Base2to4(numar)
                else:
                    numar=Conversie.Base16to2(numar)
                    numar = Numar(numar, 2)
                    numar=Conversie.Base2to8(numar)


            #return "Rezultatul este: {}".format(Console.fromList_toString(numar))
            return "\nREZULTAT: {}({})  = {}({})".format(nr, bz, Console.fromList_toString(numar), baza)

        return "\n           Baza sursa nu poate fi egala cu baza destinatie\n".upper()

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def menuOperatii():
        menu="""
        
                              ===== MENU OPERATII =====
    1. Adunarea a doua numere naturale din baze identice/diferite intr-o a treia baza aleasa de utilizator
    2. Scaderea a doua numere naturale din baze identice/diferite intr-o a treia baza
    3. Inmultirea unui numar cu o cifra in aceeasi baza ca numarul.
    4. Impartirea unui numar la o cifra care se afla in aceeasi baza ca numarul.
    0. Intoarcere la meniul principal
    
   
    
        """
        optiuni = {"1": Console.adunare, "2": Console.scadere, "3": Console.inmultire, "4": Console.impartire}
        while True:

            print(menu)
            try:
                op = input("Alege optiune: ")
                if op == "0":

                    break
                else:
                    #Console.cls()
                    print(optiuni[op]())
                    print (" ")

            except KeyError:
                print("\n           Optiune invalida. \n".upper())


    @staticmethod
    def menuConversii():
        menu="""
        
                ====== MENU CONVERSII ======
        1.  Conversia unui numar dintr-o baza mai mica in alta mai mare prin substitutie. 
        2.  Conversia unui numar dintr-o baza mai mare in alta mai mica prin impartiri succesive.
        3.  Conversia unui numar intr-o baza folosindu-se baza intermediara 10.
        4.  Conversii rapide intre bazele 2, 4, 8 si 16.
        0.  Intoarcere la meniul principal   
          
"""
        optiuni={"1":Console.substitutie, "2":Console.impartiriSuccesive, "3":Console.bazaIntermediara,"4":Console.conversiiDirecte}
        while True:
            print(menu)
            try:
                op = input("Alege optiune: ")
                if op == "0":

                    break
                else:
                    print(optiuni[op]())
            except KeyError:
                print("\n           Optiune invalida. \n".upper())
    @staticmethod
    def runUI():

        menu="""
      =====MENU PRINCIPAL====
    1. Operatii in diferite baze
    2. Conversii
    0. Iesire 
        """
        optiuni = {"1":Console.menuOperatii,"2":Console.menuConversii}
        while True:
            print(menu)
            try:
                op = input("Alege optiune: ")
                if op == "0":
                    print("La revedere")
                    break
                else:
                    optiuni[op]()
            except KeyError:
                print("\n           Optiune invalida. \n".upper())




x=Console()