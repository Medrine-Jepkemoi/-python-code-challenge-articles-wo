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

    @property
    def author(self):
        return self._author

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

# List of all Article instances
for instance in Article.instances:
    print(Article.instances)
