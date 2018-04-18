class Matrix:
    def __init__(self, columns, rows):
        self.my_matrix = []
        for i in range(rows * columns):
            self.my_matrix.append(0)
        self.columns = columns
        self.rows = rows
    def locate(self, column, row):
        try:
            return self.my_matrix[(column*self.rows) + row]
        except IndexError:
            print("Unknown")
            return 0 
    def shove(self, column, row, number):
        try:
            self.my_matrix[(column * self.rows) + row] = number 
            print("Updated")
        except IndexError:
            print("Bad location")
    def printAll(self):
         for i in range(len(self.my_matrix)):
            if i == self.rows:
                print("")
            print(self.my_matrix[i])


m = Matrix(5,5)
m.shove(3,3,1)
m.printAll()
            
