# You save memory
# You don't want the results immediately lazy evaluation

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Elaichi Chai"

stall=serve_chai()

for x in stall:
    print(x)

def get_chai_list():
    return ['Cup 1', 'Cup 2','Cup 3']

# Generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai=get_chai_gen()
print(chai) # it returns the reference
print(next(chai))
print(next(chai))
print(next(chai))