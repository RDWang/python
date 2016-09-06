#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/23 12:23:21 $
#   $RCSfile: solution.py,v $
#   $Revision: 1.11 $
#
#   $Id: solution.py,v 1.11 2003/09/23 12:23:21 brpreiss Exp $
#

"""
Provides the Solution class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/23 12:23:21 $"
__version__ = "$Revision: 1.11 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.object import Object

#{
class Solution(Object):
    """
    Base class from which all solution space nodes are derived.
    """

    def __init__(self):
        """
        (Solution) -> None
        Constructor.
        """
        super(Solution, self).__init__()

    def getIsFeasible(self):
        pass
    getIsFeasible = abstractmethod(getIsFeasible)

    isFeasible = property(
        fget = lambda self: self.getIsFeasible())

    def getIsComplete(self):
        pass
    getIsComplete = abstractmethod(getIsComplete)

    isComplete = property(
        fget = lambda self: self.getIsComplete())

    def getObjective(self):
        pass
    getObjective = abstractmethod(getObjective)

    objective = property(
        fget = lambda self: self.getObjective())

    def getBound(self):
        pass
    getBound = abstractmethod(getBound)

    bound = property(
        fget = lambda self: self.getBound())

    def getSuccessors(self):
        pass
    getSuccessors = abstractmethod(getSuccessors)

    successors = property(
        fget = lambda self: self.getSuccessors())
#}>a
