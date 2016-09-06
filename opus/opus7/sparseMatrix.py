#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/07/23 17:54:18 $
#   $RCSfile: sparseMatrix.py,v $
#   $Revision: 1.4 $
#
#   $Id: sparseMatrix.py,v 1.4 2003/07/23 17:54:18 brpreiss Exp $
#

"""
Provides the SparseMatrix class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/07/23 17:54:18 $"
__version__ = "$Revision: 1.4 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.matrix import Matrix

class SparseMatrix(Matrix):
    """
    Base class from which all sparse matrix classes are derived.
    """

    def __init__(self, numberOfRows, numberOfColums):
        """
        (SparseMatrix, int, int) -> None
        Constructs a sparse matrix with the given number of rows and columns.
        """
        super(SparseMatrix, self).__init__(numberOfRows, numberOfColums)
