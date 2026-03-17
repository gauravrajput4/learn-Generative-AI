# Sends value to 07Generators

def chai_customer():
    print("Welcome ! What chai would you like to do?")
    order=yield
    while True:
        print(f"Preparing to get {order}")
        order = yield

stall=chai_customer()
next(stall) # start the generator
# stall.send("Masala chai")
# stall.send("Lemon chai")