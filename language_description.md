# Formal Language: Accept all valid arithmetic expressions
## Alphabet: Σ = {(, ), +, -, *, /, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

The purpose of the language is simply to accept any valid arithmetic expression including numbers, elementary operations (multiplication, addition, subtraction, and division), as well as parenthetical separation. 

The language includes just a single number or set of parentheses, and also complex expressions with nested parentheses like (((2)+(7*8))/(3-6)+2)/1. 

It is important to note that the language only restricts expressions semantically, and not mathematically; for example, 4/0 would be valid in the language, even though division by 0 is not allowed mathematically. 

There are some things that can make expressions invalid, and the grammar rules would reject anything that includes:
+ Mismatched parentheses:  )(
+ Unclosed or unopened parentheses: (, )
+ Hanging operators: 5+, *
+ Multiple operators in a row: (5++2), 3-*


