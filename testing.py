from automaton import Automaton

def test():
    a = Automaton()
    # a.test_string("((15+3)*4)+(3/3)") # test case 
    while True:
        string = input("Enter a string to test: ")
        a.test_string(string)

if __name__ == "__main__":
    test()