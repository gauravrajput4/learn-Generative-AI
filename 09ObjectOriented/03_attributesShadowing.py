class Chai:
    temperature='hot'
    strength='strong'

cutting=Chai()
print(cutting.temperature)
cutting.temperature='Mild'
cutting.cup="small"
print("After changing: ",cutting.temperature)
print("cup size ",cutting.cup)
print("Direct look into the class ",Chai.temperature)

del cutting.temperature
print("After changing: ",cutting.temperature)
del cutting.cup
print("After changing: ",cutting.cup)