def _str_(x,y):
    if x == 7:
        raise ValueError('hey - x is 7!')
    return '{}/{}'.format(x, y)

def _new_(cls, num, denom):
    return super().__new__(cls, num, denom)

value = _str_(4,4)
print(value)
print(type(value))
