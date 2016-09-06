#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: demo10.py,v $
#   $Revision: 1.12 $
#
#   $Id: demo10.py,v 1.12 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Demo10 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.12 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.graphAsMatrix import GraphAsMatrix
from opus7.digraphAsMatrix import DigraphAsMatrix
from opus7.graphAsLists import GraphAsLists
from opus7.digraphAsLists import DigraphAsLists

class Demo10(object):

    def main(*argv):
        "Demostration program number 10."
        print Demo10.main.__doc__
        GraphAsMatrix.main([])
        DigraphAsMatrix.main([])
        GraphAsLists.main([])
        DigraphAsLists.main([])
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Demo10.main(*sys.argv))
