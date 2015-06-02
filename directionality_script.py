import sys
import re

#Checks if directionality of the reads match
#Usage: enter command
#       python directionality_script.py ASErefGene_shared.txt  sameDirection.txt oppositeDirection.txt noMatch.txt

input1 = open(sys.argv[1],"r")
same_output = open(sys.argv[2],"w")
opp_output = open(sys.argv[3],"w")
noMatch_output = open(sys.argv[4],"w")

for cross_line1 in input1:
    #print line
    cross_line1 = cross_line1.rstrip('\n')
    cross_linesplit1 = re.split('\t',cross_line1)

    # store basic dataset in some variables
    chrom1 = cross_linesplit1[0]
    pos1 =  cross_linesplit1[1]
    ref1 = cross_linesplit1[2]
    count1 = int(cross_linesplit1[3])
    first1 = cross_linesplit1[4]
    second1 = cross_linesplit1[5]
    qval1 = cross_linesplit1[6]
    count3 = int(cross_linesplit1[7])
    first3 = cross_linesplit1[8]
    second3 = cross_linesplit1[9]
    qval3 = cross_linesplit1[10]
    cName = cross_linesplit1[11]

    first1_base = first1[-1]
    second1_base = second1[-1]
    first3_base = first3[-1]
    second3_base = second3[-1]

    if first1_base == first3_base and second1_base == second3_base:
        same_output.write(chrom1 + "\t" + pos1 + "\t" + ref1 + "\t" + str(count1) + "\t" + first1 + "\t" + second1 + "\t" + qval1 + "\t" + str(count3) + "\t" + first3 + "\t" + second3 + "\t" + qval3 + "\t" + cName + "\n")
    elif first1_base == second3_base and first3_base == second1_base:
        opp_output.write(chrom1 + "\t" + pos1 + "\t" + ref1 + "\t" + str(count1) + "\t" + first1 + "\t" + second1 + "\t" + qval1 + "\t" + str(count3) + "\t" + first3 + "\t" + second3 + "\t" + qval3 + "\t" + cName + "\n")
    else:
        noMatch_output.write((chrom1 + "\t" + pos1 + "\t" + ref1 + "\t" + str(count1) + "\t" + first1 + "\t" + second1 + "\t" + qval1 + "\t" + str(count3) + "\t" + first3 + "\t" + second3 + "\t" + qval3 + "\t" + cName + "\n")

print "Complete"
                            


##    for line2 in input2:
##        line2 = line2.rstrip('\n')
##        linesplit2 = re.split('\t',line2)
##
##        chrom2 = linesplit2[0]
##        pos2 = linesplit2[1]
##        ref2 = linesplit2[2]
##        count2 = int(linesplit2[3])
##        first2 = linesplit2[4]
##        second2 = linesplit2[5]
##        first2_base = first2[-1]
##        second2_base = second2[-1]
##        qval2 = linesplit2[6]
##
##        if first1_base == first2_base and second1_base == second2_base:
##            
            
