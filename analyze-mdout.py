import os
import glob
import numpy
import argparse
    
parser = argparse.ArgumentParser(description=" This script parses an Amber mdout file to extract the total energy.")
parser.add_argument("mdout_file", help="The filepath for the mdout file to analyze")
args = parser.parse_args()

file_location = args.mdout_file
etot_file = os.path.join('data','03_Prod.mdout')

basefile_location = file_location.split(".")[0]
output_file_location = F'{basefile_location}_Etot.txt'
filehandle = open(output_file_location,'w+')
outfile = open(output_file_location, 'r')
data = outfile.readlines()
outfile.close()

for line in data:
    if "NSTEP" in line:
        nstep_line = line
        cat = nstep_line.split()
        nstep = float(cat[2])
    if "Etot" in line:
        energy_line = line
        words = energy_line.split()
        energy = float(words[2])
        filehandle.write(F'{nstep} \t {energy: .4f} \n')
filehandle.close()
