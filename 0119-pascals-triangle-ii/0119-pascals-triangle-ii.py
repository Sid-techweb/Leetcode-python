class Solution:
    def getRow(self, rowIndex):
        row = [1]

        for i in range(rowIndex):
            new = [1] * (len(row) + 1)

            for j in range(1, len(row)):
                new[j] = row[j - 1] + row[j]

            row = new

        return row