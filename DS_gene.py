#!/usr/bin/env python
# encoding: utf-8

import jinja2, random, os
import sys
import optparse
from path import path
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

    # Saving place
    cwd = path("./").abspath()

    template_file =  path(options.template)

    if options.output:
        output = path(options.output)
    else:
        # Template should be named tpl_... tpl will replace by the number/name of the version
        output =  path(template_file.dirname()) / path(template_file.name[3:])

    if output.dirname != "":
        output.dirname().cd()

    output = output.name


    for subj in range(options.num_subj):
        subj = subj+1
        dest = path(str(subj) + output)
        with open( dest, 'w') as f:
            f.write(template.render( RdExpression = RdExpression , infos = {"subj" : subj}))
        #os.system("pdflatex " + dest)

        #if not options.dirty:
        #    os.system("rm *.aux *.log")

    cwd.cd()

if __name__ == '__main__':


    parser = optparse.OptionParser()
    parser.add_option("-t","--tempalte",action="store",type="string",dest="template", help="File with template")
    parser.add_option("-o","--output",action="store",type="string",dest="output",help="Base name for output )")
    parser.add_option("-n","--number_subjects", action="store",type="int", dest="num_subj", default = 1, help="The number of subjects to make")
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
