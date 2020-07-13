zoo = ('Monkey', 'Lion', 'Owl', 'Dolphin', 'Snake', 'Turtle', 'Raven', 'Deer', 'Elk', 'Bear')
print(zoo.index('Owl'))

if 'Bear' in zoo:
    print('Animal found')

foo = list(zoo)
foo.extend(['Meercat', 'Horse', 'Camel'])
zoo = tuple(foo)