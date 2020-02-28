# With assistance from Hunter Shiells (Git: HunterShiells) and Warren Phillips (Git: warrenphilly)


# Prints the board in a square to the console
def printboard(board):
    numbers = '01234567890123456789'
    mids = '_' * 20
    print(' ' + numbers)
    print(' ' + mids)
    for i in range(20):
        s = ''.join(board[i])
        print('|{}|{}'.format(s, i))
    print(' ' + mids)
    print(' ' + numbers)

    
# The first word is initialized in the center of the board
def addFirstWord(board, word):
    wordlength = len(word)
    boardlength = len(board)
    if wordlength > 20:
        return False
    rowposition = boardlength // 2
    columnposition = (boardlength - wordlength) // 2
    board[rowposition][columnposition: columnposition+wordlength] = word
    return True


# Checks to see if the word fits in any way vertically. Places the word in the last possible position
def checkvertical(board, word, row, col):
    # if the word is longer than the board it will not place
    wordlength = len(word)
    if wordlength > 20:
        print(word, "word is too big for the board")
        return False
    letterfound = False
    for i in range(wordlength):
        letter = word[i]
        if row + i == 19:
            break
        boardletter = board[row + i][col]
        if boardletter == letter and (board[row + (i + 1)][col] == ' ' and board[row + (i - 1)][col] == " "):
            for j in range(i):
                if col + 1 >= 20:
                    break
                if (board[row + j][col] == ' ' or board[row+j][col] == word[j]) and \
                        (board[row+j][col+1] == ' ' and board[row + j][col-1] == ' ' and board[row-1][col] == ' '):
                    letterfound = True
                else:
                    letterfound = False
                    break
            if letterfound:
                for j in range(wordlength - i - 1):
                    if row + wordlength + 1 + j >= 20:
                        break
                    if (board[row + wordlength - 1 - j][col] == ' ' or board[row + wordlength - 1 - j][col] == word[wordlength-1-j]) and \
                            (board[row + wordlength - 1 - j][col+1] == ' ' and board[row + wordlength - 1 - j][col-1] == ' ' and board[row+wordlength][col] == ' '):
                        letterfound = True
                    else:
                        letterfound = False
    return letterfound


# Inserts a word vertically if it fits
def addvertical(board, word):
    boardlength = len(board)
    wordlength = len(word)
    for i in range(boardlength):
        for j in range(boardlength):
            # call to see if word fits
            if checkvertical(board, word, i, j) is True:
                for a in range(wordlength):
                    board[i+a][j] = word[a]
                return True
    return False


# Checks to see if the word fits in any way horizontally. Places the word in the last possible position
def checkhorizontal(board, word, row, col):
    # if the word is longer than the board it will not place
    wordlength = len(word)
    if wordlength > 20:
        print(word, "word is too big for the board")
        return False
    letterfound = False
    for i in range(wordlength):
        let = word[i]
        if col+i == 19:
            break
        blet = board[row][col+i]
        if blet == let and (board[row][col + (i + 1)] == " " and board[row][col + (i - 1)] == " "):
            for j in range(i):
                if row + i >= 20:
                    break
                if (board[row][col + j] == " " or board[row][col + j] == word[j]) and \
                        (board[row + 1][col + j] == ' ' and board[row - 1][col + j] == ' ' and board[row][col - 1] == ' '):
                    letterfound = True
                else:
                    letterfound = False
                    break
            if letterfound:
                for j in range(wordlength - i - 1):
                    if col + wordlength - 1 - j >= 20 or col + wordlength >= 20:
                        break
                    if (board[row][col + wordlength - 1 - j] == ' '
                            or board[row][col + wordlength - 1 - j] == word[wordlength - 1 - j]) \
                            and (board[row+1][col + wordlength - 1 - j] == ' ' and board[row-1][col + wordlength - 1 - j] == ' ' and board[row][col + wordlength] == ' '):
                        letterfound = True
                    else:
                        letterfound = False
            if letterfound:
                return letterfound
    return letterfound


# Inserts a word horizontally if it fits
def addhorizontal(board, word):
    d = len(board)
    for i in range(d):
        for j in range(d):
            if checkhorizontal(board, word, i, j) is True:
                for y in range(len(word)):
                    board[i][j+y] = word[y]
                return True
    return False


# Alternates between adding words vertically and horizontally
def crossword(L):
    blank = ' '
    board = [[blank] * 20 for i in range(20)]
    addFirstWord(board, L[0])
    for i in range(1, len(L)):
        if i % 2 != 0:
            addvertical(board, L[i])
        else:
            addhorizontal(board, L[i])
    printboard(board)


# EXAMPLE FUNCTION CALL: crossword(['menacing', 'ericharley', 'stylistic', 'vivianhu', 'stan', 'drdavemason', 'daphne', 'cockwell', 'pitman', 'bedbug'])
# EXAMPLE 2: crossword(['guacamole', 'television', 'microwave', 'dishes', 'laundry', 'couch', 'computer', 'backpack', 'slurmp', 'lofus', 'bezel'])
