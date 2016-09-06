#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/27 00:43:09 $
#   $RCSfile: edge.py,v $
#   $Revision: 1.12 $
#
#   $Id: edge.py,v 1.12 2003/09/27 00:43:09 brpreiss Exp $
#

"""
Provides the Edge class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/27 00:43:09 $"
__version__ = "$Revision: 1.12 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.object import Object

#{
class Edge(Object):
    """
    Base class from which all graph edge classes are derived.
    """

    def __init__(self):
        """
        (Edge) -> None
        Constructor.
        """
        super(Edge, self).__init__()

    def getV0(self): pass
    getV0 = abstractmethod(getV0)
    v0 = property(
        fget = lambda self: self.getV0())

    def getV1(self): pass
    getV1 = abstractmethod(getV1)
    v1 = property(
        fget = lambda self: self.getV1())

    def getWeight(self): pass
    getWeight = abstractmethod(getWeight)
    weight = property(
        fget = lambda self: self.getWeight())

    def getIsDirected(self): pass
    getIsDirected = abstractmethod(getIsDirected)
    isDirected = property(
        fget = lambda self: self.getIsDirected())

    def mateOf(self, vertex): pass
    mateOf = abstractmethod(mateOf)
#}>a
