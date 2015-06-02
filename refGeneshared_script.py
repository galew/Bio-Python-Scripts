import sys
import re

#Checks between two ASE files and outputs those shared ASEs without gene names
#Usage: enter command
#       python shared_script.py ASEinput1.txt ASEinput2.txt outputfile.tsv

cross_input1 = open(sys.argv[1],"r")
cross_input2 = open(sys.argv[2],"r")
match_output = open(sys.argv[3],"w")

#with open("15810_cross.txt", "rb") as cross_input, open("15807_cross.txt", "rb") as geneName_input, open("15810_15807_match.txt", "wb") as match_output:

for cross_line1 in cross_input1:
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
    cName = cross_linesplit1[8]
    cross_input2.seek(0)
    
    for cross_line2 in cross_input2:
        cross_line2 = cross_line2.rstrip('\n')
        cross_linesplit2 = re.split('\t',cross_line2)

        chrom2 = cross_linesplit2[0]
        pos2 =  cross_linesplit2[1]
        ref2 = cross_linesplit2[2]
        count2 = int(cross_linesplit2[3])
        first2 = cross_linesplit2[4]
        second2 = cross_linesplit2[5]
        qval2 = cross_linesplit2[6]
        gName = cross_linesplit2[8]

        if cName == gName:
            if chrom1 == chrom2:
                if pos1 == pos2:
                    match_output.write(chrom1 + "\t" + pos1 + "\t" + ref1 + "\t" + str(count1) + "\t" + first1 + "\t" + second1 + "\t" + qval1 + "\t" + str(count2) + "\t" + first2 + "\t" + second2 + "\t" + qval2 + "\t" + cName + "\n")

print "Complete"
