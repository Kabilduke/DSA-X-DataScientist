import numpy as np

Given two sparse matrices A and B, return the result of A * B. You can assume that A(s) number of columns is equal to B(s) number of rows.
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Solution:

a = np.array(A)
b = np.array(b)

result = np.dot(a, b)

==> [[ 7  0  0]
     [-7  0  3]]
