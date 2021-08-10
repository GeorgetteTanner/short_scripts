#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:43:03 2021
@author: medgnt
"""

import argparse

parser = argparse.ArgumentParser(description='Rename reads in fastq file by adding a prefix and ending to the first section of read names. Eg. "@123 additional info" > "@{prefix}123{end} additional info"')
parser.add_argument('-i', '--input', dest='input', help='Input fastq file')
parser.add_argument('-o', '--output', dest='output', help='Output fastq file')
parser.add_argument('-p', '--prefix', dest='prefix', help='String to prefix read names')
parser.add_argument('-e', '--end', dest='end', help='String to end read names')
args = parser.parse_args()



with open(args.input,'r') as ifile:
    with open(args.output,'w+') as ofile:
        line=1
        i=1
        line=ifile.readline()
        while line:

            l=line.split()
            ofile.write('@'+args.prefix+':'+l[0][1:]+args.end+' '+' '.join(l[1:])+'\n')

            line=ifile.readline()
            ofile.write(line)
            line=ifile.readline()
            ofile.write(line)
            line=ifile.readline()
            ofile.write(line)
            line=ifile.readline()

            i+=1
