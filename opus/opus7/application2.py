#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: application2.py,v $
#   $Revision: 1.7 $
#
#   $Id: application2.py,v 1.7 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Application2 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.7 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.algorithms import Algorithms
from opus7.naryTree import NaryTree

class Application2(object):

    def buildTree(lo, hi):
        """
        (char, char) -> NaryTree
        Builds an N-ary tree that contains keys in the xrange from lo to hi.
        """
        mid = chr((ord(lo) + ord(hi)) / 2)
        result = NaryTree (2, mid)
        if lo < mid:
            result.attachSubtree(0,
                Application2.buildTree(lo, chr(ord(mid) - 1)))
        if hi > mid:
            result.attachSubtree(1,
                Application2.buildTree(chr(ord(mid) + 1), hi))
        return result
    buildTree = staticmethod(buildTree)

    def main(*argv):
        "Application program number 2."
        print Application2.main.__doc__
        print "Should be: dbfaceg."
        tree = Application2.buildTree("a", "g")
        Algorithms.breadthFirstTraversal(tree)
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Application2.main(*sys.argv))
