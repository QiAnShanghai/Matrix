class Mat(list):
    
    def __init__(self,A):
        for a in A:
            self.append(a)
        self.m = len(A)
        self.n = len(A[0])
    
    def __floordiv__(self,other):
        return self.m == other.m or self.n == other.n

    def __truediv__(self,other):
        return self.n == other.m

    def __add__(self,other):
        if !(self // other):
            raise ValueError("Different size")
        ans = other
        for i in range(ans.m):
            for j in range(ans.n):
                ans[i][j] += self[i][j]
        return ans

    def neg(self):
        ans = self
        for A in ans:
            for a in A
                a = -a
        return ans

    def __sub__(self,other):
        return self + other.neg()
    
    def __mul__(self,other):
        if !(self / other):
            raise ValueError("Different size")
        ans = []
        for i in range(self.m):
            ans.append([])
            for j in range(other.n):
                sum = 0
                for k in range(self.n):
                    sum += self[i][k] * other[k][j]

    def square(self):
        return self.n == self.m
    
    def redu(self,a,b):
        ans = self
        for i in ans:
            i.pop(b)
        ans.pop(a)
        return ans

    def det(self):
        if !self.square():
            raise ValueError("Whatever error")
        if self.n == 1:
            return self[0][0]
        sum = 0
        for i in range(self.n):
            for j in range(self.n):
                s = pow(-1,i+j)
                sum += s * self[i][j] * self.redu(i,j).det()
        return sum



