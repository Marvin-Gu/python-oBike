a = "helloworld"
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
print("===============================================================")

b = "0123456789"
print(a[1:5])
print(a[:])
print(a[5:-2])
print(a[5::-2])
print(a[4::-2])
print(a[4::2])
print("===============================================================")

x = [1,3,5]
y = [2,4,6]

a = "hello"
b = "world"
c = 1
print(a+b)

print(x+y)
print("===============================================================")


a = [1,3,5]
b = [2,4,6]
c = 7
x = "hello"
print(a*c)
print(c*x)
print("===============================================================")


a = [1,2,3,4,5,6,7,8,9]
b = "greeting"
print(1 in a)
print(10 in a)

print("get" in b)
print("ting" in b)
print("eet" in b)