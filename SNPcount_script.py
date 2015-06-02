import sys
import re

#Counts SNP total after filter (does not care about ratio)
#Usage: enter command
#       python SNPcount_script.py inputfile.tsv outputfile.tsv 

count_input = open(sys.argv[1],"r")
SNPcount_output = open(sys.argv[2],"w")
#SNPcount_output10 = open(sys.argv[3],"w")

#with open("15807_filterall.txt", "rb") as count_input, open("15807_allSNPcount.txt", "wb") as SNPcount_output:

counter = 0
for line in count_input:
        #print line
        line=line.rstrip('\n')
        linesplit = re.split('\t',line)

        # store basic dataset in some variables
        chrom = linesplit[0]
        pos =  linesplit[1]
        ref =  linesplit[2]
        count =  int(linesplit[3])
        
        # initiate all variables as zero
        count_base = 0
        count_A = 0
        count_T = 0
        count_G = 0
        count_C = 0

        #iterate over column five of pileup format and count ATGCN. Count . and , as base count and latter assign  it to ATGCN.
        for c in linesplit[4]:
                if c == '.' or c == ',':
                        count_base += 1
                elif c.upper() == 'A':
                        count_A += 1
                elif c.upper() == 'T':
                        count_T += 1
                elif c.upper() == 'G':
                        count_G += 1
                elif c.upper() == 'C':
                        count_C += 1
                elif c.upper() == 'N':
                        count -= 1
                elif c == '*':
                        count -= 1

        #assign count_base to anybase ATGC
        if ref.upper() == 'A':
                count_A += count_base
        if ref.upper() == 'T':
                count_T += count_base
        if ref.upper() == 'G':
                count_G += count_base
        if ref.upper() == 'C':
                count_C += count_base


        counts = [count_A, count_T, count_G, count_C]
        top_count = int(max(counts))

        if count != 0 or top_count != 0:
            #ratio = float(top_count)/int(count)
            #if ratio < float(1.0):                   #control ratio here
                counter += 1
                #if count >= 10:
                    #counter10++
                 
SNPcount_output.write(str(counter))
#SNPcount_output10.write(counter10)


print "Complete"
