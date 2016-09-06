#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/06 16:35:15 $
#   $RCSfile: application6.py,v $
#   $Revision: 1.6 $
#
#   $Id: application6.py,v 1.6 2003/09/06 16:35:15 brpreiss Exp $
#

"""
Provides the Application6 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/06 16:35:15 $"
__version__ = "$Revision: 1.6 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.expressionTree import ExpressionTree

class Application6(object):

    def main(*argv):
        "Application program number 6. (expression tree)"
        print Application6.main.__doc__
        expression = ExpressionTree.parsePostfix(sys.stdin)
        sys.stdout.write(str(expression) + "\n")
        return 0
    main = staticmethod(main)

if __name__ == "__main__":
    sys.exit(Application6.main(*sys.argv))
