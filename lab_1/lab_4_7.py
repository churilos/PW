class Row:
    def __init__(self, row_id, collection, value):
        self.id = row_id
        self.collection = collection
        self.value = value

class Table:
    def __init__(self, rowsNum):
        self.rows = []
        self.rowsNum = rowsNum

    def addRow(self, row):
        if any(r.id == row.id for r in self.rows):
            raise ValueError("Row with id {} already exists".format(row.id))
        self.rows.append(row)

    def setRow(self, row):
        for i, r in enumerate(self.rows):
            if r.id == row.id:
                self.rows[i] = row
                return
        raise ValueError("Row with id {} does not exist".format(row.id))

    def getRow(self, rowId):
        for r in self.rows:
            if r.id == rowId:
                return r
        raise ValueError("Row with id {} does not exist".format(rowId))

    def display(self):
        print("id | x1 | x2 | f(x1,x2)")
        for row in self.rows:
            print("{} | {} | {} | {}".format(row.id, row.collection[0], row.collection[1], row.value))

class LogicFunction:
    def __init__(self, variablesNum, table):
        self.variablesNum = variablesNum
        self.table = table

    def getExpression(self):
        # Implement the calculation of the minimal formula for the logical function here
        # ...
        pass

    def getTable(self):
        return self.table

    def printTable(self):
        self.table.display()

table = Table(4)
table.addRow(Row(1, [0, 0], 1))
table.addRow(Row(2, [0, 1], 0))
table.addRow(Row(3, [1, 0], 0))
table.addRow(Row(4, [1, 1], 1))

logic_function = LogicFunction(2, table)
logic_function.printTable()
