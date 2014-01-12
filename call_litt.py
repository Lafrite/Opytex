#!/usr/bin/env python
# encoding: utf-8

from random import randint, uniform
from math import sqrt
from jinja2 import Template

"""
Generate expression for litteral calculous

3 types of expression (a, b, c != 0, 1)
    1 -> ax + b  and eval for x != -b / a
    2 -> ax(bx + c) and eval for x != 0 and x != -c / b
    3 -> ax^2 + b and eval for x != +-sqrt(b/a) (if a and b have same sign)
"""

def gene_type1(min_ = -10, max_ = 10):
    """@todo: Docstring for gene_type1

    :param min_: @todo
    :param max_: @todo
    :returns: @todo

    """
    a, b = 0, 0
    while (b in [0]) or (a in [0, 1]):
        a = randint(min_, max_)
        b = randint(min_, max_)

    return "{}x + {}".format(a,b), [-b/a]

def gene_type2(min_, max_):
    """@todo: Docstring for gene_type2

    :param min_: @todo
    :param max_: @todo
    :returns: @todo

    """
    a, b, c = 0, 0, 0
    while (a in [0, 1]) or (b in [0, 1]) or c in [0]:
        a = randint(min_, max_)
        b = randint(min_, max_)
        c = randint(min_, max_)

    return "{}x({}x + {})".format(a,b,c), [0, -c/b]

def gene_type3(min_ = -10, max_ = 10):
    """@todo: Docstring for gene_type3

    :param min_: @todo
    :param max_: @todo
    :returns: @todo

    """
    a, b = 0, 0
    while (b in [0]) or (a in [0, 1]):
        a = randint(min_, max_)
        b = randint(min_, max_)

    if a*(-b) > 0:
        VI = [-sqrt(-b/a), sqrt(-b/a)]
    else:
        VI = []

    return "{}x^2 + {}".format(a,b), VI

def get_goodX(VI, approx = 0, min_ = -10, max_ = 10):
    """@todo: Docstring for get_goodX

    :param VI: @todo
    :returns: @todo

    """
    x = uniform(min_, max_)
    if approx == 0:
        x = int(x)
    else:
        x = round(x,approx)
    while x in VI:
        x = uniform(min_, max_)
        if approx == 0:
            x = int(x)
        else:
            x = round(x,approx)

    return x



def fullExo(min_ = -10 , max_ = 10):
    """Generate the whole exo

    :param min_: @todo
    :param max_: @todo
    :returns: @todo

    """
    template = Template("""
\\begin{equation*}
$A = {{type1}}$ \\qquad $B = {{type2}}$ \\qquad $C = {{type3}}
\\end{equation*}

Évaluer $A$, $B$ et $C$ pour $x = {{x1}}$ puis $x = {{x2}}$""")

    type1, VI1 = gene_type1(min_, max_)
    type2, VI2 = gene_type2(min_, max_)
    type3, VI3 = gene_type3(min_, max_)

    VI = VI1 + VI2 + VI3

    x1, x2 = get_goodX(VI), get_goodX(VI, approx = 1)

    info = {"type1": type1, "type2": type2, "type3": type3, "x1":x1, "x2":x2}

    exo = template.render(**info)

    return exo

if __name__ == '__main__':
    print(fullExo())

    




# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
