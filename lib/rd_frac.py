#!/usr/bin/env python
# encoding: utf-8

from random import randint, random
from random_expression import RdExpression
from arithmetic import gcd
from renders import tex_render



"""Classe which generate randomly fractions calculus

Types of sums

add1 -> b / a + c / a
add2 -> b / a + c / ka
add3 -> b / a + e / d
add4 -> f + b / a 
add5 -> b / a + f

where:
    a integer > 2
    b integer different from 0 (could be coprime with a)
    c integer different from 0 (could be coprime with a or ka)
    e integer different from 0 (could be coprime with d)
    d integer > 2 ( a not divisible by d and d not divisible by a)
    k integer > 2
    f integer different from 0


Types of multiplications

mult1 -> a x b / c
mult2 -> a x b / c + d / c
mult3 -> a x b / c + d / e 
mult4 -> e / f x g / h  >>> TODO
mult5 -> i / j x k / l 

where:
    a integer different from -1, 0, 1
    b integer different from 0 
    c integer different from 0 and 1 (could be coprime with b)
    d integer different from 0 
    e, g integer different from 0
    f, g integer different from 0 and 1 such that e*g is coprime with f*h
    i, k integer different from 0
    j, l integer different from 0 and 1 such that i*k and j*l have divisor in common


Types of divisions

div1 -> a / b : c / d

where:
    a integer different from 0
    b integer different from 0, 1 
    c integer different from 0 
    d integer different from 0 
    


#Signs can be mod 
    

"""

add1 = RdExpression("{b} / {a} + {c} / {a}", \
        conditions = ["{a} > 2", "{b} != 0","{c} != 0"])

add2 = RdExpression("{b} / {a} + {c} / {k*a}", \
        conditions = ["{a} > 2","{k} > 2", "{b} != 0","{c} != 0"])

add3 = RdExpression("{b} / {a} + {e} / {d}", \
        conditions = ["{a} not in [0,1]", "{e} not in [0,1]", "{b} != 0","{d} not in [0,1]"])

add4 = RdExpression("{b} / {a} + {f}", \
        conditions = ["{a} > 2", "{b} != 0", "{f} != 0"])

add5 = RdExpression("{f} + {b} / {a}", \
        conditions = ["{a} > 2", "{b} != 0", "{f} != 0"])


mult1 = RdExpression("{a} * {b} / {c}",\
        conditions = ["{a} not in [-1, 0, 1]", "{b} != 0", "{c} not in [0,1]"])

mult2 = RdExpression("{a} * {b} / {c} + {d} / {c}",\
        conditions = ["{a} not in [-1, 0, 1]", "{b} != 0", "{c} not in [0,1]", \
        "{d} != 0"])

mult3 = RdExpression("{a} * {b} / {c} + {d} / {e}",\
        conditions = ["{a} not in [-1, 0, 1]", "{b} != 0", "{c} not in [0,1]", \
        "{d} != 0", "{e} not in [0,1]", "{c} != {e}"])

#mult4 = RdExpression("{e} / {f} * {g} / {h}", \
#        conditions = ["{e} != 0", "{g} != 0", "{f} != 0", "{g} != 0", \
#        "gcd({e*g}, {f*h}) == 1"])

mult5 = RdExpression("{e} / {f} * {g} / {h}", \
        conditions = ["{e} != 0", "{g} != 0", "{f} not in [0, 1]", "{h} not in [0, 1]"])
        #"gcd({e*g}, {f*h}) != 1"])

div1 = RdExpression("{a} / {b} : {c} / {d}", \
        conditions = ["{a} not in [0]", "{b} not in [0,1]", "{c} != 0","{d} not in [0]"])

frac = {"add1": add1,\
        "add2": add2,\
        "add3": add3,\
        "add4": add4,\
        "add5": add5, \
        "mult1": mult1,\
        "mult2": mult2,\
        "mult3": mult2,\
        #"mult4": mult2,\
        "mult5": mult5, \
        "div1": div1 }

if __name__ == '__main__':
    print(add1())
    print(add2())
    print(add3())
    print(add4())
    print(add5())

    print(mult1())
    print(mult2())
    print(mult3())
    #print(mult4())
    print(mult5())

    print(div1())
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
