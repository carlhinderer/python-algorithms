def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, top, bottom):
        if bottom == 0:
            raise ZeroDivisionError
        cmmn = gcd(top, bottom)
        self.num = top // cmmn
        self.den = bottom // cmmn

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def  __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den
