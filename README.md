# Bio-Python-Scripts

filter_script.py: Filters out unwanted characters from pileup and cuts out SNPs if the minimum number of reads does not meet the threshold given.
SNPcount_script.py: Counts the number of SNPs after being filtered.
pileup_script.py: Takes filtered data file in and counts the readings for each base within the given ratios, outputting the two highest SNPs in two new columns as well as giving the chi squared value.
pvalue_script.py: Takes in a pileup file and finds the p value from the chi squared value.
qvalue_script.py: Takes the p value and finds the q value, written to a separate file.
consolidate.py: Appends the q values to the original pileup script in a new column.
qfilter_script.py: Filters out reads if the q value does not meet the 0.05 base line.
crossref_script.py: Checks across the refGene file for if the SNP is part of a gene and outputs the gene names in a new column.
refGeneshared_script.py: Takes two files with gene names attached and checks if outputs the commonly shared SNPs.  This is used for the first two shared files, if there is a third in the group, you would use refGeneshared_script2.py to compare and add the results from the third file.
directionality_script.py: Checks if directionality of a two shared file is the same, different, or has no match.  Will output each to separate files.
unique_shared_script.py: Used after the infected and controlled shared files are created, producing a shared list of SNPs across both infected and control files as well as two unique files, listing SNPs that were unique to the infected, and to the controls. 
geneCount_script.py: Takes in a file with gene names and counts the number of SNPs were in each gene found.
