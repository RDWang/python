#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: experiment2.py,v $
#   $Revision: 1.7 $
#
#   $Id: experiment2.py,v 1.7 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Experiment2 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.7 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.demo9 import Demo9

class Experiment2(object):
    """
    Program tha measures the running times of both
    a recursive and a non-recursive method to compute
    the Fibonacci numbers.
    """

    def main(*argv):
        "Experiment2 test program."
        print "4"
        print "sort"
        print "length"
        print "seed"
        print "time"
        seeds = ["1", "57", "12345", "7252795", "3127"]
        for seed in seeds:
            lengths = ["10", "25", "50", "75",
                "100", "250", "500", "750",
                "1000", "1250", "1500", "1750", "2000"]
            for length in lengths:
                Demo9.main(["Demo9.main", length, seed, "7"])
            lengths = ["3000", "4000", "5000", "6000",
                "7000", "8000", "9000", "10000"]
            for length in lengths:
                Demo9.main(["Demo9.main", length, seed, "3"])
            lengths = ["20000", "30000", "40000", "50000",
                "60000", "70000", "80000", "90000", "100000"]
            for length in lengths:
                Demo9.main(["Demo9.main", length, seed, "1"])
        return 0
    main = staticmethod(main)

if __name__== "__main__":
    sys.exit(Experiment2.main(*sys.argv))
