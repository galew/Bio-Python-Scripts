#Filters out unwanted characters from pileup and SNPs with min number of reads
# Usage: enter command
#        python filter_script.py inputfile.tsv outputfile.tsv

import sys
import re

#read input file and create an output file
pileup_input = open(sys.argv[1],"r")
pileup_output = open(sys.argv[2],"w")
#pileup_output15 = open(sys.argv[3],"w")

#with open("text.txt", "rb") as pileup_input, open("50_text_filter.txt", "wb") as pileup_output:

# go through each line of input file and remove patterns. While loops are used to filter the presence of repeated patterns

for lines in pileup_input:
        lines=lines.rstrip('\n')
        linesplit = re.split('\t',lines)
        line = linesplit[4]
        test = linesplit[3]

        if int(test) >= 50:              #control min num of reads here
                # filter deletions
                while (re.search('(-[0-9]+[ACGTNacgtn]+)',line)):
                        if re.search('(-[0-9]+)',line):
                                count = re.search('(-[0-9]+)',line).group(1)  
                                str_command = '(-[0-9]+[A-Za-z]{' + str(abs(int(count))) + '})'
                                line = re.sub(str_command,'',line)

                # filter insertion
                while (re.search('(\+[0-9]+[ACGTNacgtn]+)',line)):
                        if re.search('(\+[0-9]+)',line):
                                count = re.search('(\+[0-9]+)',line).group(1)
                                str_command = '(\+[0-9]+[A-Za-z]{' + str(abs(int(count))) + '})'
                                line = re.sub(str_command,'',line)

                # filter ^ and its next chatacter
                while (re.search('\^.{1}',line)):
                        line = re.sub('\^.{1}','',line)

                # write the output file
                #if int(test) > 10:
                pileup_output.write(linesplit[0] + "\t" + linesplit[1] + "\t" + linesplit[2] + "\t" + linesplit[3] + "\t" + line + "\t" + linesplit[5]  + "\n")
         
print "Complete"
