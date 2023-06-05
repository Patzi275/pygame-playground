class Game():
    def __init__(self):
        self.XO = 'x'
        self.winner = None
        self.draw = False
        self.board = [[None]*3, [None]*3, [None]*3]
        self.history = []
        
    def check_win(self):
        # checking for winnig row
        winning_pos = []
        board = self.board
        for row in range(3):
            if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
                self.winner = board[row][0]
                winning_pos = ("r", row)
                break

        # checking for winning columns
        for col in range(3):
            if ((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
                self.winner = board[0][col]
                winning_pos = ("c", col)
                break
        
        # check for diagonal winners
        if ((board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None)):
            self.winner = board[0][0]
            winning_pos = ("d", 0)

        if ((board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None)):
            self.winner = board[0][2]
            winning_pos = ("d", 1)

        if (all([all(row) for row in board]) and self.winner is None):
            self.draw = True

        return winning_pos

    def play(self, row, col):
        self.board[row - 1][col - 1] = self.XO
        self.history.append((self.XO, row, col))
        self.XO = 'o' if self.XO == 'x' else 'x'
    
    def undo(self):
        if not self.history:
            return
        XO, row, col = self.history[-1]
        self.board[row - 1][col - 1] = None
        self.history.pop()
        self.XO = XO
        self.winner = None
        self.draw = False

    def canPlay(self, row, col):
        return (row and col and self.board[row-1][col-1] is None)

    def reset(self, first = 'x'):
        self.XO = first
        self.draw = False
        self.winner = None
        self.board = [[None]*3, [None]*3, [None]*3]

    def isFinished(self):
        return self.winner or self.draw