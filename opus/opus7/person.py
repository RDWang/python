#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/07/23 17:54:18 $
#   $RCSfile: person.py,v $
#   $Revision: 1.6 $
#
#   $Id: person.py,v 1.6 2003/07/23 17:54:18 brpreiss Exp $
#

"""
Provides the Person class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/07/23 17:54:18 $"
__version__ = "$Revision: 1.6 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

#{
class Person(object):
    """
    Represents a person.
    """

    FEMALE = 0
    MALE = 1

    def __init__(self, name, sex):
        """
        (Person, str, int) -> None
        Constructs a person with the given name and sex.
        """
        super(Person, self).__init__()
        self._name = name
        self._sex = sex

    def __str__(self):
        """
        (Person) -> str
        Returns a string representation of this person.
        """
        return str(self._name)
#}>a
