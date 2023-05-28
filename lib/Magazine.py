class Magazine:
    def __init__ (self, name, category):
        self._name = name
        self._category = category

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


love = Magazine("Loving", "Relationships")
# print(love.name)
love.name = "Hope"
print(love.name)

# print(love.category)
love.category = "Sports"
print(love.category)

