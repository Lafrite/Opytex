#!/usr/bin/env python
# encoding: utf-8

import jinja2, random, os
import sys
import optparse
from rd_frac import frac

def randfloat(approx = 1, low = 0, up = 10):
		""" return a random number between low and up with approx floating points """
		ans = random.random()
		ans = ans*(up - low) + low
		ans = round(ans, approx)
		return ans 

random.randfloat = randfloat

def gaussRandomlist(mu = 0, sigma = 1, size = 10, manip = lambda x:x):
    """ return a list of a gaussian sample """
    ans = []
    for i in range(size):
        ans += [manip(random.gauss(mu,sigma))]
    return ans

random.gaussRandomlist = gaussRandomlist

def gaussRandomlist_strInt(mu = 0, sigma = 1, size = 10):
    return gaussRandomlist(mu, sigma, size, manip = lambda x: str(int(x)))

random.gaussRandomlist_strInt = gaussRandomlist_strInt

random.frac = frac


report_renderer = jinja2.Environment(
block_start_string = '%{',
block_end_string = '%}',
variable_start_string = '%{{',
variable_end_string = '%}}',
loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

def main(options):
    template = report_renderer.get_template(options.template)

    cwd = os.getcwd()

    if options.output:
        output_name = options.output
    else:
        tpl_base = os.path.splitext(options.template)[0]
        output_name = tpl_base + "_"
    
    output_dir = os.path.dirname(output_name)
    output_basename = os.path.basename(output_name)
    output_tplname = output_basename.split("/")[-1]

    os.chdir(output_dir)

    for subj in range(options.num_subj):
        subj = subj+1
        dest = output_tplname + str(subj) + '.tex'
        with open( dest, 'w') as f:
                f.write(template.render(random = random, infos = {"subj" : subj}))
        os.system("pdflatex " + dest)

        if not options.dirty:
            os.system("rm *.aux *.log")

    os.chdir(cwd)

if __name__ == '__main__':


    parser = optparse.OptionParser()
    parser.add_option("-t","--tempalte",action="store",type="string",dest="template", help="File with template")
    parser.add_option("-o","--output",action="store",type="string",dest="output",help="Base name for output (without .tex or any extension))")
    parser.add_option("-n","--number_subjects", action="store",type="int", dest="num_subj", default = 2, help="The number of subjects to make")
    parser.add_option("-d","--dirty", action="store_true", dest="dirty", help="Do not clean after compilation")

    (options, args) = parser.parse_args()

    if not options.template:
        print("I need a template!")
        sys.exit(0)

    main(options)

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
