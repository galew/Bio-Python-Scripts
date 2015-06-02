import sys
import re

#Takes in shared unique/shared file and counts how many ASE are in each gene
#Usage: enter command
#       geneCount_script.py ASErefGene_shared.txt outputfile.txt

refGene_input = open(sys.argv[1],"r")
geneCount_output = open(sys.argv[2],"w")

geneList = []
geneCountList = []

#with open("50_ASErefGene_shared_15807_15810.txt", "rb") as refGene_input:

for refGene_line in refGene_input:
    refGene_line = refGene_line.rstrip('\n')
    refGene_linesplit = re.split('\t',refGene_line)

    #chrom = refGene_linesplit[0]
    gene = refGene_linesplit[11]     #change column where gene name is here

    geneList.append(gene)

for i in geneList:
    if i not in geneCountList:
        geneCountList.append(i)

counter = 0
#with open("geneCount.txt", "wb") as geneCount_output:

for i in geneCountList:
    newline = i.rstrip('\n\r')
    geneCount_output.write(newline)
    geneCount_output.write("\t" + str(geneList.count(geneCountList[counter])) + "\n")
    counter += 1
