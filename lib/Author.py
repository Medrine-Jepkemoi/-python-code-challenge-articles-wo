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

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
    def topic_areas(self):
        return list({article.magazine().category() for article in self._articles})


medrine = Author("Joy")
print(medrine.name)

