#!/usr/bin/env python
# encoding: utf-8

import jinja2, random, os
import sys
import optparse
from pymath.random_expression import RdExpression

texenv = jinja2.Environment(
    block_start_string = '\Block{',
    # Gros WTF!! Si on le met en maj ça ne marche pas alors que c'est en maj dans le template...
    block_end_string = '}',
    variable_start_string = '\Var{',
    variable_end_string = '}',
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

def main(options):
    #template = report_renderer.get_template(options.template)
    template = texenv.get_template(options.template)

    cwd = os.getcwd()

    if options.output:
        output_name = options.output
    else:
        tpl_base = os.path.splitext(options.template)[0]
        output_name = tpl_base + "_"
    
    output_dir = os.path.dirname(output_name)
    if output_dir != "":
        os.chdir(output_dir)
    output_basename = os.path.basename(output_name)
    output_tplname = output_basename.split("/")[-1]


    for subj in range(options.num_subj):
        subj = subj+1
        dest = output_tplname + str(subj) + '.tex'
        with open( dest, 'w') as f:
            f.write(template.render(plop = str(1), RdExpression = RdExpression , infos = {"subj" : subj}))
        #os.system("pdflatex " + dest)

        #if not options.dirty:
        #    os.system("rm *.aux *.log")

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
