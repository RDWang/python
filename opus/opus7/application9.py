#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: application9.py,v $
#   $Revision: 1.6 $
#
#   $Id: application9.py,v 1.6 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Application9 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.6 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.algorithms import Algorithms

class Application9(object):

    def main(*argv):
        "Application program number 9. (equivalence classes)"
        print Application9.main.__doc__
        Algorithms.equivalenceClasses(sys.stdin, sys.stdout)
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Application9.main(*sys.argv))
