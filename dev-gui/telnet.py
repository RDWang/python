#!/usr/bin/env python

def telnetdo(HOST=None, USER=None, PASS=None, COMMAND=None): #define a function
    import telnetlib, sys
    finish = '[root@AT8410X ~]#'
    if not HOST:
        try:
            HOST = sys.argv[1]
            USER = sys.argv[2]
            PASS = sys.argv[3]
            COMMAND = sys.argv[4]
        except:
            print "Usage: telnetdo.py host user pass command"
 #           return
    msg = ['Debug messages:\n'] 
    #print msg	
    tn = telnetlib.Telnet() 
    try:
        tn.open(HOST)
    except:
        print "Cannot open host"
        return
    #msg.append(tn.expect(['login:'], 5)) #
    print "login"
    print tn.read_eager()
    tn.read_until("AT8410X login:")
    tn.write(USER + '\n')
    if PASS:
        #msg.append(tn.expect(['Password:'], 5))
        tn.read_until("Password:")
        tn.write(PASS + '\n')
    #msg.append(tn.expect([USER], 5))
    if COMMAND:
        print tn.read_until(finish)
        print "start cmd\n"
        tn.write(COMMAND + '\n')
        print "end start cmd"
        tmp = tn.read_some()
        print "end read cmd"
        print tmp
    while 1:
        com = raw_input("enter an commad:\n")
        print com 
        tn.write(com + '\n')
        tmp = tn.read_until(finish)
        print tmp
    #msg.append(tn.expect(['#'], 5))
    tn.write("exit\n")
    tn.close()
    del tn
    return tmp

if __name__ == '__main__':
    print "start telnet\n"
    telnetdo()
