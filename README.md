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

### Save tex to file
save tex class to file
```py
tex.write("test.tex")
```

## Example
example making math test
```py
from mathtex import MathTex, Problem

tex = MathTex("Calculus Problem Test", "smiilliin")

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
            "\\( x^4 + C \\)",
        ],
    )
)

tex.write("test.tex")
```
[Result tex file(test.tex)](./test.pdf)
```tex
\documentclass{article}
\usepackage{tasks}
\usepackage{kotex}
\usepackage{datetime2}
\usepackage{multicol}
\usepackage{amsmath}
\usepackage[a4paper, margin=1in]{geometry}
\title{Calculus Problem Test}
\author{smiilliin}
\date{\today}\begin{document}
\maketitle\begin{multicols*}{2}
\noindent
\begin{minipage}{\linewidth}
1. Solve \[ \int x^2 dx \]\begin{tasks}[label=\textcircled{\scriptsize\arabic*},label-width=13pt](3)\task \( \frac{x^3}{3} + C \)\task \( \frac{x^2}{2} + C \)\task \( \frac{x^3}{2} + C \)\task \( x^2 + C \)\end{tasks}
\end{minipage}
\bigskip

\noindent
\begin{minipage}{\linewidth}
2. Solve \[ \int 4x^3 dx \]\begin{tasks}[label=\textcircled{\scriptsize\arabic*},label-width=13pt](3)\task \( {x^4} + C \)\task \( \frac{1}{x} + C \)\task \( {x^2} + C \)\task \( x^4 + C \)\end{tasks}
\end{minipage}
\bigskip

\end{multicols*}
\end{document}
```