# CMSC-124_RecursiveParser

Implementing a recursive-descent parser for the following grammar rules: 
 
1. Grammar rules for an arithmetic expression: 
  <expr> ::= <expr>+<term> | <expr>-<term> | <term> 
  <term> ::= <term>*<factor> | <term>/<factor> | <factor> 
  <factor> ::= (<expr>) |<digit> 
  <digit> ::= 0|1|2|3 Terminate every input string with ‘$’. 

2. Grammar rules for a multi-digit decimal number 
    <expr> ::= +<num> | -<num> | <num> 
    <num> ::= <num><digits> | <digits> 
    <digits> ::= <digit> | <digit>.<digit> 
    <digit> ::= 0|1|2|3|4|5|6|7|8|9 Terminate every input string with ‘$’
