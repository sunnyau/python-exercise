class board:
    matrix = []
    def __init__(self,stringWith81Chars):
        self.stringWith81Chars = stringWith81Chars

    def assign_to_matrix(self):
        row = 0
        col = 0
        for element in self.stringWith81Chars:
            if col == 0:
                self.matrix.append([])
            self.matrix[row].append(element)
            col += 1
            if col == 9:
                col = 0
                row += 1

    def print_matrix(self):
        for line in self.matrix:
            print(line)

    def getStartRange(self, rowOrCol):
        if rowOrCol <= 2:
            return 0
        elif rowOrCol <= 5:
            return 3
        else:
            return 6

    def getEndRange(self, rowOrCol):
        if rowOrCol <= 2:
            return 3
        elif rowOrCol <= 5:
            return 6
        else:
            return 9


    def removeFromRow(self,default_number,row):
        for col in range(9):
            if self.matrix[row][col] in default_number:
                default_number.remove(self.matrix[row][col])

    def removeFromCol(self,default_number,col):
        for row in range(9):
            if self.matrix[row][col] in default_number:
                default_number.remove(self.matrix[row][col])

    def removeFromBlock(self,default_number,row,col):
        for i in range(self.getStartRange(row), self.getEndRange(row)):
            for j in range(self.getStartRange(col), self.getEndRange(col)):
                if self.matrix[i][j] in default_number:
                    default_number.remove(self.matrix[i][j])


    def solver(self):
        for row in range(9):
            for col in range(9):
                default_number = ['1','2','3','4','5','6','7','8','9']
                if self.matrix[row][col] == ".":
                    self.removeFromRow(default_number, row)
                    self.removeFromCol(default_number, col)
                    self.removeFromBlock(default_number,row,col)
                    if len(default_number) == 1:
                        self.matrix[row][col] = default_number[0]


# main

b = board("53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79")
b.assign_to_matrix()
b.print_matrix()
# blute force method. Not very good
for i in range(100):
    b.solver()
print("------------------------------------------")
b.print_matrix()

