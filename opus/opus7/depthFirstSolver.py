#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/07/23 17:54:18 $
#   $RCSfile: depthFirstSolver.py,v $
#   $Revision: 1.3 $
#
#   $Id: depthFirstSolver.py,v 1.3 2003/07/23 17:54:18 brpreiss Exp $
#

"""
Provides the DepthFirstSolver class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/07/23 17:54:18 $"
__version__ = "$Revision: 1.3 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.solver import Solver

#{
class DepthFirstSolver(Solver):
    """
    Depth-first solver.
    """

    def __init__(self):
        """
        (DepthFirstSolver) -> None
        Constructor.
        """
        super(DepthFirstSolver, self).__init__()

    def search(self, current):
        """
        (DepthFirstSolver, Solution) -> Solution
        Does a depth-first traversal of the solution space
        starting from the given node.
        """
        if current.isComplete:
            self.updateBest(current)
        else:
            for successor in current.successors:
                self.search(successor)
#}>a
