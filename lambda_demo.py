


""" def example_method(n):
    return lambda a: a * n

doubler = example_method(2)

print(doubler(3))

def add_method():
    return lambda a: a + 10

adding = add_method()

print(adding(4))

x = lambda a, b: a / b
print(x(23, 22)) """


def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))