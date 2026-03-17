class ChaiOrder:
    def __init__(self,type_,size ):
        self.type=type_
        self.size=size

    def summary(self):
        return f" {self.type} {self.size} ml chai"


order=ChaiOrder("Masala Chai",100)
print(order.summary())
