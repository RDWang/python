import os
import os.path
import sys
import re 
import string
import shutil

path = "/home/lwang/fcgi"
new_path = "/home/lwang/disk2/myself/python/change_file_name/fcgi_to_cgi"
cgi_path = "/home/lwang/disk2/myself/python/change_file_name/cgi"
src_cgi_path = "/home/lwang/pages"

if __name__=="__main__":
    """
    process all file in the path 
    """

    #create new path
    if not os.path.exists(new_path):
        os.mkdir(new_path,0755)

    #copy file to new path
    filelist = os.listdir(path)
    os.chdir(path)
    for filename in filelist:
        if re.match("^fcgi_.*\.[c,h]$",filename,0):
            new_filename = filename[5:]
            new_filename = new_path + '/' + new_filename
            if not os.path.exists(new_filename):
                shutil.copyfile(filename,new_filename)
               # print filename
               # print "**"
               # print new_filename
    
    #process cgi dir
    if os.path.exists(src_cgi_path):
        if not os.path.exists(cgi_path):
            os.mkdir(cgi_path,0755)

    for root,dirname,filename in os.walk(src_cgi_path,True):
#        print("root= ",root,"dir= ",dirname,"filename= ",filename)
#        length = len(dirname)
#        print length
        for num in dirname:
            tmpfile = root + '/'+ num
            listfile = os.listdir(tmpfile)
            length = len(listfile)
            print length
            if length == 0:
                print "list is null,exit..."
                continue
            print "cd ",tmpfile
            os.chdir(tmpfile)
            for listtmpfile in listfile:
                dstfile = cgi_path + '/' + listtmpfile
                print dstfile
                if not os.path.exists(dstfile):
                    shutil.copyfile(listtmpfile, dstfile)

