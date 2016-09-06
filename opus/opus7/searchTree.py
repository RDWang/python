#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/23 23:01:18 $
#   $RCSfile: searchTree.py,v $
#   $Revision: 1.21 $
#
#   $Id: searchTree.py,v 1.21 2003/09/23 23:01:18 brpreiss Exp $
#

"""
Provides the SearchTree class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/23 23:01:18 $"
__version__ = "$Revision: 1.21 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from opus7.abstractmethod import abstractmethod
from opus7.tree import Tree
from opus7.searchableContainer import SearchableContainer
from opus7.preOrder import PreOrder
from opus7.inOrder import InOrder
from opus7.postOrder import PostOrder
from opus7.printingVisitor import PrintingVisitor

#{
class SearchTree(Tree, SearchableContainer):
    """
    Base class from which all search tree classes are derived.
    """

    def __init__(self):
        """
        (SearchTree) -> None
        Constructor.
        """
        super(SearchTree, self).__init__()

    def getMin(self):
        pass
    getMin = abstractmethod(getMin)

    min = property(
        fget = lambda self: self.getMin())

    def getMax(self):
        pass
    getMax = abstractmethod(getMax)

    max = property(
        fget = lambda self: self.getMax())
#}>a

    def test(tree):
        "SearchTree test program."
        for i in xrange(1, 8):
            tree.insert(i)
        visitor = PrintingVisitor()
        print tree
        print "Breadth-first traversal"
        tree.breadthFirstTraversal(visitor)
        visitor.finish()
        print "Preorder traversal"
        tree.depthFirstTraversal(PreOrder(visitor))
        visitor.finish()
        print "Inorder traversal"
        tree.depthFirstTraversal(InOrder(visitor))
        visitor.finish()
        print "Postorder traversal"
        tree.depthFirstTraversal(PostOrder(visitor))
        visitor.finish()
        print "Using iterator"
        for i in tree:
            print i
        print "Using depth-first generator"
        for i in tree.depthFirstGenerator(Tree.INORDER):
            print i
        print "Using breadth-first generator"
        for i in tree.breadthFirstGenerator():
            print i
        print "Withdrawing 4"
        obj = tree.find(4)
        try:
            tree.withdraw(obj)
            print tree
        except NotImplementedError:
            print "Withdraw not implemented."
    test = staticmethod(test)
