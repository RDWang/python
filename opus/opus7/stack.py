#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/23 17:24:17 $
#   $RCSfile: stack.py,v $
#   $Revision: 1.24 $
#
#   $Id: stack.py,v 1.24 2003/09/23 17:24:17 brpreiss Exp $
#

"""
Provides the Stack class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/23 17:24:17 $"
__version__ = "$Revision: 1.24 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.container import Container

#{
class Stack(Container):
    """
    Base class from which all stack classes are derived.
    """

    def __init__(self):
        """
        (Stack) -> None
        Constructor
        """
        super(Stack, self).__init__()

    def getTop(self):
        pass
    getTop = abstractmethod(getTop)

    top = property(
        fget = lambda self: self.getTop())

    def push(self, obj):
        pass
    push = abstractmethod(push)

    def pop(self):
        pass
    pop = abstractmethod(pop)
#}>a

    def test(stack):
        "Stack test program."
        print Stack.test.__doc__
        for i in xrange(6):
            if not stack.isFull:
                stack.push(i)
        print stack
	print "Using iterator"
	for obj in stack:
	    print obj
	print "Top is", stack.top
        print "Popping"
        while not stack.isEmpty:
            obj = stack.pop()
            print obj
    test = staticmethod(test)
