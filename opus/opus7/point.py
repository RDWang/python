#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/07/23 17:54:18 $
#   $RCSfile: point.py,v $
#   $Revision: 1.3 $
#
#   $Id: point.py,v 1.3 2003/07/23 17:54:18 brpreiss Exp $
#

"""
Provides the Point class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/07/23 17:54:18 $"
__version__ = "$Revision: 1.3 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

#{
class Point(object):
    """
    Represents a point in in image.
    """

    def __init__(self, x, y):
        """
        (Point, int, int) -> None
        Constructs a point with the given coordinates.
        """
        self._x = x
        self._y = y
    # ...
#}>a
