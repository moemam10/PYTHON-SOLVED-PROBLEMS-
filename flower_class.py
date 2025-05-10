
class Flower:
    def __init__(self, name: str, petals: int, price: float):
        self.name = name
        self.petals = petals
        self.price = price

    def setName(self, name):
        self.name = name

    def setPetals(self, P):
        self.petals = P

    def setprice(self, pr):
        self.price = pr

    def getName(self) -> str:
        return self.name

    def getPetals(self):
        return self.petals

    def getprice(self):
        return self.price

f = Flower("f1", 10, 250)
f.setprice(400)
print(f.getprice())
