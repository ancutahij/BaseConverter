'''
Created on Nov 12, 2017

@author: Ancuta
'''

from numar.numar import Numar


class Validator():
    """
        Aceasta clasa are rolul de a valida datele care se citesc.

    """

    @staticmethod
    def eNumarValid(numar):
        """
            Face verificarea daca un numar dat se afla intr-o baza data.
        """
        for cifra in numar.getNumar():
            if cifra >= numar.getBaza():
                raise ValueError("\n        Numarul trebuie sa fie in baza citita si sa fie natural \n".upper())

    @staticmethod
    def eBazaValida(baza,mesaj2="\n        Baza trebuie sa fie un numar intre 2 si 16 \n".upper(), minim=2, maxim=16):
        """
            Verifica daca o baza este sau nu valida.
            Asta inseamna ca baza trebuie sa fie un numar cuprins intre 2 si 16, inclusiv
        """
        if not baza.isdigit():
            raise ValueError(mesaj2)
        if int(baza) < minim or int(baza) > maxim:
            raise ValueError(mesaj2)



    @staticmethod
    def eCifraValida(cifra, baza):
        """
            Verifica daca cifra citita se afla in baza data.
        :param cifra: cifra pe care o verificam
        :param baza: baza in care trebuie sa se afle cifra
        :return:
        """
        if cifra.isdigit():
            if int(cifra)>=baza:
                raise ValueError("\n          Cifra trebuie sa se afle in aceeasi baza ca numarul.\n".upper())
            elif int (cifra)>9:
                raise ValueError("\n          Cifra trebuie sa fie de forma A, B, C, D, E sau F \n".upper())
        else:
            if cifra.upper() not in ["A", "B", "C", "D", "E", "F"]:
                raise ValueError("\n          Cifra trebuie sa se afle in aceeasi baza ca numarul.\n".upper())
            if  baza<=10 and cifra.isalpha() :
                raise ValueError("\n          Cifra trebuie sa se afle in aceeasi baza ca numarul.\n".upper())



    @staticmethod
    def compare(nr1, nr2):
        """
            Face compararea intre doua numere.
            Pentru ca la anumite functii scadem din primul numar, acesta trebuie sa fie mai mare egal ca al doilea.
            Numerele sunt pastrate in menorie sub lista cifrelor.
        :param nr1: primul numar
        :param nr2: al doilea numar
        :return: raise ValueError daca al doilea numar este mai mare.
        """
        if len(nr1)<len(nr2):
            raise ValueError("\n        Scazatorul trebuie sa fie mai mic decat descazutul. \n".upper())
        if len(nr1)==len(nr2):
            for digit1, digit2 in zip(nr1,nr2):
                if digit2>digit1:
                    raise ValueError("\n        Scazatorul trebuie sa fie mai mic decat descazutul. \n".upper())

    @staticmethod
    def eBazaValidaConversiiDirecte(baza):
        if not baza.isdigit() :
            raise ValueError("\n        Baza trebuie sa fie unul din numerele 2, 4, 8 sau 16: \n".upper())
        if int(baza)<2 or int(baza)>16:
            raise ValueError("\n        Baza trebuie sa fie unul din numerele 2, 4, 8 sau 16: \n".upper())
        if int(baza)!=2 and int(baza)%4!=0:
            raise ValueError("\n        Baza trebuie sa fie unul din numerele 2, 4, 8 sau 16: \n".upper())


def test_eCifraValida():
    try:
        Validator.eCifraValida("123",12)
    except ValueError as msg:
        assert True

test_eCifraValida()