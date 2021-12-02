"""
CMSC 124 Machine Problem 3 - Item #1
Topic Coverage: Lexical and Syntax Analysis 
Programmed by Dianne M. Mondido


<expr> ::= <expr>+<term> | <expr>-<term> | <term> 
<term> ::= <term>*<factor> | <term>/<factor> | <factor> 
<factor> ::= (<expr>) |<digit> 
<digit> ::= 0|1|2|3
"""

DIGIT = ['0','1','2','3']
OPERATION = ['+','-','*','\\']
PAR = ['(', ')']

class RecursiveParser():
    def __init__(self, input):    
        self.__source = input
        self.__currChar = None
        self.__currPos = -1
        self.__result = []  # Base Case. Stores valid characters
        self.nextChar()     # Goes to the first character of the string

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
        self.__result = self.term()
        while self.__currChar in ('+', '-'):
            if self.__currChar == '+' and (self.peek() in DIGIT or self.peek() in PAR):
                self.__result.append(self.__currChar)
                self.nextChar()
                self.term()
            elif self.__currChar == '-' and (self.peek() in DIGIT or self.peek() in PAR):
                self.__result.append(self.__currChar)
                self.nextChar()
                self.term()
            else:
                return False
        return self.__result

    # Nonterminal
    def term(self):
        self.__result = self.factor()
        while self.__currChar in ('*', '/'):
            if self.__currChar == '*' and (self.peek() in DIGIT or self.peek() in PAR):
                self.__result.append(self.__currChar)
                self.nextChar()                                                       
                self.term()                                                           
            elif self.__currChar == '/' and (self.peek() in DIGIT or self.peek() in PAR): 
                self.__result.append(self.__currChar)                                               
                self.nextChar()
                self.term()
            else:
                return False
        return self.__result
    
    # Non-terminal
    def factor(self):
        # Reads if char is Digit or next char is ')'
        if (self.__currChar in DIGIT and self.peek().isdigit() == False and self.peek() != '(') or self.peek() ==')':
            if self.peek() == ')':
                self.__result.append(self.__currChar)
                self.nextChar()
                if self.peek() == '\0':
                    self.__result.append(self.__currChar)
                    return self.__result
                # If next char is ')', it goes to funtion factor()
                elif self.peek() == ')':
                    self.factor()
                # Else, it goes to next character
                else:
                    self.__result.append(self.__currChar)
                    self.nextChar()       
            else:
                self.__result.append(self.__currChar)
                self.nextChar()
        elif self.__currChar == '(' and (self.peek() in DIGIT or self.peek() in PAR):
            self.__result.append(self.__currChar)
            self.nextChar()
            self.expr()
            self.nextChar()
        else:
            return False
        return self.__result

if __name__ == '__main__':
    while True:
        testCase = str(input())
        if testCase[-1] == '$':
            testCase = testCase[:-1]
            checkResult = RecursiveParser(testCase).expr()
            if checkResult != False:
                if testCase.count('(') == testCase.count(')'):
                    print ("Valid Input String")
                else:
                    print("Invalid Input String")
            else:
                print("Invalid Input String")
        else:
            print("Invalid Input String")
            
        
