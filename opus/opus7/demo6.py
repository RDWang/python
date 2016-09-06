#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: demo6.py,v $
#   $Revision: 1.9 $
#
#   $Id: demo6.py,v 1.9 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Demo6 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.9 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.binaryHeap import BinaryHeap
from opus7.leftistHeap import LeftistHeap
from opus7.binomialQueue import BinomialQueue
from opus7.deap import Deap

class Demo6(object):

    def main(*argv):
        "Demostration program number 6."
        print Demo6.main.__doc__
        BinaryHeap.main(*argv)
        LeftistHeap.main(*argv)
        BinomialQueue.main(*argv)
        Deap.main(*argv)
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Demo6.main(*sys.argv))
