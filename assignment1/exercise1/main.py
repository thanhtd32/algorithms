def Euclid(a, b):
    if b==0:
        return a
    return Euclid(b, a % b)
gcd=Euclid(25,15)
print(gcd)
