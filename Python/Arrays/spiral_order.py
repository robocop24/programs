class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        m, n = len(A), len(A[0])
        T, B, L, R = 0, m-1, 0, n-1
        d = 0
        result  = []
        while T <= B and L <= R:
            if d == 0:
                for i in range(L, R+1):
                    result.append(A[T][i])
                T += 1
            elif d == 1:
                for i in range(T, B+1):
                    result.append(A[i][R])
                R -= 1
            elif d == 2:
                for i in range(R, L-1, -1):
                    result.append(A[B][i])
                B -= 1
            elif d == 3:
                for i in range(B, T-1, -1):
                    result.append(A[i][L])
                L += 1
            d = (d+1) % 4
            #print(d, T, B, L, R)
        return result
if __name__ == "__main__":
    ob = Solution()
    print(ob.spiralOrder([ [1,2,3], [4,5,6], [7,8,9] ]))