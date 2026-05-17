#!/usr/bin/python
import math
import re

# -----------Arithmetic ---------------

#Handles basic arithmetic operations: addition, subtraction, multiplication, and division.
def calculate_add(*numbers):
    return sum(numbers)

def calculate_subtract(*numbers):
    if not numbers:
        return 0

    result = numbers[0]

    for n in numbers[1:]:
        result -= n

    return result

def calculate_multiply(*numbers):
    result = 1

    for n in numbers:
        result *= n

    return result

def calculate_divide(*numbers):
    if not numbers:
        return 0

    result = numbers[0]

    for n in numbers[1:]:
        if n == 0:
            return "Cannot divide by zero"

        result /= n

    return result

# Choose the correct arithmetic operation based on the operator.
def arithmetic_function(operator, *numbers):
    if operator == "+":
        return calculate_add(*numbers)

    elif operator == "-":
        return calculate_subtract(*numbers)

    elif operator == "*":
        return calculate_multiply(*numbers)

    elif operator == "/":
        return calculate_divide(*numbers)

    else:
        return "Invalid operator"

# --------- Advanced Functions ----------

# Choose the correct advanced math function based on the function name.
def advanced_function(function_name, *args):

    if function_name == "sqrt":
        return safe_sqrt(args[0])

    elif function_name == "sin":
        return math.sin(args[0])

    elif function_name == "cos":
        return math.cos(args[0])

    elif function_name == "tan":
        return math.tan(args[0])

    elif function_name == "log":
        return math.log(args[0])

    elif function_name == "pow":
        return math.pow(args[0], args[1])

    elif function_name == "abs":
        return abs(args[0])

    elif function_name == "round":
        return round(args[0])

    else:
        return "Invalid function"
    
# Calculate square root, but reject negative inputs.
def safe_sqrt(x):
    if x < 0:
        raise ValueError("sqrt_negative")

    return math.sqrt(x)

# Calculate natural log, but reject zero and negative inputs.
def safe_log(x):
    if x <= 0:
        raise ValueError("log_not_positive")

    return math.log(x)

# ------------ Input Parsing, Validation & Error Handling --------
ALLOWED_FUNCTIONS = ["sqrt", "sin", "cos", "tan", "log", "pow", "abs", "round", "pi"]


# Check that the user typed something, not just spaces.
def is_not_empty(expression):
    if expression is None:
        return False

    if expression.strip() == "":
        return False
    
    return True

# Check that the expression only contains valid calculator characters.
def has_only_allowed_characters(expression):
    pattern = r"^[0-9a-zA-Z.()+*/,\s-]+$"

    if re.match(pattern, expression):
        return True
    else:
        return False

# Check that any typed word is an allowed math function.
def has_only_allowed_function_names(expression):
    words = re.findall(r"[a-zA-Z]+", expression)

    for word in words:
        if word not in ALLOWED_FUNCTIONS:
            return False

    return True

# Check that function names are followed by parentheses.
# pi is skipped because it is a constant, not a function.
def functions_are_followed_by_parenthesis(expression):
    words = re.finditer(r"[a-zA-Z]+", expression)

    for match in words:
        function_name = match.group()

        if function_name == "pi":
            continue

        if function_name in ALLOWED_FUNCTIONS:
            after_function = expression[match.end():]

            if not re.match(r"\s*\(", after_function):
                return False

    return True

# Check that every opening parenthesis has a matching closing parenthesis.
def has_balanced_parentheses(expression):
    counter = 0

    for char in expression:
        if char == "(":
            counter = counter + 1
        elif char == ")":
            counter = counter - 1

        if counter < 0:
            return False

    return counter == 0

# Check that pi is not used like a function.
def has_no_constant_as_function(expression):
    e = re.sub(r"\s+", "", expression)

    if re.search(r"\bpi\(", e):
        return False

    return True

# Check that the expression does not contain empty parentheses like ().
def has_no_empty_parentheses(expression):
    e = re.sub(r"\s+", "", expression)

    if re.search(r"\(\)", e):
        return False

    return True

# Check that an operator does not appear right before a closing parenthesis.
def has_no_operator_before_closing_parenthesis(expression):
    e = re.sub(r"\s+", "", expression)

    if re.search(r"[-+*/]\)", e):
        return False

    return True

# Check that the expression does not start or end with an incorrect operator.
def has_valid_start_and_end(expression):
    e = re.sub(r"\s+", "", expression)

    if re.search(r"^[+*/]", e):
        return False

    if re.search(r"[-+*/]$", e):
        return False

    return True

# Check that operators are not placed together incorrectly.
def has_no_invalid_operator_sequence(expression):
    e = re.sub(r"\s+", "", expression)

    if re.search(r"[-+*/][+*/]", e):
        return False

    return True

# Check for missing operators, such as 5(4), )5, or )(.
def has_no_missing_operator(expression):
    e = re.sub(r"\s+", "", expression)

    if re.search(r"\d\(", e):
        return False

    if re.search(r"\)[0-9(]", e):
        return False

    return True

# Run all validation checks before calculation.
def validate_expression(expression):
    if not is_not_empty(expression):
        return False

    if not has_only_allowed_characters(expression):
        return False

    if not has_only_allowed_function_names(expression):
        return False

    if not functions_are_followed_by_parenthesis(expression):
        return False

    if not has_balanced_parentheses(expression):
        return False
    
    if not has_no_constant_as_function(expression):
        return False

    if not has_no_empty_parentheses(expression):
        return False

    if not has_no_operator_before_closing_parenthesis(expression):
        return False

    if not has_valid_start_and_end(expression):
        return False

    if not has_no_invalid_operator_sequence(expression):
        return False

    if not has_no_missing_operator(expression):
        return False

    return True

# Return a clear error message when validation fails.
def get_validation_error(expression):
    if not is_not_empty(expression):
        return "Input cannot be empty."

    if not has_only_allowed_characters(expression):
        return "Expression contains unsupported characters. Use numbers, operators, parentheses, commas, and allowed function names only."

    if not has_only_allowed_function_names(expression):
        return "Incorrect function name. Allowed functions are: sqrt, sin, cos, tan, log, pow, abs, round."

    if not functions_are_followed_by_parenthesis(expression):
        return "Function names must be followed by parentheses, like sqrt(9), not sqrt 9 or sqrt9."

    if not has_balanced_parentheses(expression):
        return "Parentheses are not balanced. Make sure every '(' has a matching ')'."

    if not has_no_constant_as_function(expression):
        return "pi is a constant, not a function. Use pi, not pi()."

    if not has_no_empty_parentheses(expression):
        return "Empty parentheses are not allowed."

    if not has_no_operator_before_closing_parenthesis(expression):
        return "Incorrect operator placement. An operator cannot come right before a closing parenthesis."

    if not has_valid_start_and_end(expression):
        return "Incorrect operator placement. The expression cannot start with +, *, or /, and cannot end with an operator."

    if not has_no_invalid_operator_sequence(expression):
        return "Incorrect operator sequence. Operators like +*, /*, or ** are not allowed."

    if not has_no_missing_operator(expression):
        return "Missing operator. Use an operator between numbers and parentheses, like 5*(3+2), not 5(3+2)."

    return "Invalid expression."

# -------- Evaluation -------------
def evaluate_expression(expression):
    allowed_items = {

        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "pow": math.pow,
        "abs": abs,
        "round": round,
        "sqrt": safe_sqrt,
        "log": safe_log,
        "pi": math.pi
    }

    result = eval(expression, {"__builtins__": None}, allowed_items)

    return result

# ----------- Intro and Guide -----------
def print_intro():
    print("--- Universal CLI Calculator --- \n")
    print("This calculator evaluates arithmetic expressions and selected advanced math functions.")
    print("You can combine arithmetic and functions in one expression.")
    print("Allowed operators: +, -, *, /")
    print("Allowed functions: sqrt, sin, cos, tan, log, pow, abs, round, pi")
    print("Example: 5+3*(sqrt(81)/3)-2")
    print("Trigonometric functions use radians, not degrees.")
    print("You can use pi in expressions, such as sin(pi/2), cos(pi), or tan(pi/4).")

def print_guide():
    print("\n--- Calculator Guide ---")

    print("How to use:")
    print("Enter a math expression directly.")
    print("Type g to open this guide.")
    print("Type e to exit the calculator.\n")

    print("1. Basic arithmetic:")
    print("   Example: 5+3")
    print("   Example: 5+3*8")
    print("   Example: (5+3)*2\n")

    print("2. Allowed operators:")
    print("   + for addition")
    print("   - for subtraction")
    print("   * for multiplication")
    print("   / for division\n")

    print("3. Parentheses:")
    print("   Use parentheses to control order of operations.")
    print("   Correct: (5+3)*2")
    print("   Incorrect: (5+3")
    print("   Incorrect: 5(3+2)")
    print("   Use 5*(3+2) instead.\n")

    print("4. Allowed functions:")
    print("   sqrt(x)   square root")
    print("   sin(x)    sine")
    print("   cos(x)    cosine")
    print("   tan(x)    tangent")
    print("   log(x)    natural logarithm")
    print("   pow(x,y)  power")
    print("   abs(x)    absolute value")
    print("   round(x)    rounds to the nearest whole number")
    print("   round(x,n)  rounds to n decimal places\n")

    print("5. Function format:")
    print("   Function names must be followed by parentheses.")
    print("   Correct: sqrt(9)")
    print("   Correct: pow(2,3)")
    print("   Incorrect: sqrt 9")
    print("   Incorrect: sqrt9")
    print("   Note: Python may round .5 values to the nearest even number.")
    print("   Example: round(4.5) gives 4, but round(5.5) gives 6.\n")

    print("6. Trigonometric functions:")
    print("   sin, cos, and tan use radians, not degrees.")
    print("   You can use pi in expressions.")
    print("   Example: sin(pi/2)")
    print("   Example: cos(pi)")
    print("   Example: tan(pi/4)\n")

    print("7. pi:")
    print("   pi is a constant.")
    print("   Correct: pi")
    print("   Correct: 2*pi")
    print("   Correct: sin(pi/2)")
    print("   Incorrect: pi()\n")

    print("8. Math restrictions:")
    print("   Division by zero is undefined.")
    print("   Incorrect: 5/0")
    print("   Incorrect: 0/0")
    print("   sqrt cannot take a negative number in this calculator.")
    print("   Incorrect: sqrt(-9)")
    print("   log input must be greater than 0.")
    print("   Incorrect: log(0)")
    print("   Incorrect: log(-5)")

# ----------- Main -----------

# Start the calculator and handle user input.
def main():
    print_intro()

    while True:
        user_input = input("\nEnter expression, g for guide, or e to exit: ").strip()

        if user_input.lower() == "e":
            print("Exiting calculator...")
            break

        elif user_input.lower() == "g":
            print_guide()

        else:
            expression = user_input

            # Validate the expression before trying to calculate it.
            if validate_expression(expression):
                try:
                    result = evaluate_expression(expression)
                    print("Result:", result)

                except ZeroDivisionError:
                    print("Undefined: division by zero is not allowed.")

                except ValueError as e:
                    if str(e) == "sqrt_negative":
                        print("Negative numbers are not allowed inside sqrt.")

                    elif str(e) == "log_not_positive":
                        print("Log input must be greater than 0.")

                    else:
                        print("Math domain error.")

                except Exception:
                    print("Invalid expression.")

            else:
                print(get_validation_error(expression))
if __name__ == "__main__":
    main()
