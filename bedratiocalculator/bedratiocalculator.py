
#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Create a BED file with the alele specific copy number ratios between two input BED files.")
parser.add_argument('bed1', help='BED file for the numerator.')
parser.add_argument('bed2', help='BED file for the denominator.')
parser.add_argument('output', help='Output BED file.')

args = parser.parse_args()

regions={}
with open(args.bed2,'r') as file: 
    heading=file.readline()
    for line in file:
        l=line.strip().split('\t')
        if l[0] not in regions: regions[l[0]]=[]
        regions[l[0]].append(l[0:])

   
with open(args.output,'w+') as file2: 
    with open(args.bed1,'r') as file:
        heading=file.readline()
        file2.write(heading)
        for line in file:
            l=line.strip().split('\t')
            #find the corresponding information from bed2
            info=[]
            for reg in regions[l[0]]:
                if int(l[1])>=int(reg[1]):
                    if int(l[1])<=int(reg[2]):
                        info=reg
                        continue
                    else:
                        next
            a_allele=''
            b_allele=''
            total=''
            if float(info[4])==0:
                a_allele=1
            else:
                a_allele=round(float(l[4])/float(info[4]),5)
            if float(info[5])==0:
                b_allele=1
            else:
                b_allele=round(float(l[5])/float(info[5]),5)
            total=a_allele+b_allele     
            file2.write(l[0]+'\t'+l[1]+'\t'+l[2]+'\t'+str(total)+'\t'+str(a_allele)+'\t'+str(b_allele)+'\n')
            