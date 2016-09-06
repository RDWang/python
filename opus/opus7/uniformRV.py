#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/26 15:02:08 $
#   $RCSfile: uniformRV.py,v $
#   $Revision: 1.7 $
#
#   $Id: uniformRV.py,v 1.7 2003/09/26 15:02:08 brpreiss Exp $
#

"""
Provides the UniformRV class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/26 15:02:08 $"
__version__ = "$Revision: 1.7 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.randomVariable import RandomVariable
from opus7.randomNumberGenerator import RandomNumberGenerator

#{
class UniformRV(RandomVariable):
    """
    A random variable uniformly distributed on the interval (u, v].
    """

    def __init__(self, u, v):
        """
        (UniformRV, double, double) -> None
        Constructs a uniform random variable on the given interval.
        """
        self._u = u;
        self._v = v;

    def getNext(self):
        """
        (UniformRV) -> double
        Returns the next sample.
        """
        return self._u + (self._v - self._u) * \
	    RandomNumberGenerator.next
#}>a

    def main(*argv):
	"UniformRV test program."
	print UniformRV.main.__doc__
	rv = UniformRV(0,100)
	for i in range(10):
	    print rv.next
	return 0
    main = staticmethod(main)

if __name__== "__main__":
    sys.exit(UniformRV.main(*sys.argv))
