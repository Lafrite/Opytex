#!/usr/bin/env python
# encoding: utf-8

from random import randint

def pythagore_triplet(v_min = 1, v_max = 10):
    """Random pythagore triplet generator

    :param v_min: minimum in randint
    :param v_max: max in randint
    :returns: (a,b,c) such that a^2 + b^2 = c^2

    """
    u = randint(v_min,v_max)
    v = randint(v_min,v_max)
    while v == u:
        v = randint(v_min,v_max)

    u, v = max(u,v), min(u,v)

    return (u**2-v**2 , 2*u*v, u**2 + v**2)

if __name__ == '__main__':
    print(pythagore_triplet())

    for j in range(1,10):
        for i in range(j,10):
            print((i**2-j**2 , 2*i*j, i**2 + j**2))






# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
