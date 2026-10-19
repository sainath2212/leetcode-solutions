class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        arr = [[-1]*n for i in range(n)]
        l, r, t, b = 0, n-1, 0, n-1
        def fill_matrix(l, r, t, b, k):
            for i in range(l, r+1):
                if(arr[t][i]==-1):
                    arr[t][i] = k[0] 
                k[0]+=1 
            for i in range(t+1, b+1):
                if(arr[i][r]==-1):
                    arr[i][r] = k[0]
                k[0]+=1
            if n!=1:
                for i in range(r-1, l-1, -1):
                    if(arr[b][i]==-1):
                        arr[b][i] = k[0] 
                    k[0]+=1
            if n!=1:
                for i in range(b-1, t, -1):
                    if(arr[i][l]==-1):
                        arr[i][l] = k[0] 
                    k[0]+=1 
        k = [1]
        while l<=r and t<=b:
            fill_matrix(l, r, t, b, k)
            l+=1 
            r-=1
            t+=1
            b-=1 
        return arr

        