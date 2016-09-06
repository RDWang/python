#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/23 12:23:21 $
#   $RCSfile: deque.py,v $
#   $Revision: 1.24 $
#
#   $Id: deque.py,v 1.24 2003/09/23 12:23:21 brpreiss Exp $
#

"""
Provides the Deque class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/23 12:23:21 $"
__version__ = "$Revision: 1.24 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.queue import Queue

#{
class Deque(Queue):
    """
    Represents a doubled-ended queue.
    """

    def __init__(self):
        """
        (Deque) -> None
        Constructor.
        """
        super(Deque, self).__init__()

    def getHead(self):
        pass
    getHead = abstractmethod(getHead)

    head = property(
        fget = lambda self: self.getHead())

    def getTail(self):
        pass
    getTail = abstractmethod(getTail)

    tail = property(
        fget = lambda self: self.getTail())

    def enqueueHead(self, obj):
        pass
    enqueueHead = abstractmethod(enqueueHead)

    def dequeueHead(self):
        """
        (Deque) -> Object
        Dequeues the head of this deque.
        """
        return self.dequeue()

    def enqueueTail(self, object):
        """
        (Deque, Object) -> None
        Enqueues the given object at the tail of this deque.
        """
        self.enqueue(object)

    def dequeueTail(self):
        pass
    dequeueTail = abstractmethod(dequeueTail)
#}>a

    def test(deque):
        "Deque test program."
        print Deque.test.__doc__
        for i in xrange(6):
            if deque.isFull:
                break
            deque.enqueueHead(i)
            if deque.isFull:
                break
            deque.enqueueTail(i)
        print deque
        print deque.head
        print deque.tail
        while not deque.isEmpty:
            obj = deque.dequeueHead()
            print obj
            if deque.isEmpty:
                break
            obj = deque.dequeueTail()
            print obj
    test = staticmethod(test)
