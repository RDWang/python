#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:16 $
#   $RCSfile: prePostVisitor.py,v $
#   $Revision: 1.10 $
#
#   $Id: prePostVisitor.py,v 1.10 2003/09/06 16:35:16 brpreiss Exp $
#

"""
Provides the PrePostVisitor class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:16 $"
__version__ = "$Revision: 1.10 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.visitor import Visitor

#{
class PrePostVisitor(Visitor):
    """
    Pre/Post visitor class.
    """

#}@head

#{
#}@tail

#{
    def __init__(self):
        """
        (PrePostVisitor) -> None
        Constructor.
        """
        super(PrePostVisitor, self).__init__()

    def preVisit(self, obj):
        """
        (PrePostVisitor, Object) -> None
        Default pre-visit method does nothing.
        """
        pass

    def inVisit(self, obj):
        """
        (PrePostVisitor, Object) -> None
        Default in-visit method does nothing.
        """
        pass

    def postVisit(self, obj):
        """
        (PrePostVisitor, Object) -> None
        Default post-visit method does nothing.
        """
        pass

    visit = inVisit
#}>a

    def main(*argv):
        "PrePostVisitor test program."
        print PrePostVisitor.main.__doc__
        v = PrePostVisitor()
        print v.isDone
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(PrePostVisitor.main(*sys.argv))
