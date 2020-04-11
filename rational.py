from collections import namedtuple


class Rational(namedtuple('Rational', ['num', 'denom'])):

    def __new__(cls, num, denom):
        if denom ==0:
            raise ValueError('Denom cannot be null')
        if denom < 0:
            num, denom = -num, -denom
        return super().__new__(cls,num,denom)

    def __str__(self):
        return '{}/{}'.format(self.num, self.denom)
