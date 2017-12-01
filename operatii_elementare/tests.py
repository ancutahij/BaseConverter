'''
Created on Nov 12, 2017

@author: Ancuta Hij
'''


from operatii_elementare.operatii import Operatii


def test_adunare():
    numar1 = Operatii([3, 1, 4, 7], 8)
    numar2 = Operatii([2, 0, 2], 8)
    assert numar1.adunare(numar2) == [3, 3, 5, 1]


def test_scadere():
    numar1 = Operatii([3, 1, 4, 7], 8)
    numar2 = Operatii([2, 0, 2], 8)
    assert numar2.scadere(numar1) == [2, 7, 4, 5]

    numar1=Operatii([1,0,2],8)
    assert (numar1.scadere(numar2))==[1,0,0]

    numar1=Operatii([1,0,0,1,1,0],2)
    numar2=Operatii([1,0,0,1],2)


    assert Operatii.scadere(numar2,numar1)==[1,1,1,0,1]

def test_inmultire():
    numar = Operatii([4, 12, 3, 2, 10], 16)

    cifra = 11
    assert numar.inmultire(cifra) == [3, 4, 6, 2, 12, 14]




def test_impartire():
    numar = Operatii([2, 9, 11, 4, 13], 16)
    cifra = 8

    assert numar.impartire(cifra) == [[5, 3, 6, 9], 5]

    numar=Operatii([5],10)
    cifra=9
    assert (numar.impartire(cifra))==[[0], 5]


test_adunare()
test_scadere()
test_inmultire()
test_impartire()