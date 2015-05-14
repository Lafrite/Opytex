#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import optparse
import csv
from path import path

from texenv import texenv

import math as m
import random as rd
from pymath.expression import Expression
from pymath.polynom import Polynom
from pymath.polynomDeg2 import Polynom_deg2
from pymath.fraction import Fraction 
from pymath.random_expression import random_str 


export_dict = {}
export_dict.update(m.__dict__)
export_dict.update(rd.__dict__)
export_dict.update(__builtins__.__dict__)
export_dict.update({"Expression":Expression,\
        "Polynom":Polynom,\
        "Polynom_deg2":Polynom_deg2,\
        "Fraction":Fraction,\
        "random_str": random_str,\
        })

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

    if not options.csv_file:
        list_infos = [{"num": i+1} for i in range(options.num_subj)]
    else:
        with open(options.csv_file, 'r', encoding = 'ISO-8859-1') as f:
            list_infos = list(csv.DictReader(f, delimiter=";"))
            for (i,a) in enumerate(list_infos):
                a['num'] = i+1

    if output.dirname() != "":
        output.dirname().cd()

    output = output.name

    tmp_pdf = []

    for infos in list_infos:
        #print("_______" + str(infos))
        dest = path(str(infos['num']) + output)
        tmp_pdf.append(dest.namebase + ".pdf")
        with open( dest, 'w') as f:
            f.write(template.render(  infos = infos, **export_dict ))

        if not options.no_compil:
            os.system("pdflatex " + dest)

    if not options.dirty:
        os.system("rm *.aux *.log")

    if not options.no_join:
        print(path("./").abspath())
        print("pdfjam "+ " ".join(tmp_pdf) + " -o all" + path(output).namebase + ".pdf")
        os.system("pdfjam "+ " ".join(tmp_pdf) + " -o all" + path(output).namebase + ".pdf")
        #os.system("pdfjam *.pdf -o all" + path(output).namebase + ".pdf")
        print("rm " + " ".join(tmp_pdf))
        os.system("rm " + " ".join(tmp_pdf))

    cwd.cd()

if __name__ == '__main__':


    parser = optparse.OptionParser()
    parser.add_option("-t","--template",action="store",type="string",dest="template", help="File with the template. The name should have the following form tpl_... .")
    parser.add_option("-o","--output",action="store",type="string",dest="output",help="Base name for output )")
    parser.add_option("-c","--csv", action="store", type="string", dest="csv_file", help="Filename of the csv file where informations are stored")
    parser.add_option("-N","--number_subjects", action="store",type="int", dest="num_subj", default = 1, help="The number of subjects to make")
    parser.add_option("-d","--dirty", action="store_true", dest="dirty", help="Do not clean after compilation")
    parser.add_option("-n","--no-compile", action="store_true", dest="no_compil", help="Do not compile source code")
    parser.add_option("-j","--no-join", action="store_true", dest="no_join", help="Do not join pdf and clean single pdf")


    (options, args) = parser.parse_args()

    if not options.template:
        print("I need a template!")
        sys.exit(0)

    main(options)

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
