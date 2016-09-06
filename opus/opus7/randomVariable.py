#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/25 01:07:38 $
#   $RCSfile: randomVariable.py,v $
#   $Revision: 1.15 $
#
#   $Id: randomVariable.py,v 1.15 2003/09/25 01:07:38 brpreiss Exp $
#

"""
Provides the RandomVariable class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/25 01:07:38 $"
__version__ = "$Revision: 1.15 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.object import Object

#{
class RandomVariable(Object):
    """
    Base class from which all random variables are derived.
    """

    def __init__(self):
        """
        (RandomVariable) -> None
        Constructor.
        """
        super(RandomVariable, self).__init__()

    def getNext(self):
        pass
    getNext = abstractmethod(getNext)

    next = property(
        fget = lambda self: self.getNext())
#}>a

    def _compareTo(self, obj):
        """
        (RandomVariable, RandomVariable) -> int

        Compares this random variable with the given random variable.
        """
        assert isinstance(self, obj.__class__)
        raise NotImplementedError

