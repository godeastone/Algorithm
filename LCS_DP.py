def LCS_dp(X, Y, m, n):

    table = []

    for i in range(0, m+1):
        line = []
        for j in range(0, n+1):
            line.append(0)
        table.append(line)

    for i in range(0, m):
        for j in range(0, n):
            if X[i] == Y[j]:
                table[i][j] = table[i-1][j-1] + 1
            elif table[i-1][j] >= table[i][j-1]:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i][j-1]

    return table

X = ["A", "B", "C", "D", "E", "F"]
Y = ["G", "B", "C", "D", "F", "E"]
result = LCS_dp(X, Y, len(X), len(Y))




