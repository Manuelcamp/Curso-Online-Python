#Yield From
def gen1():
    yield 1
    yield 2
    yield 3
    yield 4

def gen2(gen):
    yield from gen()
    yield 5
    yield 6
    yield 7

def gen3():
    yield 10
    yield 20
    yield 30
    yield 40

# def gen2():
#     yield from gen1()
#     yield 5
#     yield 6
#     yield 7

g = gen2(gen1)
g2 = gen2(gen3)

for numero in g:
    print(numero)
for numero in g2:
    print(numero)