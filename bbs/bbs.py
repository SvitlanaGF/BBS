from random import randint
from math import gcd


class BBS:
    def __init__(self,p=0,q=0):
        self.p = self.generate_number() if p == 0 else p
        self.q = self.generate_number() if q == 0 else q
        self.__n = self.q * self.p
        self.__r = self.r()

    def r(self):
        while True:
            r = randint(9, self.__n)
            if gcd(self.__n, r) == 1:
                return r

    @staticmethod
    def is_prime(num: int):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def generate_number():
        while True:
            n = randint(90000, 1000000)
            if n % 4 == 3 and BBS.is_prime(n):
                return n

    def generate_list_of_numbers(self, s):
        while True:
            s = s ** 2 % self.__n
            yield int(s)

    def encrypt(self, text):
        bbs = self.generate_list_of_numbers(self.__r)
        return ' '.join([str(ord(c) ^ next(bbs)) for c in text])

    def decrypt(self, txt):
        bbs = self.generate_list_of_numbers(self.__r)
        lst = txt.split()
        return ''.join([chr(int(i) ^ next(bbs)) for i in lst])



