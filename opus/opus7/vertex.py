#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/27 00:43:09 $
#   $RCSfile: vertex.py,v $
#   $Revision: 1.12 $
#
#   $Id: vertex.py,v 1.12 2003/09/27 00:43:09 brpreiss Exp $
#

"""
Provides the Vertex class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/27 00:43:09 $"
__version__ = "$Revision: 1.12 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.object import Object

#{
class Vertex(Object):
    """
    Base class from which all graph vertex classes are derived.
    """

    def __init__(self):
        """
        (Vertex) -> None
        Constructor.
        """
        super(Vertex, self).__init__()

    def getNumber(self): pass
    getNumber = abstractmethod(getNumber)
    number = property(
        fget = lambda self: self.getNumber())

    def getWeight(self): pass
    getWeight = abstractmethod(getWeight)
    weight = property(
        fget = lambda self: self.getWeight())

    def getIncidentEdges(self): pass
    getIncidentEdges = abstractmethod(getIncidentEdges)
    incidentEdges = property(
        fget = lambda self: self.getIncidentEdges())

    def getEmanatingEdges(self): pass
    getEmanatingEdges = abstractmethod(getEmanatingEdges)
    emanatingEdges = property(
        fget = lambda self: self.getEmanatingEdges())

    def getPredecessors(self): pass
    getPredecessors = abstractmethod(getPredecessors)
    predecessors = property(
        fget = lambda self: self.getPredecessors())

    def getSuccessors(self): pass
    getSuccessors = abstractmethod(getSuccessors)
    successors = property(
        fget = lambda self: self.getSuccessors())
#}>a
