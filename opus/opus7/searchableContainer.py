#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:16 $
#   $RCSfile: searchableContainer.py,v $
#   $Revision: 1.19 $
#
#   $Id: searchableContainer.py,v 1.19 2003/09/06 16:35:16 brpreiss Exp $
#

"""
Provides the SearchableContainer class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:16 $"
__version__ = "$Revision: 1.19 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.abstractmethod import abstractmethod
from opus7.container import Container
from opus7.visitor import Visitor

#{
class SearchableContainer(Container):
    """
    Base class from which all searchable container classes are derived.
    """

    def __init__(self):
        """
        (SearchableContainer) -> None
        Constructor.
        """
        super(SearchableContainer, self).__init__()

    def __contains__(self, obj):
        pass
    __contains__ = abstractmethod(__contains__)

    def insert(self, obj):
        pass
    insert = abstractmethod(insert)

    def withdraw(self, obj):
        pass
    withdraw = abstractmethod(withdraw)

    def find(self, obj):
        pass
    find = abstractmethod(find)
#}>a

    def main(*argv):
        "SearchableContainer test program."
        print SearchableContainer.main.__doc__
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(SearchableContainer.main(*sys.argv))
