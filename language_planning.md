# Formal Language
## Accept any mathematical string including integers, parentheses, and +, -, *, and / operators

## Grammar Structure:

**Alphabet: Σ = {(, ), +, -, *, /, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}**

**Production Rules:**

S -> (S) | ABA | SBS | A

A -> AA | ABA | N

B -> + | - | * | /

N -> 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0

## Examples: 

### 105 * 13

S ⊢

ABA ⊢

A * A ⊢

AA * AA ⊢

AAA * AA ⊢

105 * 13

### ((15 + 3) * 4) + (3 / 3)

S ⊢

SBS ⊢

S + S ⊢

(S) + (S) ⊢

(SBS) + (ABA) ⊢

((S) * S) + (ABA) ⊢

((ABA) * A) + (ABA) ⊢

((AA + A) * A) + (A / A) ⊢

((15 + 3) * 4) + (3 / 3)

## PDA Rules:

things to consider:
+ whenever an operator is pushed, you need a way to ensure it is followed by a digit
+ parentheses need a stack to keep track of paired brackets
+ maybe only push a character to the stack for the first digit 