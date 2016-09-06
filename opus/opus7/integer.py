#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/25 01:07:38 $
#   $RCSfile: integer.py,v $
#   $Revision: 1.4 $
#
#   $Id: integer.py,v 1.4 2003/09/25 01:07:38 brpreiss Exp $
#

"""
Provides the Integer class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/25 01:07:38 $"
__version__ = "$Revision: 1.4 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
import warnings
from opus7.object import Object

#{
class Integer(int, Object):
    """
    Integer class.
    """

#}@head

#{

    # ...
#}@tail

    def __init__(self, obj):
        """
        (Integer, object) -> None
        Constructs a string with the string representation of the given object.
        The Object metaclass provides a __new__ method
        that initializes the str instance, so none is defined here.
        """
        pass

    def _compareTo(self, obj):
        """
        (Integer, Integer) -> int

        Compares this string with the given string.
        """
        assert isinstance(self, obj.__class__)
        return cmp(int(self), int(obj))

#{
    def __hash__(self):
        """
        (Integer) -> int
        Hashes this string.
        """
	return self & sys.maxint
#}>a

    def testHash():
        "Integer hash test program."
        print Integer.testHash.__doc__
	print "57=%d" % hash(Integer(57))
	print "-123=%d" % hash(Integer(-123))
    testHash = staticmethod(testHash)

    def main(*argv):
        "Integer test program."
        print Integer.main.__doc__
        Integer.testHash()
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Integer.main(*sys.argv))
