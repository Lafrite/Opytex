#!/usr/bin/env python
# encoding: utf-8

import jinja2, random, os

report_renderer = jinja2.Environment(
  block_start_string = '%{',
  block_end_string = '%}',
  variable_start_string = '%{{',
  variable_end_string = '%}}',
  loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

template = report_renderer.get_template('./DS_09_litt_mediane.tpl.tex')

def randfloat(approx = 1, low = 0, up = 10):
		""" return a random number between low and up with approx floating points """
		ans = random.random()
		ans = ans*(up - low) + low
		ans = round(ans, approx)
		return ans 

def gaussRandomlist(mu = 0, sigma = 1, size = 10, manip = lambda x:x):
    """ return a list of a gaussian sample """
    ans = []
    for i in range(size):
        ans += [manip(random.gauss(mu,sigma))]
    return ans

def hauteurs(num = 15):
    return " ;\\quad ".join(gaussRandomlist(mu = 120, sigma = 10, size = 15, manip = lambda x: str(int(x))))

random.randfloat = randfloat
random.gaussRandomlist = gaussRandomlist
random.hauteurs = hauteurs

for subj in ["A"]:
    dest = 'DS_09_litt_mediane_{subj}.tex'.format(subj = subj)
    with open( dest, 'w') as f:
            f.write(template.render(random = random, infos = {"subj" : subj}))
    os.system("pdflatex " + dest)
    os.system("rm *.aux *.log")

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
