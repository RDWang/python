#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: medianOfThreeQuickSorter.py,v $
#   $Revision: 1.7 $
#
#   $Id: medianOfThreeQuickSorter.py,v 1.7 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the MedianOfThreeQuickSorter class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.7 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.sorter import Sorter
from opus7.quickSorter import QuickSorter

#{
class MedianOfThreeQuickSorter(QuickSorter):
    """
    Quick sorter that uses median-of-three pivot selection.
    """

    def __init__(self):
        """
        (MedianOfThreeQuickSorter) -> None
        Constructor.
        """
        super(MedianOfThreeQuickSorter, self).__init__()

    def selectPivot(self, left, right):
        """
        (MedianOfThreeQuickSorter, int, int) -> int
        Sorts the left, middle, and right array element
        and returns the position of the middle element as the pivot.
        """
        middle = (left + right) / 2
        if self._array[left] > self._array[middle]:
            self.swap(left, middle)
        if self._array[left] > self._array[right]:
            self.swap(left, right)
        if self._array[middle] > self._array[right]:
            self.swap(middle, right)
        return middle
#}>a

    def main(*argv):
        "MedianOfThreeQuickSorter test program."
        print MedianOfThreeQuickSorter.main.__doc__
        Sorter.test(MedianOfThreeQuickSorter(), 100, 123)
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(MedianOfThreeQuickSorter.main(*sys.argv))
