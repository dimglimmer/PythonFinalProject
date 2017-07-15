"""
Calculating nucleotide frequencies from HIV 5'UTR of patients
"""


""" 
Determining if the input is a FASTA file 
"""

import re

def fasta(filename, maxline = 100): # iterates over the first 100 characters of the file
    pat = re.compile('^[ACGTN-]+$')  # nucleotides are represented by these letters
    nrecords = 0
    handle = open('uc_hivdata.fasta', 'rU')
    for ln, line in enumerate(handle):
            if line.startswith('>'): # in FASTA files, records start with '>'
                nrecords += 1
                continue # goes into FASTA file
            if not pat.findall(line.upper()) and len(line.strip()) > 0:
                print(line)
                return False
            if ln > maxline: # stops iterating after first 100 characters as after a 100, it probably know if it's a FASTA file
                break
    if nrecords == 0:
        print ('no records')
        return False
"""
Note: I "borrowed" this from your goodcode.py file.
"""

"""
Using Bowtie package to align the sequences together


# Build index from reference
bowtie2-build nl43.fasta refer

# Align the sequences and output as sam file
bowtie2 -x refer -f uc_hivdata.fasta -S newcut --very-sensitive-local -p2


newcut = the name of the output file
refer = name of file generated form index
p2 = using 2 processorts
type of alignment = very-sensitive local (takes longer but is more precise)
-x = specifying index to use
-S = output as sam file
-f = file to align is a FASTA file
"""
# The aligning of these files allows us to visualize and cut the region in the HIV genome we are interested in.
# This can be done using samtools or bowtie but since we are using python, let's do it using that! :)

"""
#Isolating region of interest from series of HIV genomes
"""

handle = open('uc_hivdata.fasta', 'rU') # open file as read only
outfile = open('hivda.fasta', 'w') # make new output file with results
for line in handle:
    if line.startswith('>'): # find FASTA seq
        continue
    else:
        area = line[695:790] # region encompassing of (5'UTR)
        print area
        outfile.write(area+'\n')

"""
Calculating nucleotide frequencies per site
"""
handle = open('hivda.fasta')
nucMatrix = [] # establish a matrix of our sequence

for i in range (0,100): # 100 different sequences
    nucMatrix.append(list(handle.readline().strip("\n"))) #taking out all the spaces allows to only work with strings of interest
#print (nucMatrix)
flipnucMatrix = [] # flipping the matrix allows us to calculate nuc frequencies per nuc site (i.e. freq at position 695, 696, etc.)
for i in range(0,95): # length of UTR is 95 nuc
    columntorow = []
    for j in range (0,85):
        print nucMatrix[j][i]
        columntorow.append(nucMatrix[j][i])
    flipnucMatrix.append(columntorow)
print flipnucMatrix


counts = [] # use counter function to calculate total number of nucleotides
from collections import Counter
for row in flipnucMatrix:
    counts.append(Counter(row)) # after counting the total number of nucleotides, divide by 85 and multiply by 100 to get frequency
for j in counts:
    for i in j:
        j[i] = float(j[i] * 100 / 85)
print(counts)
print('Done!')

outfile.close()
handle.close() # close for good etiqutte
