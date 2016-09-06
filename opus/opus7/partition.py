#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:16 $
#   $RCSfile: partition.py,v $
#   $Revision: 1.10 $
#
#   $Id: partition.py,v 1.10 2003/09/06 16:35:16 brpreiss Exp $
#

"""
Provides the Partition class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:16 $"
__version__ = "$Revision: 1.10 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.set import Set

#{
class Partition(Set):
    """
    Base class from which all partitions are derived.
    """

    def __init__(self, n):
        super(Partition, self).__init__(n)

    def find(self, obj):
        pass
    find = abstractmethod(find)

    def join(self, s, t):
        pass
    join = abstractmethod(join)
#}>a

    def test(p):
        "Partition test program."
        print Partition.test.__doc__
        print p
        s2 = p.find(2)
        s4 = p.find(4)
        p.join(s2, s4)
        s3 = p.find(3)
        s4b = p.find(4)
        p.join(s3, s4b)
        print p
    test = staticmethod(test)
