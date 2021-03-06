#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:16 $
#   $RCSfile: straightInsertionSorter.py,v $
#   $Revision: 1.8 $
#
#   $Id: straightInsertionSorter.py,v 1.8 2003/09/06 16:35:16 brpreiss Exp $
#

"""
Provides the StraightInsertionSorter class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:16 $"
__version__ = "$Revision: 1.8 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.sorter import Sorter

#{
class StraightInsertionSorter(Sorter):
    """
    Straight insertion sorter.
    """

    def __init__(self):
        """
        (StraightInsertionSorter) -> None
        Sorts the elements of the array.
        """
        super(StraightInsertionSorter, self).__init__()

    def _sort(self):
        """
        (StraightInsertionSorter) -> None
        Sorts the elements of the array.
        """
        for i in xrange(1, self._n):
            j = i
            while j > 0 and self._array[j - 1] > self._array[j]:
                self.swap(j, j - 1)
                j -= 1
#}>a

    def main(*argv):
        "StraightInsertionSorter test program."
        print StraightInsertionSorter.main.__doc__
        Sorter.test(StraightInsertionSorter(), 100, 123)
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(StraightInsertionSorter.main(*sys.argv))
