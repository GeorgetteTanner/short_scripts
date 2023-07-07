# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:37:08 2020

@author: medgnt
"""

import argparse

parser = argparse.ArgumentParser(description="Extract log2 values for a list of genes from a bed segmentation file.")
parser.add_argument('-l', '--list', required=True, dest='list', help='Comma separated list of gene names.')
parser.add_argument('-g', '--gencode', required=True, dest='gencode', help='Gencode file.')
parser.add_argument('-b', '--bed', required=True, dest='bed', help='BED file.')

args = parser.parse_args()

genes={}
with open(args.gencode,'r') as file:
    for line in file:
        if not line.startswith("#"):
            l=line.split("\t")
            if l[2]=='transcript':
                gene=line[line.index("gene_name ")+11:]
                gene=gene[:gene.index('"')]
                genes[gene]=[l[0],l[3]]

segs={}
with open(args.bed,'r') as file:
    file.readline()
    for line in file:
        l=line.strip().split('\t')
        if l[1] not in segs:
            segs[l[1]]=[]
        segs[l[1]].append([l[2],l[3],l[8]])
            
            
log2s=[]                
for g in args.list.split(','):
    chro,pos=genes[g]
    for seg in segs[chro]:
        if int(pos)>int(seg[0]):
            log2=seg[2]
    log2s.append(log2)
    #print(g+'\t'+chro+'\t'+pos)

print(args.bed+'\t'+'\t'.join(log2s))
          