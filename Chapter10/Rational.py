# To build Rational Numbers
def gcd(x, y):
    x1 = abs(min(x, y))
    y1 = abs(max(x, y))
    gcd_ = x1

    if y1 % x1:
        gcd_ = gcd(x1, y1 % x1)
    return gcd_



class Rational(object):
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int):
            raise Exception("Numerator must be an integer.")
        elif not isinstance(denominator, int) or denominator == 0:
            raise Exception("Denominator must be a non-zero integer.")

        self.num = numerator
        self.den = denominator

    def __repr__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return "{0}/{1}".format(self.num, self.den)

    def _cleanup(self):
        """Manage negative symbols."""
        if self.num < 0 and self.den < 0:
            self.num = abs(self.num)
            self.den = abs(self.den)
        elif self.num > 0 and self.den < 0:
            self.num = -self.num
            self.den = abs(self.den)


    # Unary Operation
    def reciprocal(self):   # mutable
        temp = self.num
        self.num = self.den
        self.den = temp

    def reduce(self):
        g = gcd(self.num, self.den)
        self.num = self.num // g
        self.den = self.den // g

    def _add(self, a_rational):
        a = self.num
        b = self.den
        c = a_rational.num
        d = a_rational.den
        new_rational = Rational(a*d + b*c, b*d)
        new_rational.reduce()
        return new_rational

    def __add__(self, other):
        return self._add(other)



if __name__ == "__main__":
    rat1 = Rational(3, 7)
    print(rat1)

    # Potential Errors
    # rat2 = Rational(1,3.5)
    # rat2 = Rational(1, 0)
    # rat2 = Rational(1.5,"dog")

    rat3 = Rational(19,-20)
    print(rat3)
    rat3._cleanup()
    print(rat3)

    rat1.reciprocal()
    print(rat1)

    rat4 = Rational(35, 15)
    print(rat4)
    rat4.reduce()
    print(rat4)

    rat5 = Rational(40, 12)
    rat5.reduce()
    rat5.reciprocal()
    print(rat5)

    rat6 = Rational(4,2)
    rat6.reduce()
    print(rat6)
    # exercise how do we manage a / 1 rationals so they are integers

    print(rat1, rat3)
    rat7 = rat1 + rat3
    print(rat7)
