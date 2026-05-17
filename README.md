# CLI Calculator

A minimalist, lightweight command-line calculator built in Python. Designed for rapid mathematical evaluations directly from your terminal, prioritizing simplicity, speed, and clean code execution.

## Key Features

* **Arithmetic & Order of Operations:** Handles standard operations (+, -, *, /) while fully respecting explicit parenthesis nesting and default operator precedence.
* **Advanced Mathematical Functions:** Integrated support for standard transcendental and algebraic functions including trigonometry, logarithms, powers, and absolute values.
* **Built-in Constants:** Full support for the Archimedes constant ($\pi$) via the pi keyword.
* **Rigorous Input Validation:** Eleven distinct validation checks filter out malformed syntax, structural errors, invalid characters, and structural exploits before evaluation begins.
* **Graceful Error Handling:** Provides descriptive, contextual feedback for syntax validation failures and mathematical domain violations (e.g., division by zero, negative square roots).

## Supported Mathematical Operations
### 1. Operators

    + : Addition

    - : Subtraction

    * : Multiplication

    / : Division

### 2. Functions & Constants

| Function / Constant | Description | Example Input | Expected Output |
| :--- | :--- | :--- | :--- |
| `pi` | The constant ratio $\pi \approx 3.14159265...$ | `pi` | `3.141592653589793` |
| `sqrt(x)` | Square root ($\sqrt{x}$). Domain: $x \ge 0$ | `sqrt(81)` | `9.0` |
| `pow(x, y)` | Power function ($x^y$) | `pow(2, 3)` | `8.0` |
| `log(x)` | Natural logarithm ($\ln x$). Domain: $x > 0$ | `log(pi)` | `1.1447298858494002` |
| `sin(x)` | Sine function (input in radians) | `sin(pi / 2)` | `1.0` |
| `cos(x)` | Cosine function (input in radians) | `cos(pi)` | `-1.0` |
| `tan(x)` | Tangent function (input in radians) | `tan(pi / 4)` | `0.9999999999999999` |
| `abs(x)` | Absolute value ($|x|$) | `abs(-5.5)` | `5.5` |
| `round(x, [n])` | Rounds $x$ to nearest integer or $n$ decimal places | `round(4.57, 1)` | `4.6` |

**Technical Note on Rounding:** Python utilizes "Banker's Rounding" (half-to-even) for numbers exactly halfway between two integers. Consequently, round(4.5) evaluates to 4, whereas round(5.5) evaluates to 6


## Installation & Setup
### Prerequisites

* Python 3.6 or higher. No external third-party dependencies are required.

### Installation Steps

1. Clone this repository to your local system:
    ```text
    git clone https://github.com/nuhaak/ITAP-COSC-3411-Gamma.git
2. Navigate into the project directory:
    ```text
   cd cli-calculator
3. Ensure the script file has execution privileges (Unix-based systems):
   ```text
    chmod +x CLI.py
### Usage Instructions

### Running the Application
Launch the application directly through the terminal:

    ./CLI.py

## Interactive Commands

Once running, the CLI prompt will await instructions:

* Enter any valid mathematical string expression to evaluate it.

* Type g to display the interactive runtime User Guide.

* Type e to terminate the session and exit the program.

### Example Session Trace
```text
--- Universal CLI Calculator --- 

This calculator evaluates arithmetic expressions and selected advanced math functions.
You can combine arithmetic and functions in one expression.
Allowed operators: +, -, *, /
Allowed functions: sqrt, sin, cos, tan, log, pow, abs, round, pi
Example: 5+3*(sqrt(81)/3)-2
Trigonometric functions use radians, not degrees.
You can use pi in expressions, such as sin(pi/2), cos(pi), or tan(pi/4).

Enter expression, g for guide, or e to exit: 5 + 3 * (sqrt(81) / 3) - 2
Result: 12.0

Enter expression, g for guide, or e to exit: pow(2, 3) + log(1)
Result: 8.0

Enter expression, g for guide, or e to exit: 5/0
Undefined: division by zero is not allowed.

Enter expression, g for guide, or e to exit: sqrt(-9)
Negative numbers are not allowed inside sqrt.

Enter expression, g for guide, or e to exit: 5(3+2)
Missing operator. Use an operator between numbers and parentheses, like 5*(3+2), not 5(3+2).

Enter expression, g for guide, or e to exit: e
Exiting calculator...
