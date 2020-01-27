import numpy as np

A = np.arange(2, 14).reshape((3, 4))

print(A)

B = np.argmin(A)
print(B)

C = np.argmax(A)
print(C)

D = np.mean(A)
print(D)
print(A.mean())

print(np.average(A))
# print(A.average())  not suitable


print(np.median(A))


print(A)
print(np.cumsum(A))


print(np.nonzero(A))  #output the position of the element

print(np.sort(A))


E = np.arange(14,2,-1).reshape((3,4))
print(E)
print(np.sort(A))
print(np.transpose(A))
print(A.T)


print((A.T).dot(A))


print(np.clip(A,5,9)) # 大于小于5的变成5/9

print(np.mean(A,axis=0)) #对列进行计算
print(np.mean(A,axis=1))







