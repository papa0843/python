import numpy as np

np.random.seed(0)
x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))

print("x3 ndim : ", x3.ndim)
print("x3 shape : ", x3.shape)
print("x3 size : ", x3.size)
print("x3 dtype : ", x3.dtype)
print("itemsize : ", x3.itemsize, "byte")
print("nbytes : ", x3.nbytes, "bytes")
print("x1 :", x1)
print("x2 :", x2)
print("x3 :", x3)

x = np.arange(10)
print("x : ", x)
print("x[:5]", x[:5])
print("x[5:]", x[5:])
print("x[4:7]", x[4:7])
print("x[::2]", x[::2])
print("x[1::2]", x[1::2])
print("x[::-1]", x[::-1])
print("x[5::-2]", x[5::-2])

print("x2 :", x2)
print("x2[:2, :3] :", x2[:2, :3])
print("x2[:3, ::2] :", x2[:3, ::2])
print("x2[::-1, ::-1] :", x2[::-1, ::-1])

print("x2 :",x2)
x2_sub = x2[:2, :2]
print("x2_sub :",x2_sub)
x2_sub[0,0]=99
print("x2_sub :",x2_sub)
print("x2 :",x2)