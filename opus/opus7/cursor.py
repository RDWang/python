#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/25 01:07:38 $
#   $RCSfile: cursor.py,v $
#   $Revision: 1.28 $
#
#   $Id: cursor.py,v 1.28 2003/09/25 01:07:38 brpreiss Exp $
#

"""
Provides the Cursor class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/25 01:07:38 $"
__version__ = "$Revision: 1.28 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.abstractmethod import abstractmethod
from opus7.object import Object

#{
class Cursor(Object):
    """
    Base class from which all cursor classes are derived.
    """

    def __init__(self, list):
        """
        (Cursor) -> None
        Constructor.
        """
        super(Cursor, self).__init__()
	self._list = list

    def getDatum(self):
        pass
    getDatum = abstractmethod(getDatum)

    datum = property(
        fget = lambda self: self.getDatum())

    def insertAfter(self, obj):
        pass
    insertAfter = abstractmethod(insertAfter)

    def insertBefore(self, obj):
        pass
    insertBefore = abstractmethod(insertBefore)

    def withdraw(self, obj):
        pass
    withdraw = abstractmethod(withdraw)
#}>a

    def _compareTo(self, obj):
        """
        (Cursor, Cursor) -> int

        Compares this cursor with the given cursor.
        """
        assert isinstance(self, obj.__class__)
        raise NotImplementedError

    def main(*argv):
        "Cursor test program."
        print Cursor.main.__doc__
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Cursor.main(*sys.argv))
