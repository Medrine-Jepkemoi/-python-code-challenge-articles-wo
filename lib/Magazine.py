import weakref


class Magazine():

    instances = []
    def __init__ (self, name, category):
        self._name = name
        self._category = category
        self.__class__.instances.append(weakref.proxy(self))
        self.articles = []
        

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

    def contributors(self):
        return list({article.author() for article in self._articles})
        
    @classmethod
    def find_by_name()

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






