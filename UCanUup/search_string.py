import sys
import re 

one_line = []
txt_count = 0

#search UCanUup string main
if __name__=="__main__":
    print "Start count UCanUup number"

    argvlens = len(sys.argv)
    if argvlens < 1:
       print "please input: count file name"

    print sys.argv[1]
    fl_file = sys.argv[1]

    f = open(fl_file)
    list_of_all_line = f.readlines()
    for one_line in list_of_all_line:
        txt_line = re.findall("UCanUup",one_line)
        txt_count = txt_count + txt_line.count("UCanUup")
#        print txt_count

    print("Total UCanUup number is %d"%(txt_count))

