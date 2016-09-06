#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/23 12:23:21 $
#   $RCSfile: doubleEndedPriorityQueue.py,v $
#   $Revision: 1.12 $
#
#   $Id: doubleEndedPriorityQueue.py,v 1.12 2003/09/23 12:23:21 brpreiss Exp $
#

"""
Provides the DoubleEndedPriorityQueue class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/23 12:23:21 $"
__version__ = "$Revision: 1.12 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.priorityQueue import PriorityQueue

class DoubleEndedPriorityQueue(PriorityQueue):
    """
    Base class from which all double-ended priority queues are derived.
    """

    def __init__(self):
        """
        (DoubleEndedPriorityQueue) -> None
        Constructor.
        """
        super(DoubleEndedPriorityQueue, self).__init__()

    def getMax(self):
        pass
    getMax = abstractmethod(getMax)

    max = property(
        fget = lambda self: self.getMax())

    def dequeueMax(self):
        pass
    dequeueMax = abstractmethod(dequeueMax)

    def test(pqueue):
        "DoubleEndedPriorityQueue test program."
        print DoubleEndedPriorityQueue.test.__doc__
        PriorityQueue.test(pqueue)
        print pqueue
        pqueue.enqueue(3)
        pqueue.enqueue(1)
        pqueue.enqueue(4)
        pqueue.enqueue(1)
        pqueue.enqueue(5)
        pqueue.enqueue(9)
        pqueue.enqueue(2)
        pqueue.enqueue(6)
        pqueue.enqueue(5)
        pqueue.enqueue(4)
        print pqueue
        while not pqueue.isEmpty:
            obj = pqueue.dequeueMax()
            print obj
    test = staticmethod(test)
