import math
import sys
import csv


#f1_file = "/home/lwang/otdr/otdr_12-5-25.csv"
#f2_file = "/home/lwang/otdr/otdr_34-5-25.csv"
#outfile = "/home/lwang/otdr/process_csv/outfile.csv"
f1_file = ""
f2_file = ""
outfile = ""
outfile12 = []
outfile34 = []

def read_csv_file():
    """"process csv 
    function 
    """

    f1 =open(f1_file)
    f2 = open(f2_file)
    reader = csv.reader(f1)

    CsvItem = [row for row in reader]
    for item in CsvItem:
        outfile12.append(item[0:5])

    reader2 = csv.reader(f2)
    C2 = [row for row in reader2]
    for item1 in C2:
        outfile34.append(item1[5:9])

    num1 = len(outfile12)
    num2 = len(outfile34)
    print num1,num2

    if num1 > num2:
        num = num1
    else:
        num = num2

    with open(outfile,'w') as csvfile:
        spamwriter = csv.writer(csvfile,delimiter=',')
        for i in range(num):
            outf = outfile12[i]+outfile34[i]
            spamwriter.writerow(outf)
            print outf 


#process csv main
if __name__=="__main__":
    print "Start process csv file to create new csv"
    argvlens = len(sys.argv)
    if argvlens < 4:
       print "please input: inputfile1 inputfile2 outoutfile"
    print sys.argv[1]
    f1_file = sys.argv[1]
    f2_file = sys.argv[2]
    outfile = sys.argv[3]
    read_csv_file()


