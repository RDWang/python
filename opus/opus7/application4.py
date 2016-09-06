#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: application4.py,v $
#   $Revision: 1.6 $
#
#   $Id: application4.py,v 1.6 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Application4 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.6 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.polynomial import Polynomial
from opus7.polynomialAsSortedList import PolynomialAsSortedList

class Application4(object):

    def main(*argv):
        "Application program number 4."
        print Application4.main.__doc__
        p1 = PolynomialAsSortedList()
        p1.addTerm(Polynomial.Term(4.5, 5))
        p1.addTerm(Polynomial.Term(3.2, 14))
        print p1

        p2 = PolynomialAsSortedList()
        p2.addTerm(Polynomial.Term(7.8, 3))
        p2.addTerm(Polynomial.Term(1.6, 14))
        p2.addTerm(Polynomial.Term(9.999, 27))
        print p2

        p3 = p1 + p2
        print p3
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Application4.main(*sys.argv))
