#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/25 01:07:38 $
#   $RCSfile: object.py,v $
#   $Revision: 1.25 $
#
#   $Id: object.py,v 1.25 2003/09/25 01:07:38 brpreiss Exp $
#

"""
Provides the Object class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/25 01:07:38 $"
__version__ = "$Revision: 1.25 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.abstractmethod import abstractmethod
from opus7.metaclass import Metaclass

#{
class Object(object):
    """
    Base class from which all objects are derived.
    """

#}@head

#{
    # ...
#}@tail

#{
    def __init__(self):
        """
        (Object) -> None
        Constructor.
        """
        super(Object, self).__init__()

    def __cmp__(self, obj):
        """
        (Object, Object) -> int
        Compares this object with the given object.
        """
        if isinstance(self, obj.__class__):
            return self._compareTo(obj)
        elif isinstance(obj, self.__class__):
            return -obj._compareTo(self)
        else:
            return cmp(self.__class__.__name__,
                obj.__class__.__name__)

    def _compareTo(self, obj):
        pass
    _compareTo = abstractmethod(_compareTo)
#}>a

#{
    __metaclass__ = Metaclass
#}>b

    def main(*argv):
        "Object test program."
        print Object.main.__doc__
        try:
            object = Object()
        except TypeError, msg:
            print "Caught TypeError: %s" % str(msg)
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Object.main(*sys.argv))
