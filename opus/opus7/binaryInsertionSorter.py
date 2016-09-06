#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: binaryInsertionSorter.py,v $
#   $Revision: 1.8 $
#
#   $Id: binaryInsertionSorter.py,v 1.8 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the BinaryInsertionSorter class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.8 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.sorter import Sorter

#{
class BinaryInsertionSorter(Sorter):
    """
    Binary insertion sorter.
    """

    def __init__(self):
        """
        (BinaryInsertionSorter) -> None
        Constructor.
        """
        super(BinaryInsertionSorter, self).__init__()

    def _sort(self):
        """
        (BinaryInsertionSorter) -> None
        Sorts the elements of the array.
        """
        for i in xrange(1, self._n):
            tmp = self._array[i]
            left = 0
            right = i
            while left < right:
                middle = (left + right) / 2
                if tmp >= self._array[middle]:
                    left = middle + 1
                else:
                    right = middle
            j = i
            while j > left:
                self.swap(j - 1, j)
                j -= 1
#}>a

    def main(*argv):
        "BinaryInsertionSorter test program."
        print BinaryInsertionSorter.main.__doc__
        Sorter.test(BinaryInsertionSorter(), 100, 123)
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(BinaryInsertionSorter.main(*sys.argv))
