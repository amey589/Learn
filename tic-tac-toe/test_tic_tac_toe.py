from ttt import Board,Mark
import unittest

class testMarkMethods(unittest.TestCase):
    def test_mark_init(self):
        m1 = Mark(0)
        self.assertEqual(m1.mark,0,"mark set at 0")
        self.assertEqual(str(m1),"O","mark dispplay as O")
        m1 = Mark(1)
        self.assertEqual(m1.mark,1,"mark set at 1")
        self.assertEqual(str(m1),"X","mark dispplay as X")
    
    def test_mark_equality(self):
        m1 = Mark(0)
        m2 = Mark(0)
        self.assertTrue(m1 == m2,"mark equality correct")

class testBoardMethods(unittest.TestCase):
    def test_board_init(self):
        b = Board(3)
        self.assertEqual(b.empty_mark.mark , -1)
        self.assertEqual(b.bd, 3)
        self.assertEqual(len(b.winning_combo),8,"winning combo length correct")

    def test_make_new_board(self):
        b = Board(3)
        b.make_new_board()
        self.assertEqual(len(b.board),b.bd*b.bd,"length of board is set to board dimentions")
        self.assertEqual(b.board[0],b.empty_mark,"empty cell set at board 0 0")
    
    def test_make_move(self):
        b = Board(3)
        b.make_new_board()
        m1 = Mark(0)
        b.make_move(0,m1)
        self.assertEqual(len(b.board),b.bd*b.bd,"length of board is set to board dimentions")
        self.assertEqual(b.board[0],m1,"cell marked")
        
        #TODO: check exception using UT
        with self.assertRaises(Exception) as context:
            b.make_move(0,m1)
        print "exception message is " + str(context.exception)
        self.assertTrue("Invalid move" in str(context.exception))

    def  test_make_winnning_combo(self):
        b = Board(3)
        b.make_new_board()
        wc = b.make_winning_combo()
        self.assertEqual(len(wc),8,"winning combo len is correct")
        self.assertTrue(wc[0] == (0,1,2), "winnnng combo entry 0 is correct")
    
    def test_print_board(self):
        b = Board(3)
        b.make_new_board()
        b.print_board()
   
    def test_is_board_empty(self):
        b = Board(3)
        b.make_new_board()
        self.assertTrue(b.is_board_empty(),"board is empty")
        m = Mark(0)
        b.make_move(0,m)
        self.assertFalse(b.is_board_empty(),"board is not empty")


    def  test_check_winner(self):
        b = Board(3)
       
        # test row winning 
        b.make_new_board()
        m1 = Mark(0)
        m2 = Mark(0)
        b.make_move(0,m1)
        b.make_move(1,m2)
        b.make_move(2,m1)
        (winning_mark,stat) = b.check_winner()
        print "mark is " + repr(b.board[0].mark)
        print "mark is " + repr(b.board[1].mark)
        print "board is " + repr(b.board)
        self.assertTrue(b.board[0].mark ==   b.board[1].mark, "board mark equality passed" )
        print "winning mark is " + str(winning_mark) + "stat is " + str(stat)

        self.assertEqual(winning_mark,m1,"winning mark correct")
        self.assertEqual(stat,True,"status returned true correcntly")
        
        # test column winning
        b1 = Board(3)
        b1.make_new_board()
        m1 = Mark(1)
        m2 = Mark(1)
        b1.make_move(0,m1)
        b1.make_move(3,m2)
        b1.make_move(6,m1)
        (winning_mark,stat) = b1.check_winner()
        print "mark is " + repr(b1.board[0].mark)
        print "mark is " + repr(b1.board[1].mark)
        print "board is " + repr(b1.board)
        print "winning mark is " + str(winning_mark) + "stat is " + str(stat)
        self.assertEqual(winning_mark,m1,"winning mark correct")
        self.assertEqual(stat,True,"status returned true correcntly")
        
        # test diagonal winning
        b2 = Board(3)
        b2.make_new_board()
        m1 = Mark(1)
        m2 = Mark(1)
        b2.make_move(2,m1)
        b2.make_move(4,m2)
        b2.make_move(6,m1)
        (winning_mark,stat) = b2.check_winner()
        print "mark is " + repr(b2.board[0].mark)
        print "mark is " + repr(b2.board[1].mark)
        print "board is " + repr(b2.board)
        print "winning mark is " + str(winning_mark) + "stat is " + str(stat)
        self.assertEqual(winning_mark,m1,"winning mark correct")
        self.assertEqual(stat,True,"status returned true correcntly")
        
        # test no winner
        b3 = Board(3)
        b3.make_new_board()
        m1 = Mark(1)
        m2 = Mark(1)
        b3.make_move(1,m1)
        b3.make_move(4,m2)
        b3.make_move(6,m1)
        (winning_mark,stat) = b3.check_winner()
        print "mark is " + repr(b3.board[0].mark)
        print "mark is " + repr(b3.board[1].mark)
        print "board is " + repr(b3.board)
        print "winning mark is " + str(winning_mark) + "stat is " + str(stat)
        self.assertEqual(winning_mark,b3.empty_mark,"winning mark correct")
        self.assertEqual(stat,False,"status returned true correcntly")
        
if __name__ == '__main__':
         unittest.main()
