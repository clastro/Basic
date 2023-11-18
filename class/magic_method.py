class Vector(object):

    def __init__(self, *arg):
        '''
        Create a vector, example : v = Vector(5, 10)
        '''

        if len(arg) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = arg

    def __repr__(self):
        ''' Return the vector informations.'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        ''' Return the vector add of self and other '''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        return Vector(self._x * other._x, self._y * other._y)

    def __bool__(self):
        return bool(max(self._x, self._y))

### v1 = Vector(5, 2)
