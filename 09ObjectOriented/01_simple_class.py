class User:
    pass


class Person:
    pass

print(type(User))

user1 = User()
print(type(user1))
print(type(user1) is User)


print(type(user1) is Person)