#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: demo1.py,v $
#   $Revision: 1.7 $
#
#   $Id: demo1.py,v 1.7 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Demo1 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.7 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.denseMatrix import DenseMatrix
from opus7.sparseMatrixAsArray import SparseMatrixAsArray
from opus7.sparseMatrixAsVector import SparseMatrixAsVector
from opus7.sparseMatrixAsLinkedList import SparseMatrixAsLinkedList

class Demo1(object):

    def main(*argv):
        "Demostration program number 1."
        print Demo1.main.__doc__
        DenseMatrix.main([])
        SparseMatrixAsArray.main([])
        SparseMatrixAsVector.main([])
        SparseMatrixAsLinkedList.main([])
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Demo1.main(*sys.argv))
