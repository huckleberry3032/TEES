WEIGHTS = {"match":2, "mismatch":-1, "gap":-1}

def getScore(matrix, x, y, stringA, stringB, weights):
    similarity = weights["match"] if (stringA[x-1] == stringB[y - 1]) else weights["mismatch"]
    
    scoreDiagonal = matrix[x - 1][y - 1] + similarity
    scoreUp   = matrix[x - 1][y] + weights["gap"]
    scoreLeft = matrix[x][y - 1] + weights["gap"]
    return max(0, scoreDiagonal, scoreUp, scoreLeft)

def initMatrix(stringA, stringB, weights):
    matrix = [[None] * (len(stringB) + 1) for i in range(len(stringA) + 1)]
    matrix[0][0] = 0
    weight = -1
    for i in range(1, len(stringB) + 1):
        matrix[0][i] = weight
        weight -= 1
    weight = -1
    for i in range(1, len(stringB) + 1):
        matrix[i][0] = weight
        weight -= 1
    for i in range(1, len(stringA) + 1):
        for j in range(1, len(stringB) + 1):
            matrix[i][j] = getScore(matrix, i, j, stringA, stringB, weights)
    return matrix

def printMatrix(matrix):
    for row in matrix:
        print row

if __name__=="__main__":
    from optparse import OptionParser
    optparser = OptionParser(description="")
    optparser.add_option("-a", default=None, help="")
    optparser.add_option("-b", default=None, help="")
    (options, args) = optparser.parse_args()
    
    matrix = initMatrix(options.a, options.b, WEIGHTS)
    printMatrix(matrix)