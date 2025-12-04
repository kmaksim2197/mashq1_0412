m1 = lambda lst: list(map(lambda x: x*x, lst))

m2 = lambda a, b: list(map(lambda x, y: x+y, a, b))

m3 = lambda lst: list(map(lambda x: x.upper(), lst))

f1 = lambda lst: list(filter(lambda x: x%2==0, lst))

f2 = lambda lst: list(filter(lambda x: len(x) > 5, lst))

f3 = lambda lst: list(filter(lambda x: x % 3 == 0, lst))

m4 = lambda lst: list(map(lambda x: (x*2 if x*2<10 else (x*2)%10), lst))

m5 = lambda lst: list(map(lambda x: x.capitalize(), lst))

m6 = lambda a, b: list(map(lambda x, y: x+y, a, b))

f3b = lambda lst: list(filter(lambda x: x[0].isdigit(), lst))

m7 = lambda lst: list(map(lambda x: x*2, lst))

f4 = lambda lst: list(filter(lambda x: x%2!=0, lst))

mix = lambda lst: list(map(lambda x: x*x, filter(lambda y: y%2!=0, lst)))

f5 = lambda lst: list(filter(lambda x: not x.startswith("a"), lst))

m8 = lambda lst: list(map(lambda x: ((x**3)%2 if (x**3)%2!=0 else 2), lst))
