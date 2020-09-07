# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 02:07:45 2020

@author: medgnt
"""

import argparse

parser = argparse.ArgumentParser(description="Filter out variants in dbSNP from vcf file.")
parser.add_argument('-i', '--input', required=True, dest='input', help='Input vcf file.')
parser.add_argument('-d', '--dbsnp', required=True, dest='dbsnp', help='dbSNP vcf file.')
parser.add_argument('-g', '--germline', required=True, dest='germline', help='Output germline file.')
parser.add_argument('-s', '--somatic', required=True, dest='somatic', help='Output somatic file.')
args = parser.parse_args()


dbsnp={}
with open(args.dbsnp,'r') as file:
    for line in file:
        if line.startswith('#'):
            pass
        else:
            l=line.split('\t')
            dbsnp[l[0]+'_'+l[1]]=''

out=[]
with open(args.input,'r') as file:
    with open(args.germline,'w+') as file2:
        with open(args.somatic,'w+') as file3:
            for line in file:
                if line.startswith('#'):
                    file2.write(line)
                    file3.write(line)
                else:
                    l=line.split('\t')
                    if l[0]+'_'+l[1] in dbsnp:
                        file2.write(line)
                    else:
                        file3.write(line)

            