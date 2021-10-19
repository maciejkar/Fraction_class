import math

class Fraction():
    """Class which represent fractions """

    mixed = False
    allow_float = True
    float_precision = 4

    def __init__(self, num, den) :
        """Function creat and reduse fractions
        @parm num: (int) numerator
        @parm den: (int) denominator"""
        
        # Change float to ratio whe is allowed
        if self.allow_float == True and type(num) in (float, int) and type(den) in (float, int):
            num = math.floor(num * 10 ** self.float_precision)
            den = math.floor(den * 10 ** self.float_precision)
            
            while num % 10 == 0 and den % 10 == 0:
                num = num // 10
                den = den // 10


        if type(num) == int and type(den) == int:
            if den == 0 :
                raise ValueError("Denominator can't be 0")
            if den * num > 0:
                self.num = abs(num)
                self.den = abs(den)
            else :
                self.num = -abs(num)
                self.den = abs(den)
            
            # redusing fraction   
            n = 2
            while n <= min(abs(self.num), abs(self.den)):
                if self.num % n == 0 and self.den % n == 0:
                    self.num = self.num // n
                    self.den = self.den // n 
                else :
                    n += 1
        else :    
            raise ValueError("Numerator and denominator must be intiger ")

    def get_num(self):
        """Method return numerator"""
        return self.num

    def get_den(self):
        """Method return denominator"""
        return self.den

    def __float__(self):
        return self.num / self.den

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        if self.mixed == True:
            return str(self.num // self.den) + " and " + str(self.num % self.den) + "/" + str(self.den)
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)

        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)

    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
            
        return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)

    def __mul__(self,other):
        if type(other) != Fraction:
            return other * self
        return Fraction(self.num * other.num , self.den * other.den)

    def __rmul__(self, scalar):
        return Fraction(self.num * scalar, self.den)
    
    def __truediv__(self, other):
        if type(other) != Fraction:
            return Fraction(self.num, self.den * other)

        return Fraction(self.num * other.den , self.den * other.num)

    def __pow__(self, power):
        if type(power) != int:
            power = float(power)
        return Fraction(math.pow(self.num, power), math.pow(self.den, power))
     
            
    def __lt__(self, other):
        if type(other) != Fraction:
            if float(self) < other :
                 return True
            else:
                return False

        if self.num / self.den < other.num / other.den :
            return True
        else:
            return False

    def __gt__(self, other):
        return not self < other

    def __eq__(self, other):
        if type(other) != Fraction:
            if math.isclose(float(self) , other) :
                 return True
            else:
                return False

        if self.num == other.num and self.den == other.den:
            return True
        else:
            return False
    
    def __le__(self, other):
        if self.__lt__(other)  or self.__eq__(other):
            return True
        else:
            return False
    
    def __ge__(self, other):
        return  self > other or self == other

if __name__ == "__main__":
    f1=Fraction(1,3)
    print(f1)
    f2=Fraction(2,4)
    print(f1*f2)
    print(f1+f2)
    print(f1-f2)
    print(f1/f2)
    f4=Fraction(4,8)
    # f3= Fraction(0,1)
    # print(f1/f3)
    print(f2==f4)
    print(f1<=f2)
    f5=Fraction(1,-3)
    print(f5)
    f6=Fraction(-1,3)
    print(f6)
    f7=Fraction(-1,-3)
    print(f7)
    f8=Fraction(-7,-1)
    print(f8)

    g1=Fraction(5,2)
    g2=Fraction(3, 1)
    print(g2)
    print(float(g1))
    print(3*g1)
    print(g1*5)
    print(g1+g2)
    print(g1+2)
    print(1+g1)
    print(g1)
    Fraction.mixed = True
    print(g1)
    print(g1+g2)
    print(g1>g2)
    print(g1>=g2)
    print(g1<=g2)
    print(g1>3)
    print(g1>2.2)
    print(g1==2.5)
    print(g2 != 3)
    print(g2>=3)
    print(g2/-2)
    Fraction.mixed = False
    print(f6> g1)
    g3=Fraction(1.5 ,3)
    print(g3)
    print(g1 + 2.4)
    print(g3 ** 2)
    print(g3 ** g3)
    print(g3 - 1)
