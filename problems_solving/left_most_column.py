"""
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.
Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:
BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  
"""
# """
# This is BinaryMatrix's API interface.
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

def leftMostColumnWithOne(binaryMatrix):
    """
    :type binaryMatrix: BinaryMatrix
    :rtype: int
    """
    left_most = float('inf')
    x,y = binaryMatrix.dimensions()
    if (x==y==0): return -1
    j = y - 1
    i = x - 1
    while i in range(x):
        while j >= 0 and binaryMatrix.get(i,j) == 1:
            left_most = min(left_most,j)
            j -= 1
        i -= 1
    return left_most if left_most < 100 else -1