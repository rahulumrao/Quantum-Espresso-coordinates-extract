#!/usr/bin/env python
#extract all coordinates from Quantum Espresso output file
# and write in a file as a catresian trajectory
#
# python QE-extract-xyz.py outfilename
# Written by Rahul Verma (vrahul@iitk.ac.in)
import sys,os

start = []
end = []

#Reading QE oufilename as an argument from the same line
file =  sys.argv[1]
# Open a file as outfile-traj.xyz to write xyz 
nwfile = os.path.splitext(file)[0] + "-traj.xyz"

oldfile = open(file,"r")
newfile = open(nwfile,"w")

#Read the complete outfile
rline = oldfile.readlines()

# Find the given arguments from the file, if finds :
# Stores that line number in i as start array
# Similar for the end string in m and append it to end array
for i in range (len(rline)):
    if "ATOMIC_POSITIONS (angstrom)" in rline[i]:
        start.append(i+1)
        for m in range (start[-1],len(rline)):
            if "Writing output" in rline[m]:
                end.append(m-3)
                break
#print(start)
#print(end)

# Writing the extracted coordinates in a formatted xyz format
for i,iStart in enumerate(start):
    nAtoms = end[i] - (start[i])
    newfile.write(str(nAtoms))
    newfile.write('\n\n')
    for line in rline[start[i] : end[i]]:
        words = line.split()
        newfile.write("{:10}  {:}\n".format(words[0],line[10:-1]))

oldfile.close()
newfile.close()
#end of the program
