class A:
    label="A: Base class"

class B(A):
    label="B: Masala Blend"

class C(A):
    label="C: Herbal blend"

class D(B,C):
    pass

cup =D()
print(D.__mro__)
print(cup.label)