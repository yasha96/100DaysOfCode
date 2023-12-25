
#GeekforGeeks problem of the day 25Dec

class Solution:
    # Function for finding determinant of matrix.
    def determinantOfMatrix(self, matrix, n):
        # Base case: If the matrix is 1x1, return its single element as determinant
        if n == 1:
            return matrix[0][0]

        det = 0  # Initialize determinant value

        # Calculate the determinant using cofactor expansion
        for col in range(n):
            # Calculate the cofactor for the current element (first row, col)
            sign = (-1) ** col  # Alternate sign for cofactors
            cofactor = matrix[0][col]
            sub_matrix = []

            # Create the sub-matrix excluding the first row and current column
            for i in range(1, n):
                sub_row = []
                for j in range(n):
                    if j != col:
                        sub_row.append(matrix[i][j])
                sub_matrix.append(sub_row)

            # Recursively calculate the determinant of the sub-matrix using self.determinantOfMatrix()
            det += sign * cofactor * self.determinantOfMatrix(sub_matrix, n - 1)

        return det


# Driver code from geekforgeeks
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends
