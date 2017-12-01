'''
Created on Nov 12, 2017

@author: Ancuta Hij
'''

from conversii_rapide.conv_rapide import Conversie
from numar.numar import Numar


def test_getNumar():

    assert Conversie.getNumar([0, 1], 2, 1) == '1'
    assert Conversie.getNumar([1, 1, 1], 3, 1) == '7'

    assert Conversie.getNumar('A', 4, -1) == [1, 0, 1, 0]
    assert Conversie.getNumar('A', 4, -1) == [1, 0, 1, 0]



def test_Base2to4():
    nr = Numar([1, 1, 1, 1], 2)
    assert Conversie.Base2to4(nr) == [3, 3]
    nr = Numar([1, 1, 1, 1, 1], 2)
    assert Conversie.Base2to4(nr) == [1,3,3]


def test_Base2to8():
    nr = Numar([1, 1, 1, 1], 2)
    assert Conversie.Base2to8(nr) == [1,7]
    nr = Numar([1, 1, 1, 1, 1], 2)
    assert Conversie.Base2to8(nr) == [3,7]


def test_Base2to16():
    nr = Numar([1, 1, 1, 1], 2)
    assert Conversie.Base2to16(nr) == [15]
    nr = Numar([1, 1, 1, 1, 1], 2)
    assert Conversie.Base2to16(nr) == [1,15]


def test_Base4to2():
    nr = Numar([3,2,1], 4)
    assert Conversie.Base4to2(nr) == [1, 1, 1, 0, 0, 1]


def test_Base8to2():
    nr = Numar([3,2,7], 8)
    assert Conversie.Base8to2(nr) == [0, 1, 1, 0, 1, 0, 1, 1, 1]


def test_Base16to2():
    nr = Numar([3,15,10], 16)
    assert Conversie.Base16to2(nr) == [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]


test_getNumar()
test_Base2to4()
test_Base2to8()
test_Base2to16()
test_Base4to2()
test_Base8to2()
test_Base16to2()
