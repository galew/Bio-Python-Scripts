import sys
import re

#Takes in filtered data and gives ratios of bases if between 40:60 and 90:10
#Usage: for ASE, enter command
#       python pileup_script.py inputfile.tsv outputfile10.tsv 

pileup_input = open(sys.argv[1],"r")
pileup_output = open(sys.argv[2],"w")

#with open("50_text_filter.txt", "rb") as pileup_input, open("50_text_pileup.txt", "wb") as pileup_output:
counter = 0
for line in pileup_input:
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
        #count_N = 0
        #count_ins = 0
        #count_del = 0
        #count_amb = 0

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
##                if ref.upper() == 'N':
##                        count_N += count_base

        counts = [count_A, count_T, count_G, count_C]
        sorted_counts = sorted(counts, key=int, reverse=True)
        count = count - sorted_counts[2] - sorted_counts[3]
        first = sorted_counts[0]
        second = sorted_counts[1]
        if first == count_A:
                first = str(first) + "A"
        elif first == count_T:
                first = str(first) + "T"
        elif first == count_G:
                first = str(first) + "G"
        elif first == count_C:
                first = str(first) + "C"

        if second == count_A:
                second = str(second) + "A"
        elif second == count_T:
                second = str(second) + "T"
        elif second == count_G:
                second = str(second) + "G"
        elif second == count_C:
                second = str(second) + "C"
                
        top_count = int(max(counts))
        if count == 0:
            break
        else:
            ratio = float(top_count)/int(count)
            observed = sorted_counts[0]
            expected = float(count)/2
            chi2 = ((observed - expected)**2)/expected
            if ratio > float(0.5) and ratio < float(0.9):                   #control ratio here
                    if count >= 50:
                        counter += 1
                        pileup_output.write(chrom + "\t" + pos + "\t" + ref + "\t" + str(count) +"\t" + first + "\t" + second + "\t" + str(chi2) + "\n")
                    #elif count >= 15:
                            #pileup_output15.write(chrom + "\t" + pos + "\t" + ref + "\t" + str(count) + "\t" + str(count_A) + "A" + "\t" + str(count_G) + "G" + "\t" + str(count_C) + "C" + "\t" + str(count_T) + "T" + "\n")
#pileup_output.write(str(counter))
#pileup_input.seek(0)

print "Complete"
