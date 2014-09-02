#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import optparse
from path import path

from texenv import texenv
from pymath.random_expression import RdExpression

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

    if output.dirname() != "":
        output.dirname().cd()

    output = output.name


    for subj in range(options.num_subj):
        subj = subj+1
        dest = path(str(subj) + output)
        with open( dest, 'w') as f:
            f.write(template.render( RdExpression = RdExpression , infos = {"subj" : subj}))

        if not options.no_compil:
            os.system("pdflatex " + dest)

            if not options.dirty:
                os.system("rm *.aux *.log")

    cwd.cd()

if __name__ == '__main__':


    parser = optparse.OptionParser()
    parser.add_option("-t","--template",action="store",type="string",dest="template", help="File with the template. The name should have the following form tpl_... .")
    parser.add_option("-o","--output",action="store",type="string",dest="output",help="Base name for output )")
    parser.add_option("-N","--number_subjects", action="store",type="int", dest="num_subj", default = 1, help="The number of subjects to make")
    parser.add_option("-d","--dirty", action="store_true", dest="dirty", help="Do not clean after compilation")
    parser.add_option("-n","--no-compile", action="store_true", dest="no_compil", help="Do not compile source code")

    (options, args) = parser.parse_args()

    if not options.template:
        print("I need a template!")
        sys.exit(0)

    main(options)

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
