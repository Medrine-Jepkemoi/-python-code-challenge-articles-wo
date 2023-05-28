#!/usr/bin/env python3
import ipdb

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###

# Author.py tests
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


gazine.py tests
    import weakref


    class Magazine():

        instances = []
        def __init__ (self, name, category):
            self._name = name
            self._category = category
            self.__class__.instances.append(weakref.proxy(self))

        @property
        def name(self):
            return self._name 


        @name.setter
        def name(self, value):
            self._name = value
            

        @property
        def category(self):
            return self._category

        @category.setter
        def category(self, value):
            self._category = value

    # Magazine instances
    love = Magazine("Loving", "Relationships")

    faith = Magazine("Faithful", "Worship")
    # print(love.name)
    love.name = "Hope"
    print(love.name)

    # print(love.category)
    love.category = "Sports"
    print(love.category)


    # List of all Magazine Instances
    for instance in Magazine.instances:
        # print(instance.name)
        # print(instance.category)
        print(Magazine.instances)


# Article.py tests

    import weakref


    class Article:
        instances = []

        def __init__(self, author, magazine, title):
            self._author = author
            self._magazine = magazine
            self._title = title
            self.__class__.instances.append(weakref.proxy(self))


        @property
        def title(self):
            return self._title


    # Instances of Article
    this_love = Article("Medrine", "Parents", "This Love")
    print(this_love)
    print(this_love.title)

    # List of all Article instances
    for instance in Article.instances:
        print(Article.instances)
















# DO NOT REMOVE THIS
    ipdb.set_trace()
