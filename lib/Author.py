class Author:

    def __init__(self, name):
        self._name = name
        self.article_list = []

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self):
        pass

    @property
    def articles(self):
        return self._articles

    @property
    def magazines(self):
        unique_magazine = set()
        for article in self.article_list:
            unique_magazine.add(article.magazine)
        return list(unique_magazine)


medrine = Author("Joy")
print(medrine.name)

