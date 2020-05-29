from random import *

class letter():
    def __init__(self, lowerchar, upperchar, is_vowel, is_consonant):
        self.upperchar = upperchar
        self.lowerchar = lowerchar
        self.is_vowel = is_vowel
        self.is_consonant = is_consonant

global alphabet
alphabet = [
    letter('a','A',True,False),
    letter('b','B',False,True),
    letter('c','C',False,True),
    letter('d','D',False,True),
    letter('e','E',True,False),
    letter('f','F',False,True),
    letter('g','G',False,True),
    letter('h','H',False,True),
    letter('i','I',True,False),
    letter('j','J',False,True),
    letter('k','K',False,True),
    letter('l','L',False,True),
    letter('m','M',False,True),
    letter('n','N',False,True),
    letter('o','O',True,False),
    letter('p','P',False,True),
    letter('q','Q',False,True),
    letter('r','R',False,True),
    letter('s','S',False,True),
    letter('t','T',False,True),
    letter('u','U',True,False),
    letter('v','V',False,True),
    letter('w','W',False,True),
    letter('x','X',False,True),
    letter('y','Y',True,True),
    letter('z','Z',False,True),
]

def rand_int(x1, x2):
    return int( int(x1) + random()*(int(x2)-int(x1)))

def make_name():
    lmin = 3
    lmax = 10
    name_length = rand_int(lmin,lmax)

    my_name = ""

    prev_vowel = False
    prev_consonant = False
    prev2_vowel = False
    prev2_consonant = False

    for i in range(0, name_length):
        a = get_letter(prev2_vowel, prev2_consonant)
        if (i == 0):
            my_name = my_name + a.upperchar
        else:
            my_name = my_name + a.lowerchar
        
        prev2_vowel = (a.is_vowel and prev_vowel)
        prev2_consonant = (a.is_consonant and prev_consonant)
        prev_vowel = a.is_vowel
        prev_consonant = a.is_consonant
    
    return my_name

def get_letter(need_consonant, need_vowel):
    global alphabet
    done = False

    while (not done):
        a = alphabet[rand_int(0,25)]
        if ((need_consonant and a.is_vowel) or (need_vowel and a.is_consonant)):
            done = False
        else:
            done = True
    return a

name1 = make_name()
print(name1)