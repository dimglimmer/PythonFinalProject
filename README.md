# HIV 5'UTR Aligner 
---
The use of this tool will allow us to compile, cut and align sequences of the HIV 5'UTR. Furthermore we can calcualte the frequency of nucleotides in the sequence.

## Input Data
The genomic sequnce data was obtained from the databanks at Los Alamos. The entire sequence was filtered down to the 5' UTR region using Python. For ease, the data was placed in FASTA format.

## Step 1

Download HIV sequences from [HIV Los Alamos Database] 
	(https://www.hiv.lanl.gov/content/sequence/HIV/mainpage.html). 
Make sure the file is in FASTA format

## Step 2

This script is reliant on the use of Bowtie2, an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. To acquire Bowtie2, (visit https://sourceforge.net/projects/bowtie-bio/files/bowtie2/). The contents of that directory will have to be added to your system's PATH.

```
export PATH=$PATH:/new/bowtie2

```

## Step 3

Before we start working with our file, we want to check if it is indeed a FASTA file. We can do this by running our 'def fasta' arguement in our python script.

## Step 4

Following this we want to align our sequences using Bowtie2. 
This can be done by building an index from our refrence file and aligning our 100 seqeunces from Los Alamos to our reference.

Using Bowtie package to align the sequences together:
```
# Build index from reference
bowtie2-build nl43.fasta refer

# Align the sequences and output as sam file
bowtie2 -x refer -f uc_hivdata.fasta -S newcut --very-sensitive-local -p2
```

## Step 5

After aligning we can isolate the area we want to work with. Using python, we can cut out the 5'UTR in our sequence from each patient and put in an outfile.

## Step 6

To calculate freqeuncies of nucleotides in the seqeunce, we must turn our strings into a matrix. Although we could use a dictionary, using a matrix will allow us to allows us to calculate nuc frequencies per nuc site (i.e. freq at position 695, 696, etc. for all the amalgamated sequences)

## Step 7 

Because we are looking at nuc fequency between patients and not within a sequence, we must flip our matrix. 

## Step 8

Using the counter command, we can calculate nuc frequencies. 





*Given how incredibly ambitious my original proposal design was, I have decided to start small and learn python a little better. So I have changed m project to calculating nucleotide frequencies in the 5' UTR from patients in the Los Alomos database.* 
