#!/usr/bin/env python3
import ipdb

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###

    class Author:

        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name
            
        @name.setter
        def name(self):
            pass


    medrine = Author("Joy")
    medrine.name













# DO NOT REMOVE THIS
    ipdb.set_trace()
