#!/usr/bin/env python
# encoding: utf-8

from random import randint, random



"""Classe which generate randomly fractions sums

Types of sums

1 -> b / a + c / a
2 -> b / a + c / ka
3 -> b / a + e / d
4 -> f + b / a or b / a + f

where:
    a integer > 2
    b integer different from 0 (could be coprime with a)
    c integer different from 0 (could be coprime with a or ka)
    e integer different from 0 (could be coprime with d)
    d integer > 2 ( a not divisible by d and d not divisible by a)
    k integer > 2
    f integer different from 0

Signs can be mod 
    

"""

def a(min_ = 2, max_ = 10):
    """Generate randomly a

    :param min_: minimum value for a
    :param max_: maximum value for a
    :returns: a value

    """
    return randint(min_, max_)

def k(min_ = 2, max_ = 5):
    """Generate randomly k

    :param min_: minimum value for k
    :param max_: maximum value for k
    :returns: k value

    """
    return randint(min_, max_)

def b(a_ = 0, min_ = -20, max_ = 20):
    """Generate randomly b

    :param a: the value of a if b has to be coprime with a (default 0 which means not necessarily coprime)
    :param min_: minimum value for b (default -20)
    :param max_: maximum value for b (default 20)
    :returns: b value

    """
    b_ = 0
    while b_ == 0 or not coprime:
        b_ = randint(min_, max_)
        if a_ == 0:
            coprime = 1
        elif b_ != 0:
            gcd_ = gcd(abs(a_),abs(b_))
            coprime = (gcd_ == 1)

    return b_

def c(a_ = 0, k_ = 1, min_ = -20, max_ = 20):
    """Generate randomly c

    :param a: the value of a if c has to be coprime with a (default 0 which means not necessarily coprime)
    :param k: the value of a if c has to be coprime with ak (default 0 which means not necessarily coprime)
    :param min_: minimum value for c (default -20)
    :param max_: maximum value for c (default 20)
    :returns: c value

    """
    return b(a_ = a_*k_, min_ = min_, max_ = max_)

def e(d_ = 0, min_ = -20, max_ = 20):
    """Generate randomly e

    :param d: the value of a if e has to be coprime with a (default 0 which means not necessarily coprime)
    :param min_: minimum value for e (default -20)
    :param max_: maximum value for e (default 20)
    :returns: e value

    """
    return b(a_ = d_, min_ = min_, max_ = max_)

def d(a_, min_ = 2, max_ = 10):
    """Generate randomly d

    :param a: the value of a
    :param min_: minimum value for d
    :param max_: maximum value for d
    :returns: d value

    """
    d_ = randint(min_, max_)
    div = (not a_ % d_) or (not d_ % a_)
    while div:
        d_ = randint(min_, max_)
        div = (not a_ % d_) or (not d_ % a_)

    return d_

def f(min_ = -10, max_ = 10):
    """Generate randomly f

    :param min_: minimum value for f
    :param max_: maximum value for f
    :returns: f value

    """
    f_ = randint(min_, max_)
    while f_ == 0:
        f_ = randint(min_, max_)

    return f_

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
    b_ = b(a_=a_)
    c_ = c(a_=a_)
    
    return nothingOrMinus() + "\\frac{" + str(b_) + "}{" + str(a_) + "}" + plusOrMinus() + "\\frac{" + str(c_) + "}{" + str(a_) + "}"

def type2():
    """@todo: Docstring for type2
    :returns: @todo

    """
    a_ = a()
    b_ = b(a_=a_)
    k_ = k()
    c_ = c(a_=a_, k_ = k_)
    
    return nothingOrMinus() + "\\frac{" + str(b_) + "}{" + str(a_) + "}" + plusOrMinus() + "\\frac{" + str(c_) + "}{" + str(k_*a_) + "}"

def type3():
    """@todo: Docstring for type3
    :returns: @todo

    """
    a_ = a()
    b_ = b(a_=a_)
    c_ = c(a_=a_)
    d_ = d(a_)
    
    return nothingOrMinus() + "\\frac{" + str(b_) + "}{" + str(a_) + "}" + plusOrMinus() + "\\frac{" + str(c_) + "}{" + str(d_) + "}"

def type4():
    """@todo: Docstring for type4
    :returns: @todo

    """
    a_ = a()
    b_ = b(a_=a_)
    f_ = f()
    
    return str(f_) +  plusOrMinus() +  "\\frac{" + str(b_) + "}{" + str(a_) + "}"

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
    print(type3())
    print(type4())

# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
