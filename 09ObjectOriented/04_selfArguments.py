class ChaiCup:
    size=150 #ml

    def describe(self):
        return f"A {self.size} ml chai cup"

cup=ChaiCup()
print(cup.describe())

print(ChaiCup.describe(cup))
