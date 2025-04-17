class Solution:
    def printPat(self, n):
        #write code here
        result=[]
        for i in range(n,0,-1):
            for j in range(n,0,-1):
                result.extend([j]*i)
            result.append(-1)
        return result

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        sol = Solution()
        ans = sol.printPat(n)

        # Print the result list with -1 as a separator
        for num in ans:
            print(num, end=" ")
        print()

# } Driver Code Ends