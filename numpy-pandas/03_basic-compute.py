import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)

print(a, b)

c = a - b
print(c)

d = b ** 2
print(d)

e = 10 * np.sin(a)  # sin cos tan
print(e)

print(b)
print(b < 3)
print(b > 2)
print(b == 3)

f = np.array([[1, 1],
              [0, 1]])
g = np.arange(4).reshape((2,2))

print(f)
print(g)

print(f*g)      # 单个的乘法
print(np.dot(f,g))   #矩阵运算
print(f.dot(g))   #和上边一样，只是写法不同 矩阵运算



h = np.random.random((2,4))
print(h)  #每次结果都不一样

print(np.sum(h))
print(np.sum(h, axis=0))
print(np.sum(h, axis=1))

print(np.min(h))
print(np.min(h, axis=0))
print(np.min(h, axis=1))

print(np.max(h))
print(np.max(h, axis=0))
print(np.max(h, axis=1))




