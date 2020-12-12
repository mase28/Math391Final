# This is a draft of the Extended Euclidean Algorithm. As of currently, it just
# does the Euclidean Algorithm and saves each step. The next step is to make
# it go in reverse to make it be an Extended Euclidean Algorithm program. 

import sys
import math

class Equation:
    def __init__(self, a, q, b, r):
        self.a = a
        self.q = q
        self.b = b
        self.r = r
    
    def __str__(self):
        return f"{self.a} = {self.q}*{self.b} + ({self.r})"

    def __repr__(self):
        return f"{self.a} = {self.q}*{self.b} + ({self.r})"

class Complex_Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    
    def __simplify(self):
        self.num = self.num * self.den.conjugate()
        self.den = self.den * self.den.conjugate()

    def get_quotient(self):
        self.__simplify()
        a = self.num.real / self.den.real
        b = self.num.imag / self.den.real
        if a - math.floor(a) < .5:
            a = math.floor(a)
        else:
            a = math.ceil(a)
        
        if b - math.floor(b) < .5:
            b = math.floor(b)
        else:
            b = math.ceil(b)
        return complex(a, b)

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"{self.num}/{self.den}"

def euclidean_int(a,b):
    ret = []
    r = 1
    if abs(b) > abs(a):
        temp = b
        b = a
        a = temp

    while r != 0:
        q = a // b
        r = a % b
        equation = Equation(a, q, b, r)
        ret.append(equation)
        a = b
        b = r

    return ret

def euclidean_gaus(a, b):
    ret = []
    r = 1
    if abs(b) > abs(a):
        temp = b
        b = a
        a = temp
    
    while r != 0:
        frac = Complex_Fraction(a, b)
        q = frac.get_quotient()
        r = a - b*q
        equation = Equation(a, q, b, r)
        ret.append(equation)
        a = b
        b = r

    return ret

def bezout(ls):
    u = 1
    v = -ls[len(ls)-2].q
    for i in range(len(ls)-2, 0, -1):
        u += v * (-ls[i-1].q)

        temp = u
        u = v
        v = temp
    return u, v
        
 