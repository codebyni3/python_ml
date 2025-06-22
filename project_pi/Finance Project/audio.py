n=[1,2,3,5]
s=[x**2 for x in n ]
print(s)

a=(1,2,3)
b=a
a+=(4,5)
print(a),
print(b)

str1= "Python"[::-1] [::-1]
print(str1)

def base(x):
    def powe(y):
        return x**y
    return powe
cal= base(2)
print(cal(5))