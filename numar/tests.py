'''
Created on Nov 12, 2017

@author: Ancuta Hij
'''



from numar.numar import Numar


def test_getNumar():

    x=Numar()
    assert x.getNumar()==[]

    x=Numar([1,2,3], 4)
    assert x.getNumar()==[1,2,3]

def test_getBaza():
    x = Numar()
    assert x.getBaza()==10

    x=Numar([1,2,3], 4)
    assert x.getBaza()==4

test_getNumar()