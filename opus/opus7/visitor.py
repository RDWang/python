#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/25 01:07:38 $
#   $RCSfile: visitor.py,v $
#   $Revision: 1.24 $
#
#   $Id: visitor.py,v 1.24 2003/09/25 01:07:38 brpreiss Exp $
#

"""
Provides the Visitor class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/25 01:07:38 $"
__version__ = "$Revision: 1.24 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.object import Object

#{
class Visitor(Object):
    """
    Visitor class.
    """

#}@head

#{
#}@tail

#{
    def __init__(self):
        """
        (Visitor) -> None
        Constructs this visitor.
        """
        super(Visitor, self).__init__()

    def visit(self, obj):
        """
        (Visitor, Object) -> None
        Default visit method does nothing.
        """
        pass
    
    def getIsDone(self):
        """
        (Visitor) -> bool
        Default isDone_get method returns false always.
        """
        return False

    isDone = property(
        fget = lambda self: self.getIsDone())
#}>a

    def _compareTo(self, obj):
        """
        (Visitor, Visitor) -> int

        Compares this visitor with the given visitor.
        """
        assert isinstance(self, obj.__class__)
        raise NotImplementedError

    def main(*argv):
        "Visitor test program."
        print Visitor.main.__doc__
        v = Visitor()
        print v.isDone
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Visitor.main(*sys.argv))
