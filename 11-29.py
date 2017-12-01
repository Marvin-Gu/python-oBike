"""
字符串操作
"""
name = "xiaoming"
address = "china"
age = 18 
money = 100.1021

print("name","address")

print("name"+" "+"address")
print(name * 2)
#作业 修改下面语句 能够打印出来 my name is xiaoming, i live in china.i am 18 years old,
i have 100.1021 money
print("my name is %s, i live in %s. i am %d years old, i have %d money "%(name,address,age,money))
# 答案
print("my name is %s, i live in %s. i am %d years old, i have %f money "%(name,address,age,money))

