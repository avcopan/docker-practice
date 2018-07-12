import numpy
import scipy.linalg


A = numpy.random.random((10, 100))
H = numpy.matmul(A, A.T)
h = scipy.linalg.eigvalsh(H)
print(h)
