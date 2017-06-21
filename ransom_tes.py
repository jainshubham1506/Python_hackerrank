class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)
        return self.data
    def addtwice(self, x):
        self.add(x)
        self.add(x)
        return self.data

print(Bag().add("hello"))
print(Bag().addtwice("world"))
print (Bag().data)