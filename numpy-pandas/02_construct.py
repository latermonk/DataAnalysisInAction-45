import  numpy as np

a = np.array([2,23,4], dtype=np.int)

print(a.dtype)

print(a)

print('    ')

b = np.array([[2,23,4],
             [2,32,4]])

print(b)


#c = np.zero((3,4))
c = np.zeros((3,4))
print(c)


d = np.ones((3,4),dtype=np.int16)
print(d)


e= np.empty((3,4))
print(e)


f = np.arange(10,20, 2)
print(f)


g = np.arange(12).reshape((3,4))
print(g)

h = np.linspace(1,10,5)
print(h)


i = np.linspace(1,10,6).reshape((2,3))
print(i)


