#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/07/23 17:54:18 $
#   $RCSfile: square.py,v $
#   $Revision: 1.3 $
#
#   $Id: square.py,v 1.3 2003/07/23 17:54:18 brpreiss Exp $
#

"""
Provides the Square class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/07/23 17:54:18 $"
__version__ = "$Revision: 1.3 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.rectangle import Rectangle

#{
class Square(Rectangle):
    """
    A square.
    """

    def __init__(self, center, width):
        """
        (Square, Point, width) -> None
        Constructs a square with the given width (and height).
        """
        super(Square, self).__init__(center, width, width)
#}>a
