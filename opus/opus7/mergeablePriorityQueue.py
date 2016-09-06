#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: mergeablePriorityQueue.py,v $
#   $Revision: 1.9 $
#
#   $Id: mergeablePriorityQueue.py,v 1.9 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the MergeablePriorityQueue class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.9 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.priorityQueue import PriorityQueue

#{
class MergeablePriorityQueue(PriorityQueue):
    """
    A mergeable priority queue.
    """

    def __init__(self):
        """
        (MergeablePriorityQueue) -> None
        Constructor.
        """
        super(MergeablePriorityQueue, self).__init__()

    def merge(self, queue):
        pass
    merge = abstractmethod(merge)
#}>a

    def test(pqueue):
        "MergeablePriorityQueue test program."
        print MergeablePriorityQueue.test.__doc__
