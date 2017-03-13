import sys
class Mark:
    def __init__(self,mark):
        self.mark = mark
    def __str__(self):
        if (self.mark == 0):
            return "O"
        elif (self.mark == 1):
            return "X"
        elif (self.mark == -1):
            return "-"
    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            #return self.__dict__ == other.__dict__
            return self.mark == other.mark
        return False
    def __ne__(self, other):
        """Define a non-equality test"""
        return not self.__eq__(other)

class Board: 
    def __init__(self,bd):
        self.board = []
        self.bd = bd
        self.empty_mark = Mark(-1)
        self.winning_combo = self.make_winning_combo()
    
    def make_new_board(self):
        for i in range(0,self.bd*self.bd):
            self.board.append(self.empty_mark)
            
    
    def make_move(self,move_location,move_mark):
        """
        fills the board array at move_location with
        give move_mark
        """
        ml = move_location
        if (not self.board[ml] == self.empty_mark):
            raise Exception("Invalid move : cell already marked")
        else:
            self.board[ml] = move_mark
            #print "marked the board at " + str(move_location) + "with move "+ str(move_mark)
    
    def make_winning_combo(self):
        winning_combo = [
                        (0,1,2),
                        (3,4,5),
                        (6,7,8),
                        (0,3,6),
                        (1,4,7),
                        (2,5,8),
                        (0,4,8),
                        (2,4,6)
                        ]
        return winning_combo
  
    def check_winner(self):
        for item in self.winning_combo:
            i,j,k = item

            #print "checking item for winning stategy " + str(item)
            #print "boart i j k at " + repr(self.board[i].mark) + repr(self.board[j].mark) + repr(self.board[k].mark)
            if ((self.board[i] == self.board[j] == self.board[k])
                and 
                (self.board[i] != self.empty_mark)):
                #print "looks like we have a winner"
                winning_mark = self.board[i]
                return (winning_mark,True)
        return (self.empty_mark,False)
    def print_board(self):
        print "\nBoard looks like:\n"
        for i in range(0,self.bd*self.bd):
            sys.stdout.write(str(self.board[i])+ "  ")
            sys.stdout.write("[" + str(i)+"]")
            sys.stdout.write(str("   "))
            sys.stdout.flush()
            if (((i+1) % self.bd) == 0):
               print "\n"
        print "\n"
           
    def is_board_empty(self):
        for i in range(self.bd*self.bd):
            if (self.board[i] != self.empty_mark):
                return False
        return True
    
    def is_vacant_cell(self):
        for i in range(self.bd*self.bd):
            if (self.board[i] == self.empty_mark):
                return True
        return False
    

b = Board(3)
m0 = Mark(0)
m1 = Mark(1)
b.make_new_board()
b.print_board()
turn_0 = True

while (b.is_vacant_cell()):
    if (True == turn_0):
        move_location = raw_input("Enter location for 0 : ")
        move_location = int(move_location)
        b.make_move(move_location,m0)
        b.print_board()
        (winner_mark,stat) = b.check_winner()
        if (stat):
            print "winner is " + str(winner_mark)
            break
    elif (False == turn_0):
        move_location = raw_input("Enter location for X : ")
        move_location = int(move_location)
        b.make_move(move_location,m1)
        b.print_board()
        (winner_mark,stat) = b.check_winner()
        if (stat):
            print "winner is " + str(winner_mark)
            break
    turn_0 = not turn_0
(winner_mark,stat) =b.check_winner() 
if (stat):
    print "winner is " + str(winner_mark)
else:
    print "---- Its a draw -- "

