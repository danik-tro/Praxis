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