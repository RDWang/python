#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: iterator.py,v $
#   $Revision: 1.3 $
#
#   $Id: iterator.py,v 1.3 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Base class from which all container iterators are derived.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.3 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.object import Object
from opus7.abstractmethod import abstractmethod

#{
class Iterator(Object):
    """
    Base class from which all container iterators are derived.
    """

#}@head

#{

    # ...
#}@tail

#{
    def __init__(self, container):
        """
        (Iterator, Container) -> None

        Constructs an iterator for the given container.
        """
        super(Object, self).__init__()
        self._container = container

    def __iter__(self):
        """
        (Iterator) -> Iterator

        Returns this iterator.
        """
        return self

    def next(self):
        pass
    next = abstractmethod(next)
#}>a

    def _compareTo(self, obj):
        """
        (Iterator, Iterator) -> int

        Compares this Iterator with the given Iterator.
        """
        raise MethodNotImplemented

    def main(*argv):
        "Iterator test program."
        print Iterator.main.__doc__
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Iterator.main(*sys.argv))
