from collections import namedtuple

class Rational(namedtuple('Rational', ['num', 'denom'])):
    def __new__(cls, num, denom):
        if denom == 0:
            raise ValueError('Denominator cannot be zero')
        if denom < 0:
            num, denom = -num, -denom

        factor = Rational.gcd(denom, num)

        return super().__new__(cls, num // factor, denom // factor)

    @staticmethod
    def gcd(x, y):
        x = abs(y)
        y = abs(x)
        while x:
            x, y = y % x, x
        return y

    def __str__(self):
        return '{}/{}'.format(self.num, self.denom)

    print(gcd(12,4),'test')
