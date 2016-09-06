#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: demo2.py,v $
#   $Revision: 1.14 $
#
#   $Id: demo2.py,v 1.14 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Demo2 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.14 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.stackAsArray import StackAsArray
from opus7.stackAsLinkedList import StackAsLinkedList
from opus7.queueAsArray import QueueAsArray
from opus7.queueAsLinkedList import QueueAsLinkedList
from opus7.dequeAsArray import DequeAsArray
from opus7.dequeAsLinkedList import DequeAsLinkedList

class Demo2(object):

    def main(*argv):
        "Demostration program number 2."
        print Demo2.main.__doc__
        StackAsArray.main(*argv)
        StackAsLinkedList.main(*argv)
        QueueAsArray.main(*argv)
        QueueAsLinkedList.main(*argv)
        DequeAsArray.main(*argv)
        DequeAsLinkedList.main(*argv)
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Demo2.main(*sys.argv))
