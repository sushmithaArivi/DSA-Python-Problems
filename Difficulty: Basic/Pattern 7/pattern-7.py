#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            space=" " * (N-i)
            stars='*'*(2*i-1)
            print(space+stars)
       