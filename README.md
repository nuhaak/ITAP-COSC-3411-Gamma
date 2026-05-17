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
Function / ConstantDescriptionExample InputExpected OutputpiThe constant ratio $\pi \approx 3.14159265...$pi3.141592653589793sqrt(x)Square root ($\sqrt{x}$). Domain: $x \ge 0$sqrt(81)9.0pow(x, y)Power function ($x^y$)pow(2, 3)8.0log(x)Natural logarithm ($\ln x$). Domain: $x > 0$log(pi)1.1447298858494002sin(x)Sine function (input in radians)sin(pi / 2)1.0cos(x)Cosine function (input in radians)cos(pi)-1.0tan(x)Tangent function (input in radians)tan(pi / 4)0.9999999999999999abs(x)Absolute value ($x$)round(x, [n])Rounds $x$ to nearest integer or $n$ decimal placesround(4.57, 1)4.6





   
