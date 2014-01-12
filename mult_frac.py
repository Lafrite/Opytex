#!/usr/bin/env python
# encoding: utf-8

from random import randint, random



"""Classe which generate randomly fractions multiplications

Types of multiplications

1 -> a x b / c
2 -> a x b / c + d / c
3 -> a x b / c + d / e >>> TODO
4 -> e / f x g / h >>> TODO
5 -> i / j x k / l >>> TODO

where:
    a integer differente from -1, 0, 1
    b integer different from 0 
    c integer different from 0 and 1 (could be coprime with b)
    d integer different from 0 
    e, g integer different from 0
    f, g integer different from 0 and 1 such that e*g is coprime with f*h
    i, k integer different from 0
    j, l integer different from 0 and 1 such that i*k and j*l have divisor in common

Signs can be mod 
    

"""

def a(min_ = -10, max_ = 10, notIn = [-1,0,1]):
    """Generate randomly a

    :param min_: minimum value for a
    :param max_: maximum value for a
    :param notIn: value that can't take a
    :returns: a value

    """
    a_ = randint(min_, max_)
    while a_ in notIn:
        a_ = randint(min_, max_)

    return a_

def b(min_ = -10, max_ = 10, notIn = [0]):
    """Generate randomly b

    :param min_: minimum value for b
    :param max_: maximum value for b
    :param notIn: value that can't take b
    :returns: a value

    """
    return a(min_, max_, notIn)

def c(b_ = 0, min_ = 2, max_ = 20):
    """Generate randomly c

    :param a_: the value of b if c has to be coprime with b (default 0 which means not necessarily coprime)
    :param min_: minimum value for b (default -20)
    :param max_: maximum value for b (default 20)
    :returns: c value

    """
    c_ = 0
    while c_ == 0 or not coprime:
        c_ = randint(min_, max_)
        if b_ == 0:
            coprime = 1
        elif c_ not in [-1,0,1]:
            gcd_ = gcd(abs(c_),abs(b_))
            coprime = (gcd_ == 1)

    return c_

def d(min_ = -10, max_ = 10, notIn = [0]):
    """Generate randomly d

    :param min_: minimum value for d
    :param max_: maximum value for d
    :param notIn: value that can't take d
    :returns: a value

    """
    return a(min_, max_, notIn)

def plusOrMinus(p = 0.5):
    """Return plus with prob p and minus otherwise
    """
    pm = random()
    return "+"*(pm >= p) + "-"*(pm < p)

def nothingOrMinus(p = 0.5):
    """Return nothing with prob p and minus otherwise
    """
    pm = random()
    return ""*(pm >= p) + "-"*(pm < p)

def type1():
    """@todo: Docstring for type1
    :returns: @todo

    """
    a_ = a()
    b_ = b()
    c_ = c(b_=b_)

    return str(a_) + " \\times \\frac{" + str(b_) + "}{" + str(c_) + "}"
    
def type2():
    """@todo: Docstring for type2
    :returns: @todo

    """
    a_ = a()
    b_ = b()
    c_ = c(b_=b_)
    d_ = d()

    return str(a_) + " \\times \\frac{" + str(b_) + "}{" + str(c_) + "} + \\frac{" + str(d_) + "}{" + str(c_) + "}"


def gcd(a_, b_):
        """Compute gcd(a,b)

        :param a: first number
        :param b: second number
        :returns: the gcd

        """
        if a_ > b_:
            c_ = a_ % b_
        else:
            c_ = b_ % a_

        if c_ == 0:
            return min(a_,b_)
        elif a_ == 1:
            return b_
        elif b_ == 1:
            return a_
        else:
            return gcd(min(a_,b_), c_)

if __name__ == '__main__':
    # print(a())
    # print(b())
    # print(c())
    # print(d(3))
    # print(e())
    # print(f())
    print(type1())
    print(type2())

# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
