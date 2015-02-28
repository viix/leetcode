#!/usr/bin/python

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        cur = m - 1
        for i in range (0, n):
            while cur >= 0 and A[cur] >= B[n-1-i]:
                A[cur+n-i] = A[cur]
                cur -= 1;
            A[cur+n-i] = B[n-i-1]
