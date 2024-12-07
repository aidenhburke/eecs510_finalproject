# Formal Language
## Accept any mathematical string including integers, parentheses/brackets, and +, -, *, and / operators

## Grammar Structure:

S -> (S) | ABA | SBS | A

A -> AA | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0

B -> + | - | * | /

## Examples: 

### 105 * 13

S ->

ABA ->

A * A ->

AA * AA ->

AAA * AA ->

105 * 13

### ((15 + 3) * 4) + (3 / 3)

S -> 

SBS -> 

S + S -> 

(S) + (S) -> 

(SBS) + (ABA) -> 

((S) * S) + (ABA) -> 

((ABA) * A) + (ABA) ->

((AA + A) * A) + (A / A) ->

((15 + 3) * 4) + (3 / 3)

## PDA Rules:
