class OutOfIngredientsError(Exception):
    pass

def milk_chai(milk,sugar):
    if milk ==0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print(f"Milk {milk} sugar {sugar} chai is ready...")

milk_chai(5,0)