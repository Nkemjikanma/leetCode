class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        row_col = row * col
        i = 0
        l = []
        new_mat = []

        if row_col == (r * c):

            for row in mat:
                for elem in row:
                    l.append(elem)
                    i+=1
                    if i == c:
                        new_mat.append(l)
                        l = []
                        i = 0
            return new_mat

        else:
            return mat  


        
        