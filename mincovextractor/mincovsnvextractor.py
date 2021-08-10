
#! /usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
from subprocess import check_output

parser = argparse.ArgumentParser(description="Get a list of variants from a vcf file that have a minimum coverage and frequency in a given BAM file.")
parser.add_argument('-v', '--vcf', dest='vcf', help='Input vcf file')
parser.add_argument('-n', '--normal', dest='normal', help='Input normal BAM file')
parser.add_argument('-t', '--tumour', dest='tumour', help='Input tumour BAM file')
parser.add_argument('-o', '--output', dest='output', help='Output file')
parser.add_argument('-m', '--mincov', dest='mincov', type=int, help='Minimum coverage for varaints to be included')
parser.add_argument('-f', '--minfreq', dest='minfreq', type=float, help='Minimum variant allele frequency for variants to be included')

args = parser.parse_args()

with open(args.output,'w+') as outfile:
    with open(args.vcf,'r') as infile:
        for line in infile:
            if line.startswith("#"):
                pass
            else:
                l=line.split('\t')
                region=l[0]+":"+str(l[1])+"-"+str(l[1])
                tdepth=check_output(["samtools", "depth", "-r"+ region, args.tumour]).decode('ascii')
                ndepth=check_output(["samtools", "depth", "-r"+ region, args.normal]).decode('ascii')
                if tdepth!='' and ndepth!='':
                    if int(tdepth.split('\t')[2].strip()) >= args.mincov and int(ndepth.split('\t')[2].strip()) >= args.mincov:
                        if float(l[9].split(":")[0])>=args.minfreq:
                            outfile.write(line)