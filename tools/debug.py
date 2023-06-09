#!/usr/bin/env python3
import ipdb

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###

    # Author.py tests

    # Initializing author attributes
    class Author:
        def __init__(self, name):
            self._name = name
            self._article = []

        # getter for authors name
        @property
        def name(self):
            return self._name
        
        # list of Article instances the author has written
        @property
        def articles(self):
            return self._article

        # **unique** list of Magazine instances for which the author has contributed to
        def magazine(self):
            pk_magazines = set()
            for article in self._article:
                pk_magazines.add(article.magazine())
            return list(pk_magazines)

        # Creates a new Article instance and associates it with that author and that magazine.
        def article_instance(self, magazine, title):
            article = Article(self, magazine, title)
            self._article.append(article)
        
        #  **unique** list of strings with the categories of the magazines the author has contributed to
        def topic_areas(self):
            pk_mag_categories = set()
            for article in self._article:
                pk_mag_categories.add(article.magazine().category())
            return list(pk_mag_categories)



    medrine = Author("Joy")
    print(medrine.name)






# Magazine.py tests
    
    import weakref


# Initializing magazine class attributes
    class Magazine():
        # List to store all magazine instances
        magazine_instances = []

        # Initializing magazine class attributes
        def __init__ (self, name, category):
            self._name = name
            self._category = category
            self.__class__.magazine_instances.append(weakref.proxy(self))
            self.article = []
            self._contributors = []


            
        # Getter for magazine name
        @property
        def name(self):
            return self._name 

        # Setter for magazine name
        @name.setter
        def name(self, value):
            self._name = value
            
        # Getter for magazine category
        @property
        def category(self):
            return self._category

        # Setter for magazine category
        @category.setter
        def category(self, value):
            self._category = value

        @classmethod
        def all(cls):
            return cls.magazine_instances

        # list of Author instances who have written for this magazine
        def add_contributor(self, author):
            self._contributors.append(author)
        
        # Given a string of magazine's name, this method returns the first magazine object that matches
        @classmethod
        def find_by_name(cls, name):
            for magazine in cls.magazine_instances:
                if magazine.name() == name:
                    return magazine
            return None

        # Returns an list strings of the titles of all articles written for that magazine        # 
        @classmethod
        def article_titles(cls):
            titles = []
            for magazine in cls.magazine_instances:
                for article in magazine.articles():
                    titles.append(article.title())
            return titles

        # Returns an list of authors who have written more than 2 articles for the magazine
        def contributing_authors(self):
            author_counts = {}
            for article in self.article:
                author = article.author()
                if author in author_counts:
                    author_counts[author] += 1
                else:
                    author_counts[author] = 1
            return [author for author, count in author_counts.items() if count > 2]

    # Magazine magazine_instances
    love = Magazine("Loving", "Relationships")

    faith = Magazine("Faithful", "Worship")
    # print(love.name)
    love.name = "Hope"
    print(love.name)

    # print(love.category)
    love.category = "Sports"
    print(love.category)


    # List of all Magazine magazine_instances
    for instance in Magazine.magazine_instances:
        # print(instance.name)
        # print(instance.category)
        print(Magazine.magazine_instances)








# Article.py tests

    import weakref


    class Article:
        # list to store all article instances
        article_instances = []

        # Initializing article attributes
        def __init__(self, author, magazine, title):
            self._author = author
            self._magazine = magazine
            self._title = title
            self.__class__.article_instances.append(weakref.proxy(self))

        # Getter for article's title
        @property
        def title(self):
            return self._title

        # Getter for article's author
        @property
        def author(self):
            return self._author

        # Getter for article's magazine
        @property
        def magazine(self):
            return self._magazine


    # Instances of Article
    this_love = Article("Medrine", "Parents", "This Love")
    this_book = Article("Job", "Say", "This Yes")
    print(this_love)
    print(this_love.title)
    print(this_love.author)
    print(this_love.magazine)

    # List of all Article Instances
    for instance in Article.article_instances:
        print(Article.article_instances)
















# DO NOT REMOVE THIS
    ipdb.set_trace()
