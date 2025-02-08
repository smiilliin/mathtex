# Mathtex
Useful tool to make math test tex

## Usage

### Define MathTex object
define MatTex class object
```py
tex = MathTex("High school test", "smiilliin")
```

### Add problem to tex
add a problem with problem class
```py
tex.add_problem(
    Problem(
        "Solve \\[ \\int x^2 dx \\]",
        [
            "\\( \\frac{x^3}{3} + C \\)",
            "\\( \\frac{x^2}{2} + C \\)",
            "\\( \\frac{x^3}{2} + C \\)",
            "\\( x^2 + C \\)",
        ],
    )
)
```
### Problem class parameters
problem class constructing parameters
| prompt | choices  | width_count(Default 3) |
| -- | -- | --|
| Problem prompt| Choices text | Number of choices to place in one line |

### Add answer keys
add answer keys on new page
```py
tex.add_answer_key([1, 1, 3, 4, 5, 2, 1, 3, 3])
tex.add_answer_key(1)
tex.add_answer_key(2)
```

### Save tex to file
save tex class to file
```py
tex.write("test.tex")
```

## Example
example making math test
```py
from mathtex import MathTex, Problem

tex = MathTex("Calculus Problem Test", "smiilliin", "Answer Key")


tex.add_problem(
    Problem(
        "Solve \\[ \\int x^2 dx \\]",
        [
            "\\( \\frac{x^3}{3} + C \\)",
            "\\( \\frac{x^2}{2} + C \\)",
            "\\( \\frac{x^3}{2} + C \\)",
            "\\( x^2 + C \\)",
        ],
    )
)


tex.add_problem(
    Problem(
        "Solve \\[ \\int 4x^3 dx \\]",
        [
            "\\( {x^4} + C \\)",
            "\\( \\frac{1}{x} + C \\)",
            "\\( {x^2} + C \\)",
            "\\( x^5 + C \\)",
        ],
    )
)

tex.add_answer_key([1, 1, 3, 4, 5, 2, 1, 3, 3, 2, 2, 5, 4, 2, 3, 3, 4, 4, 1, 2])

tex.write("test.tex")
```
[Result tex file(test.tex)](./test.pdf)

```py
from mathtex import MathTex, Problem
import random

tex = MathTex("삼각함수 단순 미적분 100문제", "이지환 - smiilliin", "정답")

question_d = [
    "\\((\\sin x)'\\)",
    "\\((\\cos x)'\\)",
    "\\((\\tan x)'\\)",
    "\\((\\csc x)'\\)",
    "\\((\\sec x)'\\)",
    "\\((\\cot x)'\\)",
    "\\(-(\\sin x)'\\)",
    "\\(-(\\cos x)'\\)",
    "\\(-(\\tan x)'\\)",
    "\\(-(\\csc x)'\\)",
    "\\(-(\\sec x)'\\)",
    "\\(-(\\cot x)'\\)",
]
answer_d = [
    "\\(\\cos x\\)",
    "\\(-\\sin x\\)",
    "\\(\\sec^2 x\\)",
    "\\(-\\csc x \\cot x\\)",
    "\\(\\sec x \\tan x\\)",
    "\\(-\\csc^2 x\\)",
    "\\(-\\cos x\\)",
    "\\(\\sin x\\)",
    "\\(-\\sec^2 x\\)",
    "\\(\\csc x \\cot x\\)",
    "\\(-\\sec x \\tan x\\)",
    "\\(\\csc^2 x\\)",
]
wtf_answer_d = [
    "\\(\\tan x\\)",
    "\\(\\sec x \\cot x\\)",
    "\\(\\sec x \\sin x\\)",
    "\\(\\sec x \\cos x\\)",
    "\\(\\cos^2 x\\)",
    "\\(-\\csc x \\sin x\\)",
    "\\(-\\csc x \\cos x\\)",
    "\\(-\\csc x \\tan x\\)",
    "\\(-\\sin^2 x\\)",
    "\\(\\cot^2 x\\)",
]

question_i = [
    "\\( \\int \\cos x \, dx\\)",
    "\\( \\int -\\sin x \, dx\\)",
    "\\( \\int \\sec^2 x \, dx\\)",
    "\\( \\int -\\csc x \\cot x \, dx\\)",
    "\\( \\int \\sec x \\tan x \, dx\\)",
    "\\( \\int -\\csc^2 x\, dx\\)",
    "\\( \\int -\\cos x \, dx\\)",
    "\\( \\int \\sin x \, dx\\)",
    "\\( \\int -\\sec^2 \, dx\\)",
    "\\( \\int \\csc x \\cot x \, dx\\)",
    "\\( \\int -\\sec x \\tan x \, dx\\)",
    "\\( \\int \\csc^2 x \, dx\\)",
]
answer_i = [
    "\\(\\sin x + C\\)",
    "\\(\\cos x + C\\)",
    "\\(\\tan x + C\\)",
    "\\(\\csc x + C\\)",
    "\\(\\sec x + C\\)",
    "\\(\\cot x  + C\\)",
    "\\(-\\sin x + C\\)",
    "\\(-\\cos x + C\\)",
    "\\(-\\tan x + C\\)",
    "\\(-\\csc x + C\\)",
    "\\(-\\sec x + C\\)",
    "\\(-\\cot x  + C\\)",
]

N = 100
for i in range(100):
    if random.random() > 0.5:
        k = random.randint(0, len(question_d) - 1)
        question = question_d[k]
        answer = answer_d[k]
        picked_answers = random.sample(
            answer_d[:k] + answer_d[k + 1 :] + wtf_answer_d, k=5
        )
        n = random.randint(0, 4)
        picked_answers[n] = answer
        tex.add_problem(Problem(question, picked_answers))
    else:
        k = random.randint(0, len(question_i) - 1)
        question = question_i[k]
        answer = answer_i[k]
        picked_answers = random.sample(answer_i[:k] + answer_i[k + 1 :], k=5)
        n = random.randint(0, 4)
        picked_answers[n] = answer
        tex.add_problem(Problem(question, picked_answers))

    tex.add_answer_key(n)

tex.write("trig_deriv_int_test.tex")
```
[Result tex file(trig_deriv_int_test.tex)](./trig_deriv_int_test.pdf)