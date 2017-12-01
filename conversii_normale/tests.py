'''
Created on Nov 12, 2017

@author: Ancuta Hij
'''

from conversii_normale.impartiri_substitutie import Conversii
from operatii_elementare.operatii import Operatii


def test_impartiriSuccesive():

    nr = Operatii([1, 7, 3], 8)
    baza = 7

    assert Conversii.impartiriSuccesive(nr, baza) == [2, 3, 4]

    nr = Operatii([2, 4, 2], 7)
    baza = 6
    assert Conversii.impartiriSuccesive(nr, baza) == [3, 3, 2]

    x = Operatii([11, 0, 1], 12)
    baza = 6
    assert  Conversii.impartiriSuccesive(x, baza)==[1,1,2,0,1]



def test_substitutie():
    x = Operatii([1,1,2, 0, 1], 6)
    baza = 12
    assert Conversii.substitutie(x,baza)==[11,0,1]



    x=Operatii([6,7,3,4], 8)
    baza=6
    assert Conversii.substitutie(x, baza) == [2,4,2,3, 2]


def test_conversieBazaIntermediara():
    x=Operatii([1,1,2, 0, 1], 6)
    baza=12
    assert (Conversii.conversieBazaIntermediara(x,baza))==[11,0,1]

    x=Operatii([1,7,3],8)
    baza=7
    assert Conversii.conversieBazaIntermediara(x,baza)==[2,3,4]

test_impartiriSuccesive()
test_substitutie()
test_conversieBazaIntermediara()
