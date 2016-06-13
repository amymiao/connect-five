'''
A series of test cases to ensure that the AI functions
as expected in common situations of the game connect5.
These test cases include both offensive and defensive plays.
'''

from connect_5 import *



class UnitTests():
    #Defensive plays

    def two_3s_test1(self):
        connect5 = Connect5(10)
        connect5.update_board(5, 5, "user")
        connect5.update_board(5, 4, "user")
        connect5.update_board(6, 6, "user")
        connect5.update_board(7, 6, "user")
        connect5.print_board()

        expected_move = (5,6)


    def two_3s_test2(self):
        connect5 = Connect5(10)
        connect5.update_board(0, 0, "user")
        connect5.update_board(1, 1, "user")
        connect5.update_board(3, 1, "user")
        connect5.update_board(4, 0, "user")
        connect5.print_board()

        expected_move = (2,2)


    def two_3s_test3(self):
        connect5 = Connect5(10)
        connect5.update_board(7, 4, "user")
        connect5.update_board(7, 5, "user")
        connect5.update_board(8, 8, "user")
        connect5.update_board(9, 9, "user")
        connect5.print_board()        

        expected_move = (7,7)
        

    def two_3s_test4(self):
        connect5 = Connect5(10)
        connect5.update_board(7, 4, "user")
        connect5.update_board(7, 5, "user")
        connect5.update_board(8, 8, "user")
        connect5.update_board(6, 6, "user")
        connect5.print_board()

        expected_move = (7,7)

        
    def two_3s_test5(self):
        connect5 = Connect5(10)
        connect5.update_board(6, 3, "user")
        connect5.update_board(6, 4, "user")
        connect5.update_board(8, 8, "user")
        connect5.update_board(9, 9, "user")
        connect5.print_board()    

        expected_move = (6,6)


    def unblocked_3_test1(self):
        connect5 = Connect5(10)
        connect5.update_board(7, 4, "user")
        connect5.update_board(7, 5, "user")
        connect5.update_board(7, 6, "user")
        connect5.print_board()        

        expected_move1 = (7,3)
        expected_move2 = (7,7)


    def unblocked_3_test2(self):
        connect5 = Connect5(10)
        connect5.update_board(1, 1, "user")
        connect5.update_board(2, 2, "user")
        connect5.update_board(3, 3, "user")
        connect5.print_board()

        expected_move1 = (0,0)
        expected_move2 = (4,4)        



    def unblocked_3_test3(self): #modify
        connect5 = Connect5(10)
        connect5.update_board(0, 2, "user")
        connect5.update_board(1, 2, "user")
        connect5.update_board(3, 2, "user")
        connect5.print_board()



    def unblocked_3_test4(self):
        connect5 = Connect5(10)
        connect5.update_board(4, 6, "user")
        connect5.update_board(5, 5, "user")
        connect5.update_board(7, 3, "user")
        connect5.print_board()        

        expected_move = (6,4)


    def blocked_4_test1(self):
        connect5 = Connect5(10)
        connect5.update_board(4, 6, "user")
        connect5.update_board(4, 7, "user")
        connect5.update_board(4, 5, "user")
        connect5.update_board(4, 4, "computer")
        connect5.update_board(4, 8, "user")
        connect5.print_board()

        expected_move = (4,9)


    def blocked_4_test2(self):
        connect5 = Connect5(10)
        connect5.update_board(4, 6, "user")
        connect5.update_board(5, 5, "user")
        connect5.update_board(6, 4, "user")
        connect5.update_board(7, 3, "computer")
        connect5.update_board(3, 7, "user")
        connect5.print_board()

        expected_move = (2,8)


    def blocked_4_test3(self):
        connect5 = Connect5(10)
        connect5.update_board(4, 4, "user")
        connect5.update_board(5, 5, "user")
        connect5.update_board(7, 7, "user")
        connect5.update_board(8, 8, "user")
        connect5.print_board()
        
        expected_move = (6,6)


    def blocked_4_test4(self):
        connect5 = Connect5(10)
        connect5.update_board(1, 1, "user")
        connect5.update_board(3, 1, "user")
        connect5.update_board(4, 1, "user")
        connect5.update_board(5, 1, "user")
        connect5.print_board()

        expected_move = (2,1)


    '''
    These tests are more difficult and require a higher level of play
    to differentiate when to block, when to attack and what attack will
    yield the best state.

    These tests were created based on the author's experiences with the game.
    It will not judge the performances absolutely but it will provide a good
    measure of the AI's ability.
    '''
    #Know to attack rather than block: will win in fewer steps
    def advanced_attack_test1(self):
        connect5 = Connect5(10)
        connect5.update_board(3, 1, "computer")
        connect5.update_board(2, 0, "user")
        connect5.update_board(3, 2, "computer")
        connect5.update_board(6, 2, "user")
        connect5.update_board(3, 3, "computer")
        connect5.update_board(5, 1, "user")
        connect5.update_board(3, 4, "computer")
        connect5.update_board(3, 0, "user")
        connect5.print_board()
        
    #Know to attack rather than block: will win in fewer steps
    def advanced_attack_test2(self):
        connect5 = Connect5(10)
        connect5.update_board(1, 0, "computer")
        connect5.update_board(5, 1, "user")
        connect5.update_board(2, 0, "computer")
        connect5.update_board(5, 2, "user")
        connect5.update_board(3, 0, "computer")
        connect5.update_board(5, 3, "user")
        connect5.print_board()

    #Plan attack for two moves in advance
    def advanced_attack_test3(self):
        connect5 = Connect5(10)
        connect5.update_board(4, 1, "computer")
        connect5.update_board(4, 2, "computer")
        connect5.update_board(3, 3, "computer")
        connect5.update_board(5, 4, "computer")
        connect5.update_board(5, 5, "computer")
        connect5.print_board()
        
    #Know to block while attacking
    def advanced_defend_test1(self):
        connect5 = Connect5(10)
        connect5.update_board(2, 1, "user")
        connect5.update_board(2, 0, "computer")
        connect5.update_board(3, 2, "user")
        connect5.update_board(3, 0, "computer")
        connect5.update_board(4, 3, "user")
        connect5.print_board()

    #Know to block while attacking
    def advanced_defend_test2(self):
        connect5 = Connect5(10)
        connect5.update_board(5, 0, "user")
        connect5.update_board(1, 0, "computer")
        connect5.update_board(3, 1, "user")
        connect5.update_board(3, 0, "computer")
        connect5.update_board(4, 2, "user")
        connect5.update_board(4, 0, "computer")
        connect5.update_board(5, 3, "user")
        connect5.print_board()

    #Know to block rather than trying to attack: blocking is more urgent
    def advanced_defend_test3(self):
        connect5 = Connect5(10)
        connect5.update_board(4, 1, "computer")
        connect5.update_board(5, 1, "user")
        connect5.update_board(5, 2, "computer")
        connect5.update_board(6, 1, "user")
        connect5.update_board(6, 2, "computer")
        connect5.update_board(7, 1, "user")
        connect5.update_board(7, 2, "computer")
        connect5.update_board(9, 1, "user")
        connect5.print_board()

    #Consider borders and block pieces when attacking
    def advanced_attack_spatial_sense_test1(self):
        connect5 = Connect5(10)
        connect5.update_board(1, 0, "computer")
        connect5.update_board(2, 0, "computer")
        connect5.update_board(3, 0, "computer")
        connect5.print_board()

    #Consider borders and block pieces when attacking
    def advanced_attack_spatial_sense_test2(self):
        connect5 = Connect5(10)
        connect5.update_board(4, 1, "user")
        connect5.update_board(4, 3, "computer")
        connect5.update_board(4, 4, "computer")
        connect5.update_board(4, 5, "computer")
        connect5.print_board()

    #Consider borders and block pieces when attacking
    def advanced_attack_spatial_sense_test3(self):
        connect5 = Connect5(10)
        connect5.update_board(4, 1, "user")
        connect5.update_board(4, 3, "computer")
        connect5.update_board(4, 6, "user")
        connect5.update_board(4, 4, "computer")
        connect5.update_board(4, 5, "computer")
        connect5.print_board()

    def run_all_basic_tests(self):
        #Run test suite: basic       
        unit_tests = UnitTests()
        print("-------------------------------------------------------------")
        unit_tests.two_3s_test1()
        print("-------------------------------------------------------------")
        unit_tests.two_3s_test2()
        print("-------------------------------------------------------------")
        unit_tests.two_3s_test3()
        print("-------------------------------------------------------------")
        unit_tests.two_3s_test4()
        print("-------------------------------------------------------------")
        unit_tests.two_3s_test5()
        print("-------------------------------------------------------------")
        unit_tests.unblocked_3_test1()
        print("-------------------------------------------------------------")
        unit_tests.unblocked_3_test2()
        print("-------------------------------------------------------------")
        unit_tests.unblocked_3_test3()
        print("-------------------------------------------------------------")
        unit_tests.unblocked_3_test4()
        print("-------------------------------------------------------------")
        unit_tests.blocked_4_test1()
        print("-------------------------------------------------------------")
        unit_tests.blocked_4_test2()
        print("-------------------------------------------------------------")
        unit_tests.blocked_4_test3()
        print("-------------------------------------------------------------")
        unit_tests.blocked_4_test4()
        print("-------------------------------------------------------------")

    def run_all_tests(self):
        #Run test suite: basic       
        unit_tests = UnitTests()
        print("-------------------------------------------------------------")
        unit_tests.two_3s_test1()
        print("-------------------------------------------------------------")
        unit_tests.two_3s_test2()
        print("-------------------------------------------------------------")
        unit_tests.two_3s_test3()
        print("-------------------------------------------------------------")
        unit_tests.two_3s_test4()
        print("-------------------------------------------------------------")
        unit_tests.two_3s_test5()
        print("-------------------------------------------------------------")
        unit_tests.unblocked_3_test1()
        print("-------------------------------------------------------------")
        unit_tests.unblocked_3_test2()
        print("-------------------------------------------------------------")
        unit_tests.unblocked_3_test3()
        print("-------------------------------------------------------------")
        unit_tests.unblocked_3_test4()
        print("-------------------------------------------------------------")
        unit_tests.blocked_4_test1()
        print("-------------------------------------------------------------")
        unit_tests.blocked_4_test2()
        print("-------------------------------------------------------------")
        unit_tests.blocked_4_test3()
        print("-------------------------------------------------------------")
        unit_tests.blocked_4_test4()
        print("-------------------------------------------------------------")

        #Run test suite: advanced
        print("-------------------------------------------------------------")
        #unit_tests.advanced_attack_test1()
        print("-------------------------------------------------------------")
        #unit_tests.advanced_attack_test2()
        print("-------------------------------------------------------------")
        #unit_tests.advanced_attack_test3()
        print("-------------------------------------------------------------")
        #unit_tests.advanced_defend_test1()
        print("-------------------------------------------------------------")
        #unit_tests.advanced_defend_test2()
        print("-------------------------------------------------------------")
        #unit_tests.advanced_defend_test3()
        print("-------------------------------------------------------------")
        #unit_tests.advanced_attack_spatial_sense_test1()
        print("-------------------------------------------------------------")
        #unit_tests.advanced_attack_spatial_sense_test2()
        print("-------------------------------------------------------------")
        #unit_tests.advanced_attack_spatial_sense_test3()
        print("-------------------------------------------------------------")









