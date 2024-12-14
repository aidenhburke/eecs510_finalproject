# Formal Language: Accept all valid arithmetic expressions

### Alphabet: 
The alphabet consists of parentheses, operators, and digits:

Σ = {(, ), +, -, *, /, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

### Intent of the Language:
The intent of this formal language is to define the structure of valid arithmetic expressions. Arithmetic expressions are a fundamental concept in mathematics and computer science, serving as the basis for evaluating numerical computations. By defining a formal language for arithmetic expressions, we ensure that every valid string in the language can be parsed and evaluated correctly. This language could be used in applications such as compilers, calculators, or symbolic math solvers to verify the syntactic correctness of input expressions.

The language includes just a single number or set of parentheses, and also complex expressions with nested parentheses like (((2)+(7*8))/(3-6)+2)/1. 

It is important to note that the language only restricts expressions semantically, and not mathematically; for example, 4/0 would be valid in the language, even though division by 0 is not allowed mathematically. 

### Rules & Semantics
Operands:

A valid operand is any non-negative integer, represented as one or more consecutive digits (e.g., 42, 123).

Operators:

Operators (+, -, *, /) must always appear between two valid operands or subexpressions (e.g., 3 + 5 or (2 * 3) + 4).

Parentheses:

Parentheses are used to group subexpressions and enforce precedence rules. Each open parenthesis ( must have a corresponding close parenthesis ).

For example, (2 + 3) * 4 is valid, while (2 + 3 * 4 is not.

There are some things that can make expressions invalid, and the grammar rules would reject anything that includes:
+ Mismatched parentheses:  )(
+ Unclosed or unopened parentheses: (, )
+ Hanging operators: 5+, *
+ Multiple operators in a row: (5++2), 3-*
+ Whitespace: 5 + 1

### Valid and Invalid String Examples
Examples of Valid Strings

3+5

42*(7-2)

(3+5)*2

((10/2)+4)*3

Examples of Invalid Strings

3+ (operator without a second operand)

3 4 (missing operator between operands & whitespace)

*3 (operator without a first operand)

(3+4 (unmatched parentheses)

3+(4*) (operator without a second operand inside parentheses)
