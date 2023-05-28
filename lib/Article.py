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
