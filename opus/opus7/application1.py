#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: application1.py,v $
#   $Revision: 1.7 $
#
#   $Id: application1.py,v 1.7 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Application1 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.7 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.algorithms import Algorithms

class Application1(object):

    def main(*argv):
        "Application program number 1. (calculator)"
        print Application1.main.__doc__
        Algorithms.calculator(sys.stdin, sys.stdout)
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Application1.main(*sys.argv))
