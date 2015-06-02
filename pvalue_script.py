import sys
import re
import scipy
from scipy import stats

#Takes in pileup data and adds pval column
#Usage: python pvalue_script.py pileupinput.txt ASE_pvalue.txt

pileup_input = open(sys.argv[1],"r")
pval_output = open(sys.argv[2],"w")
#pval_only = open(sys.argv[3],"w")

for line in pileup_input:
        #print line
        line=line.rstrip('\n')
        linesplit = re.split('\t',line)

        # store basic dataset in some variables
        chrom = linesplit[0]
        pos =  linesplit[1]
        ref =  linesplit[2]
        count =  int(linesplit[3])
        first = linesplit[4]
        second = linesplit[5]
        chi2 = float(linesplit[6])

        pval = 1 - stats.chi2.cdf(chi2, 1)

        pval_output.write(chrom + "\t" + pos + "\t" + ref + "\t" + str(count) +"\t" + first + "\t" + second + "\t" + str(chi2) + "\t" + str(pval) + "\n")
        
print "Complete"
