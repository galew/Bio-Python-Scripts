import sys
import re

#Takes in an ASE file with chi2, pval, qval and compares against refGene, prints out name of gene
#Usage: enter command
#       python crossref_script.py pileupinput.tsv refGeneinput.tsv outputfile.tsv

pileup_input = open(sys.argv[1],"r")
refGene_input = open(sys.argv[2],"r")
crossref_output = open(sys.argv[3],"w")

#with open("15807_pileup.txt", "rb") as pileup_input, open("refGene.txt", "rb") as refGene, open("15807_cross.txt", "wb") as crossref_output:

for pileup_line in pileup_input:
    #print line
    pileup_line = pileup_line.rstrip('\n')
    pileup_linesplit = re.split('\t',pileup_line)

    # store basic dataset in some variables
    chrom1 = pileup_linesplit[0]
    pos =  pileup_linesplit[1]
    ref = pileup_linesplit[2]
    count = int(pileup_linesplit[3])
    first = pileup_linesplit[4]
    second = pileup_linesplit[5]
    qval = pileup_linesplit[6]
    refGene_input.seek(0)
    
    for refGene_line in refGene_input:
        refGene_line = refGene_line.rstrip('\n')
        refGene_linesplit = re.split('\t',refGene_line)

        name1 = refGene_linesplit[1]
        chrom2 = refGene_linesplit[2]
        start = refGene_linesplit[4]
        end = refGene_linesplit[5]
        name2 = refGene_linesplit[12]

        if chrom1 == chrom2:
            if pos >= start and pos <= end:
                crossref_output.write(chrom1 + "\t" + pos + "\t" + ref + "\t" + str(count) + "\t" + first + "\t" + second + "\t" + qval + "\t" + name1 + "\t" + name2 + "\n")
			#else:
                #crossref_output.write(chrom1 + "\t" + pos + "\t" + ref + "\t" + str(count) + "\t" + str(count_A) + "\t" + str(count_G) + "\t" + str(count_C) + "\t" + str(count_T) + "\n")
        #else:
            #crossref_output.write(chrom1 + "\t" + pos + "\t" + ref + "\t" + str(count) + "\t" + str(count_A) + "\t" + str(count_G) + "\t" + str(count_C) + "\t" + str(count_T) + "\n")
		
		
print "Complete"
