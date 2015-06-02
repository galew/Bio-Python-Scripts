import sys
import re

#Used to find unique and shared ASEs between infected and controls. Use 2 sample shared, then 3 sample shared
#Usage: enter command
#       python unique_shared_script.py ASErefGene_shared2.txt ASErefGene_shared3.txt sharedOutput unique1_output unique2_output

class Unique:
    def __init__(self, chrom, pos, ref, count, first, second, qval, name):
        self.chrom = chrom
        self.pos = pos
        self.ref = ref
        self.count = count
        self.first = first
        self.second = second
        self.qval = qval
        self.name = name

input1 = open(sys.argv[1],"r")
input2 = open(sys.argv[2],"r")
sharedOutput = open(sys.argv[3],"w")
unique1_output = open(sys.argv[4],"w")
unique2_output = open(sys.argv[5],"w")

infected = []
control = []

for line2 in input2:
    line2 = line2.rstrip('\n')
    linesplit2 =re.split('\t',line2)

    chrom2 = linesplit2[0]
    pos2 = linesplit2[1]
    ref2 = linesplit2[2]
    count3 = linesplit2[3]
    first3 = linesplit2[4]
    second3 = linesplit2[5]
    qval3 = linesplit2[6]
    count4 = linesplit2[7]
    first4 = linesplit2[8]
    second4 = linesplit2[9]
    qval4 = linesplit2[10]
    count5 = linesplit2[11]
    first5 = linesplit2[12]
    second5 = linesplit2[13]
    qval5 = linesplit2[14]
    cName = linesplit2[15]
    countTotal2 = (int(count3) + int(count4) + int(count5))/3
    firstTotal2 = (int(first3[:-1]) + int(first4[:-1]) + int(count5[:-1]))/3
    secondTotal2 = (int(second3[:-1]) + int(second4[:-1]) + int(second5[:-1]))/3
    qvalAve2 = (float(qval3) + float(qval4) + float(qval5))/3

    control.append(Unique(chrom2, pos2, ref2, countTotal2, firstTotal2, secondTotal2, qvalAve2, cName))

for line1 in input1:
    line1 = line1.rstrip('\n')
    linesplit1 = re.split('\t',line1)

    chrom1 = linesplit1[0]
    pos1 = linesplit1[1]
    ref1 = linesplit1[2]
    count1 = linesplit1[3]
    first1 = linesplit1[4]
    second1 = linesplit1[5]
    qval1 = linesplit1[6]
    count2 = linesplit1[7]
    first2 = linesplit1[8]
    second2 = linesplit1[9]
    qval2 = linesplit1[10]
    iName = linesplit1[11]
    countTotal1 = (int(count1) + int(count2))/2
    firstTotal1 = (int(first1[:-1]) + int(first2[:-1]))/2
    secondTotal1 = (int(second1[:-1]) + int(second2[:-1]))/2
    qvalAve1 = (float(qval1) + float(qval2))/2

    infected.append(Unique(chrom1, pos1, ref1, countTotal1, firstTotal1, secondTotal1, qvalAve1, iName))

    input2.seek(0)

    for line2 in input2:
        line2 = line2.rstrip('\n')
        linesplit2 =re.split('\t',line2)

        chrom2 = linesplit2[0]
        pos2 = linesplit2[1]
        ref2 = linesplit2[2]
        count3 = linesplit2[3]
        first3 = linesplit2[4]
        second3 = linesplit2[5]
        qval3 = linesplit2[6]
        count4 = linesplit2[7]
        first4 = linesplit2[8]
        second4 = linesplit2[9]
        qval4 = linesplit2[10]
        count5 = linesplit2[11]
        first5 = linesplit2[12]
        second5 = linesplit2[13]
        qval5 = linesplit2[14]
        cName = linesplit2[15]
        countTotal2 = (int(count3) + int(count4) + int(count5))/3
        firstTotal2 = (int(first3[:-1]) + int(first4[:-1]) + int(count5[:-1]))/3
        secondTotal2 = (int(second3[:-1]) + int(second4[:-1]) + int(second5[:-1]))/3
        qvalAve2 = (float(qval3) + float(qval4) + float(qval5))/3

        #control.append(Unique(chrom2, pos2, ref2, countTotal2, firstTotal2, secondTotal2, qvalAve2, cName))     #SEEK ABOVE CAUSES DUPLICATES

        if chrom1 == chrom2:
            if pos1 == pos2:
                if cName == iName:
                    cTot = (countTotal1 + countTotal2)/2
                    fTot = (firstTotal1 + firstTotal2)/2
                    sTot = (secondTotal1 + secondTotal2)/2
                    qvalTot = (qvalAve1 + qvalAve2)/2
                    sharedOutput.write(chrom1 + "\t" + pos1 + "\t" + ref1 + "\t" + str(cTot) + "\t" + str(fTot) + "\t" + str(sTot) + "\t" + str(qvalTot) + "\t" + cName + "\n")


def build_unique(filename):
    unique = set()
    with open(filename) as f:
        for line in f:
            unique.add(tuple(line.split()[:2]))
    return unique

f1 = build_unique(sys.argv[1])
f2 = build_unique(sys.argv[2])


for res1 in (f1 - f2):
    #unique1_output.write(str(res1) + "\n")
    for i in infected:
        if i.chrom in res1 and i.pos in res1:
            unique1_output.write(i.chrom + "\t" + i.pos + "\t" + i.ref + "\t" + str(i.count) + "\t" + str(i.first) + "\t" + str(i.second) + "\t" + str(i.qval) + "\t" + i.name + "\n")
            #f1.remove(res)

for res2 in (f2 - f1):
    #unique2_output.write(str(res2) + "\n")
    for i in control:
        if i.chrom in res2 and i.pos in res2:
            unique2_output.write(i.chrom + "\t" + i.pos + "\t" + i.ref + "\t" + str(i.count) + "\t" + str(i.first) + "\t" + str(i.second) + "\t" + str(i.qval) + "\t" + i.name + "\n")
            #f1.remove(res)

print "Complete"
