#!/usr/bin/env python
# encoding: utf-8

import jinja2, os

# Definition of jinja syntax for latex
texenv = jinja2.Environment(
    block_start_string = '\Block{',
    # Gros WTF!! Si on le met en maj ça ne marche pas alors que c'est en maj dans le template...
    block_end_string = '}',
    variable_start_string = '\Var{',
    variable_end_string = '}',
    loader = jinja2.FileSystemLoader(os.path.abspath('.')),
    extensions = ['jinja2.ext.do']
)

# Filters

def do_calculus(steps, name = "A", sep = "=", end = "", joining = " \\\\ \n"):
    """Display properly the calculus

    Generate this form string:
    "name & sep & a_step end joining"

    :param steps: list of steps
    :returns: latex string ready to be endbeded


    """

    ans = joining.join([name + " & " + sep + " & " + str(s) + end for s in steps])
    return ans

texenv.filters['calculus'] = do_calculus

from random import shuffle
texenv.filters['shuffle'] = shuffle



if __name__ == '__main__':
    from pymath.expression import Expression
    exp = Expression("2/4 + 18")
    print(do_calculus(exp.simplify()))



# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
