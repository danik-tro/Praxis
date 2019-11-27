def colods_of_card():
    import collections
    Card = collections.namedtuple('Card', ['rank','suit'])

    class FrenchDeck:
        ranks = [str(n) for n in range(2, 11) ] + list('JQKA')
        suits = 'spades diamonds clubs hearts'.split()

        def __init__(self):
            self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

        def __len__(self):
            return len(self._cards)

        def __getitem__(self, position):
            return self._cards[position]
    deck = FrenchDeck()
    print(len(deck))

    from random import choice
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))

    print(deck[:13])
    print(deck[12::13])

    for card in deck:
        print(card)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high):
        print(card)


"""
!value = SequenceMatcher(None, "rainn", "rain").ratio()
!for find defferents with words
!or
!output = get_close_matches("rain", ["help","mate","rainy"], n=1, cutoff = 0.75)
"""

def class_vector():
    from math import hypot

    class Vector:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __repr__(self):
            return 'Vector({}, {})'.format(self.x, self.y)

        def __abs__(self):
            return hypot(self.x, self.y)

        def __bool__(self):
            return bool(abs(self))

        def __add__(self, other):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)
        
        def __mul__(self, scalar):
            return Vector(self.x * scalar, self.y * scalar)

        def __rmul__(self, scalar):
            return Vector(self.x * scalar, self.y * scalar)


    def test_for_vector():
        v = Vector(3,4)
        v_1 = Vector(5,5)

        print(v, v_1)
        print(v + v_1)
        print(abs(v))
        print(abs(v + v_1))
        print(v * 5)
        print(5 * v)

    test_for_vector()
    #43 page of book Fluent Python


def praxis_Calculator():
    import numpy as np
    import functools

    def log(func):
        @functools.wraps(func)
        def wrapper(arg1, arg2):
            print('-'*15)
            print("Result function with name : {}. Result: {}".format(func.__name__ ,func(arg1, arg2)))
            print("Argument1 = {}. Argument2 = {}".format(arg1, arg2))
            print('-'*15)
        return wrapper


    class Calculator:
        def __init__(self):
            pass
        
        @log
        def sum(a, b):
            return a + b

        @log
        def multiply(a, b):
            return a * b

        @log
        def divide(a, b):
            try:
                return a / b
            except ZeroDivisionError:
                return "Second arg is zero!"
        
        @log
        def subtract(a, b):
            return a - b


    def Testing():
        testing = np.random.random(10) * 100 - 50
        for i in range(0, len(testing)-1, 2):
            Calculator.sum(*testing[i:i+2])
            Calculator.multiply(*testing[i:i+2])
            Calculator.subtract(*testing[i:i+2])
            Calculator.divide(*testing[i:i+2])
        Calculator.divide(4, 0)
    Testing()




def learn_Logging():
    import logging

    logging.basicConfig(level = logging.DEBUG)#До первого вызова ошибки
    logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)
    
    logging.debug(u"This is a debug message")
    logging.info(u'This is info message')
    logging.warning(u'This is warning message')
    logging.error(u'This is error message')
    logging.critical(u'Fatal')
    logging.debug(u'This is a debug message')


"""
! New pages of book Fluent Python
! 1.Cartesian product
"""

def cartesian_product():
    import collections
    Card = collections.namedtuple('Card', ['color', 'size'])
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']

    tshirts = [Card(color, size) for color in colors for size in sizes]
    print(tshirts)

    """
    ! Генераторные выражения
    """
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes ):
        print(tshirt)


def tuples():
    import os
    from collections import namedtuple
    _, filename = os.path.split('C:/Users/Daniil Trotsenko/Documents/Educate/ML/Book/Plas_Python-dlya-slozhnyh-zadach.507605.pdf')
    print(_, filename, '\n','-'*100)

    City = namedtuple('City' , 'name country population coordinates')
    LatLong = namedtuple( 'LatLong', 'lat long')

    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(delhi_data) # <=> City( *delhi_data )


    print(delhi)
    print(delhi._asdict())
    print('-'*100)

    for key, value in delhi._asdict().items():
        print(key + ':', value)

def sorting():
    fruits = ['apples', 'banannas', 'orange', 'tomato']
    print( sorted(fruits, key=len) )
    print(sorted(fruits, key=str.lower, reverse=True))

def find_and_sorting():
    import bisect
    import sys

    HATSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
    NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

    ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'

    def demo(bisect_fn):
        for needle in reversed(NEEDLES):
            position = bisect_fn(HATSTACK, needle)
            offset = position * " |"
            print(ROW_FMT.format(needle, position, offset))

    if __name__ == "__main__":
        if sys.argv[-1] == 'left':
            bisect_fn = bisect.bisect_left
        else:
            bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print("haystack ->", ' '.join('%2d' % n for n in HATSTACK))
    demo(bisect_fn)

    def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = bisect.bisect(breakpoints, score)
        return grades[i]

    y = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    print(y)
    #73 page of book fluent python


def sorting_and_insert():
    import bisect
    import random

    SIZE = 7

    random.seed(1729)

    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE*2)
        bisect.insort(my_list, new_item)
        print('%2d -> ' % new_item, my_list)

def arrays():
    from array import array
    from random import random

    floats  = array('d', (random() for i in range(10**7)))
    print(floats[0])

    """
    ! Add to file
    """
    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()

    floats2 = array('d')
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 10**7)
    fp.close()


def memory_view():
    import array
    numbers = array.array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(len(memv), memv[0])

    memv_oct = memv.cast('B')
    print(memv_oct.tolist())
    memv_oct[5] = 4
    print(numbers)


def numpy_and_scipy():
    import numpy as np
    floats = np.loadtxt('some.txt')
    floats *= 0.5 #divide by 0.5

    from time import perf_counter as pc

    t0 = pc(); floats /= 3; print(pc() - t0)
    np.save('floats-10M', floats)
    floats2 = np.load('floats-10M.npy', 'r+')
    floats2 *= 6


def deque_():
    from collections import deque
    dq = deque(range(10), maxlen=10)
    print(dq)
    #dq.rotate(3)
    #print(dq)
    dq.appendleft(-1)
    print(dq)
    dq.extend([11, 22, 33])
    print(dq)
    #90 page of book fluent python
    #string and bytes

def hash_():
    x = (1,2, (30, 40))
    print(hash(x))
    y = (1, 2, [30, 40])

    try:
        print(hash(y))
    except TypeError:
        print('Error,',y,'is not hashable')
    
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict((zip(['one', 'two', 'three'], (1, 2, 3))))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    print(a == b == c == d == e)

def dict_and_miss():

    class StrKeyDict0(dict):

        def __missing__(self, key):
            if isinstance(key, str):
                raise KeyError(key)
            return self[str(key)]
        
        def get(self, key, default=None):
            try:
                return self[key]
            except KeyError:
                return default

        def __contains__(self, key):
            return key in self.keys() or str(key) in self.keys()

    x = StrKeyDict0([(1,'e'), (2,'d')])
    print(x.get(3))
dict_and_miss()





