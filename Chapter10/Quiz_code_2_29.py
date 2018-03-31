# Problem 5.a
def gcd(denominator1, denominator2):
    x1 = abs(min(denominator1, denominator2))
    y1 = abs(max(denominator1, denominator2))
    gcd_ = x1

    if y1 % x1:
        gcd_ = gcd(x1, y1 % x1)
    return gcd_

print(gcd(5,10))

def fracAdd(frac1, frac2):
    a = frac1[0]
    b = frac2[1]
    c = frac2[0]
    d = frac2[1]
    numerator = a*d + b*c
    denominator = c*d
    g = gcd(numerator, denominator)
    return (numerator/g, denominator/g)

fraction1 = (1,5)
fraction2 = (1,5)
print(fracAdd(fraction1, fraction2))

def addFractions(a_fraction, b_fraction):
    denominator1 = a_fraction[1]
    denominator2 = b_fraction[1]
    numerator1 = a_fraction[0]
    numerator2 = b_fraction[0]

    _gcd = gcd(denominator1, denominator2)
    print(_gcd, "GCD")
    if numerator1 % _gcd != 0 or numerator2 % _gcd != 0:
        denominator1 = denominator1 * _gcd
        print(denominator1, "IF")
        denominator2 = denominator2 * _gcd
        print(denominator2, "D2")
        numerator1 = numerator1 * _gcd
        numerator2 = numerator2 * _gcd
        print(numerator2, "N")
        print(numerator1, "N1")
    else:
        numerator1 = numerator1 % _gcd
        print(numerator1, "N")
        numerator2 = numerator2 % _gcd
        denominator1 = denominator1 % _gcd
        print(denominator1, "D")
        denominator2 = denominator2 % _gcd

    if denominator1 == denominator2:
        added_num = numerator1 + numerator2

    return (added_num, added_denom)

#print(addFractions((1,5),(5,10))) DOESNT WORK
import fractions
def addFractions(frac1, frac2):
    x1, y1 = frac1[0], frac1[1]
    x2, y2 = frac2[0], frac2[1]
    print(fractions.Fraction(x1, y1) + fractions.Fraction(x2, y2))



# Problem 6.
list1 = [i for i in range(1,10)]
list2 = [100,200]

def transform(list1,list2,r1,r2):
    transform_list = list1[r1:r2]
    for i in range(len(transform_list)):
        insert = transform_list.pop(-1)
        list2.append(insert)
    return list2

print(transform(list1,list2,4,7))