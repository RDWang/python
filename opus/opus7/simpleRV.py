#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/26 14:46:27 $
#   $RCSfile: simpleRV.py,v $
#   $Revision: 1.6 $
#
#   $Id: simpleRV.py,v 1.6 2003/09/26 14:46:27 brpreiss Exp $
#

"""
Provides the SimpleRV class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/26 14:46:27 $"
__version__ = "$Revision: 1.6 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.randomVariable import RandomVariable
from opus7.randomNumberGenerator import RandomNumberGenerator

#{
class SimpleRV(RandomVariable):
    """
    A random variable uniformly distributed on the interval (0,1].
    """

    def getNext(self):
        """
        (SimpleRV) -> double
        Returns the next sample.
        """
        return RandomNumberGenerator.next
#}>a

    def main(*argv):
	"SimpleRV test program."
	print SimpleRV.main.__doc__
	rv = SimpleRV()
	for i in range(10):
	    print rv.next
	return 0
    main = staticmethod(main)

if __name__== "__main__":
    sys.exit(SimpleRV.main(*sys.argv))
