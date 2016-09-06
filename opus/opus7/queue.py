#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/23 12:23:21 $
#   $RCSfile: queue.py,v $
#   $Revision: 1.23 $
#
#   $Id: queue.py,v 1.23 2003/09/23 12:23:21 brpreiss Exp $
#

"""
Provides the Queue class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/23 12:23:21 $"
__version__ = "$Revision: 1.23 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.container import Container

#{
class Queue(Container):
    """
    Base class from which all queue classes are derived.
    """

    def __init__(self):
        """
        (Queue) -> None
        Constructor.
        """
        super(Queue, self).__init__()

    def getHead(self):
        pass
    getHead = abstractmethod(getHead)

    head = property(
        fget = lambda self: self.getHead())

    def enqueue(self, obj):
        pass
    enqueue = abstractmethod(enqueue)

    def dequeue(self):
        pass
    dequeue = abstractmethod(dequeue)
#}>a

    def test(queue):
        "Queue test program."
        print Queue.test.__doc__
        for i in xrange(6):
            if queue.isFull:
                break;
            queue.enqueue(i)
        print queue
        print queue.head
        while not queue.isEmpty:
            obj = queue.dequeue()
            print obj
    test = staticmethod(test)
