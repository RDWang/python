#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/07/23 17:54:18 $
#   $RCSfile: rectangle.py,v $
#   $Revision: 1.3 $
#
#   $Id: rectangle.py,v 1.3 2003/07/23 17:54:18 brpreiss Exp $
#

"""
Provides the Rectangle class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/07/23 17:54:18 $"
__version__ = "$Revision: 1.3 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.graphicalObject import GraphicalObject

#{
class Rectangle(GraphicalObject):
    """
    A rectangle.
    """

    def __init__(self, center, height, width):
        """
        (Rectangle, Point, int, int) -> None
        Constructs a rectangle with the given center, height, and width.
        """
        super(Rectangle, self).__init__(center)
        self._height = height
        self._width = width

    def draw(self):
        """
        (Rectangle) -> None
        Draws this rectangle.
        """
        # ...
#[
        pass
#]
#}>a
