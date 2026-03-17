# Features                @classmethod                    @staticmethod
# First parameter     Receives cls (the class itself)     Receives no automatic first argument
# use case            operate on the class, not instance  utility function related to the class
# Access to cls       Yes                                 No
# Access to self      No                                  No

class ChaiOrder:
    def __init__(self, tea_type, sweetness,size):
        self.tea_type = tea_type
        self.sweetness=sweetness
        self.size=size

    @classmethod
    def from_dict(cls,orderData):
        return cls(
            orderData['tea_type'],
            orderData['sweetness'],
            orderData['size']
        )
    @classmethod
    def from_string(cls,orderString):
        tea_type,sweetness,size=orderString.split('-')
        return cls(
            tea_type,
            sweetness,
            size
        )

class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size.lower() in ['small', 'edium', 'large']


print(ChaiUtils.is_valid_size('small'))
order1= ChaiOrder.from_dict({"tea_type":"Masala Chai","sweetness":"Medium","size":"Large"})
order2=ChaiOrder.from_string("Ginger-Low-Small")

print(order1.__dict__)
print(order2.__dict__)