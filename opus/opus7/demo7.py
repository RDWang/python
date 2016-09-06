#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: demo7.py,v $
#   $Revision: 1.11 $
#
#   $Id: demo7.py,v 1.11 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Demo7 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.11 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.setAsArray import SetAsArray
from opus7.setAsBitVector import SetAsBitVector
from opus7.multisetAsArray import MultisetAsArray
from opus7.multisetAsLinkedList import MultisetAsLinkedList
from opus7.partitionAsForest import PartitionAsForest
from opus7.partitionAsForestV2 import PartitionAsForestV2
from opus7.partitionAsForestV3 import PartitionAsForestV3

class Demo7(object):

    def main(*argv):
        "Demostration program number 7."
        print Demo7.main.__doc__
        SetAsArray.main(*argv)
        SetAsBitVector.main(*argv)
        MultisetAsArray.main(*argv)
        MultisetAsLinkedList.main(*argv)
        PartitionAsForest.main(*argv)
        PartitionAsForestV2.main(*argv)
        PartitionAsForestV3.main(*argv)
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Demo7.main(*sys.argv))
