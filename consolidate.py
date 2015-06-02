import sys
import re

#takes in ASE_pval file and adds the qval column to output file
#Usage: python consolidate.py ASE_pval.txt qval.txt ASE_qval.txt

pval_input = open(sys.argv[1],"r")
qvalues = open(sys.argv[2],"r")
consolidate_output = open(sys.argv[3],"w")

qvalList = []

for qvalue_line in qvalues:
    qvalue_line = qvalue_line.rstrip('\n')
    qvalue_linesplit = re.split('\t',qvalue_line)

    qv = qvalue_linesplit[0]
    qvalList.append(qv)

counter = 0

for line in pval_input:
    line=line.rstrip('\n')
    linesplit = re.split('\t',line)

    chrom1 = linesplit[0]
    pos1 =  linesplit[1]
    ref1 =  linesplit[2]
    count1 =  int(linesplit[3])
    first1 = linesplit[4]
    second1 = linesplit[5]
    chi21 = float(linesplit[6])
    pval1 = float(linesplit[7])
    #qvalues.seek(0)

    consolidate_output.write(chrom1 + "\t" + pos1 + "\t" + ref1 + "\t" + str(count1) +"\t" + first1 + "\t" + second1 + "\t" + str(chi21) + "\t" + str(pval1) + "\t" + str(qvalList[counter]) + "\n")
    counter += 1
    
        
print "Complete"
