#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/07/23 17:54:18 $
#   $RCSfile: circle.py,v $
#   $Revision: 1.3 $
#
#   $Id: circle.py,v 1.3 2003/07/23 17:54:18 brpreiss Exp $
#

"""
Provides the Circle class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/07/23 17:54:18 $"
__version__ = "$Revision: 1.3 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.graphicalObject import GraphicalObject

#{
class Circle(GraphicalObject):
    """
    A circle.
    """

    def __init__(self, center, radius):
        """
        (Circle, Point, int) -> None
        Constructs a circle with the given center and radius.
        """
        super(Circle, self).__init__(center)
        self._radius = radius

    def draw(self):
        """
        (Circle) -> None
        Draws this circle.
        """
        # ...
#[
        pass
#]
#}>a
