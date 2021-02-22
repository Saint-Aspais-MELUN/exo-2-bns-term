from exercices.exercice1 import *

def test_moyenne(lst,n):
    ## Ici le code d'initialisation si nécessaire
    lst=[2,3,5,9,4]
    assert moyenne([5,3,8])>5,33 and moyenne([5,3,8])<5,34
    assert moyenne([1,2,3,4,5,6,7,8,9,10])==5.5
        assert moyenne([])=='erreur'
    
