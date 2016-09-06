#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: demo3.py,v $
#   $Revision: 1.14 $
#
#   $Id: demo3.py,v 1.14 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Demo3 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.14 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.orderedListAsArray import OrderedListAsArray
from opus7.orderedListAsLinkedList import OrderedListAsLinkedList
from opus7.sortedListAsArray import SortedListAsArray
from opus7.sortedListAsLinkedList import SortedListAsLinkedList

class Demo3(object):

    def main(*argv):
        "Demostration program number 3."
        print Demo3.main.__doc__
        OrderedListAsArray.main(*argv)
        OrderedListAsLinkedList.main(*argv)
        SortedListAsArray.main(*argv)
        SortedListAsLinkedList.main(*argv)
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Demo3.main(*sys.argv))
