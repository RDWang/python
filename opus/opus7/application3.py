#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: application3.py,v $
#   $Revision: 1.6 $
#
#   $Id: application3.py,v 1.6 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Application3 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.6 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.polynomial import Polynomial
from opus7.polynomialAsOrderedList import PolynomialAsOrderedList
from opus7.polynomialAsSortedList import PolynomialAsSortedList

class Application3(object):

    def main(*argv):
        "Application program number 3."
        print Application3.main.__doc__
        p1 = PolynomialAsOrderedList()
        p1.addTerm(Polynomial.Term(4.5, 5))
        p1.addTerm(Polynomial.Term(3.2, 14))
        print p1
        p1.differentiate()
        print p1

        p2 = PolynomialAsSortedList()
        p2.addTerm(Polynomial.Term(7.8, 0))
        p2.addTerm(Polynomial.Term(1.6, 14))
        p2.addTerm(Polynomial.Term(9.999, 27))
        print p2
        p2.differentiate()
        print p2

        p3 = PolynomialAsSortedList()
        p3.addTerm(Polynomial.Term(0.6, 13))
        p3.addTerm(Polynomial.Term(-269.973, 26))
        p3.addTerm(Polynomial.Term(1000, 1000))
        print p3
        print p2 + p3
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Application3.main(*sys.argv))
