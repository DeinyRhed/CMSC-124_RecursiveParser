"""
CMSC 124 Machine Problem 3 - Item #2
Topic Coverage: Lexical and Syntax Analysis 
Programmed by Dianne M. Mondido


<expr> ::= +<num> | -<num> | <num> 
<num> ::= <num><digit> |<digits>
<digits> ::= <digit>.<digit> 
<digit> ::= 0|1|2|3|4|5|6|7|8|9 
Terminate every input string with ‘$’.
"""

class RecursiveParser():
    def __init__(self, input):    
        self.__source = input
        self.__currChar = None
        self.__currPos = -1
        self.__pointCount = 1   # Number of decimal point reserve
        self.__plusCount = 1    # Number of plus point reserve
        self.__minusCount = 1   # Number of minus point reserve
        self.__result = []      # Base Case. Stores valid characters
        self.nextChar()         # Goes to the first character of the string

    # Iterates over the string one-by-one
    def nextChar(self):
        self.__currPos += 1
        # Check if currPos has exceeded length of self.__source
        if self.__currPos >= len(self.__source):
            self.__currChar = '\0'
        else:
            self.__currChar = self.__source[self.__currPos]
    
    # Returns the next character of the self.__currChar
    def peek(self):
        if self.__currPos+1 >= len(self.__source):
            return '\0'
        return self.__source[self.__currPos+1]
    
    # Starting Non-Terminal
    def expr(self):
        #Checks if first char is '+' or '-' (+<num> or -<num>)
        if self.__currChar in ('+', '-'):
            if self.__currChar == '+' and self.peek().isdigit():
                # subtracts the reserve count, turning it to zero reserves
                self.__plusCount -= 1
                if self.__plusCount == 0:
                    self.__result.append(self.__currChar)
                    self.nextChar()
                    self.num()
                else:
                    return False
            elif self.__currChar == '-' and self.peek().isdigit():
                # subtracts the reserve count, turning it to zero reserves
                self.__minusCount -= 1
                if self.__minusCount == 0:
                    self.__result.append(self.__currChar)
                    self.nextChar()
                    self.num()
                else:
                    return False
        # checks if char is num (<num>)
        elif self.__currChar.isdigit():
            self.__result = self.num()
        else:
            return False
        return self.__result

    # Nonterminal
    def num(self):
        self.__result = self.digits()
        while self.__currChar.isdigit() or self.__currChar == '.':                                            
            self.num()
        return self.__result
    
    # Non-terminal
    def digits(self):
        # Check if current char is a digit.
        if self.__currChar.isdigit():
            self.__result.append(self.__currChar)
            self.nextChar()
        # Checks if current char is a decimal point and next char is a digit 
        elif self.__currChar == '.' and self.peek().isdigit():
            self.__pointCount -= 1
            if self.__pointCount == 0:
                self.__result.append(self.__currChar)
                self.nextChar()
            else:
                return False
        else:
            return False
        return self.__result
    
       
if __name__ == '__main__':
    while True:
        testCase = str(input())
        try:
            # If char == '$', that means char before that is the last char.
            if testCase[-1] == '$':
                # Removing '$' for simplicity
                testCase = testCase[:-1]
                checkResult = RecursiveParser(testCase).expr()
                # If the length of the list is equal to the original and result != False, string is valid
                if checkResult != False and len(testCase) == len(checkResult):
                    print ("Valid Input String")
                else:
                    print("Invalid Input String")
            else:
                print("Invalid Input String")
        # incase there are inputs not taken account for in the grammar
        except:
            print("Invalid Input String")
