# Mathematical Expression Evaluator

This Python script evaluates mathematical expressions containing addition, subtraction, and parentheses. It handles both positive and negative numbers and supports nested parentheses. The solution uses a stack-based approach to process the expressions.

## Table of Contents
- [Description](#description)
- [Dependencies](#dependencies)
- [Code Explanation](#code-explanation)
- [Usage](#usage)
- [Example](#example)
- [Conclusion](#conclusion)

## Description

The script defines a class Solution with a method calculate that evaluates expressions in string format. It supports basic arithmetic operations (+, -) and nested parentheses. The script also includes a test function test_calculate to verify the correctness of the calculate method with various test cases.

## Dependencies

- Python 3.x

No external libraries are required for this script.

## Code Explanation

### 1. Define the Solution Class and calculate Method
```
class Solution:
    def calculate(self, s):
        stack = []
        current_number = 0
        result = 0
        sign = 1

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '+':
                result += sign * current_number
                current_number = 0
                sign = 1
            elif char == '-':
                result += sign * current_number
                current_number = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_number
                current_number = 0
                result *= stack.pop()
                result += stack.pop()

        result += sign * current_number
        return result
```
- Initialization:
  - stack: Used to store the intermediate results and signs.
  - current_number: Accumulates digits to form the current number.
  - result: Stores the ongoing result of the expression.
  - sign: Tracks the current sign (positive or negative).

- Processing Characters:
  - Digits: Accumulate into current_number.
  - **Operators (+, -):** Apply the current operation and reset current_number.
  - **Parentheses ((, )):** Use the stack to handle nested operations.

### 2. Test the calculate Method
```
def test_calculate():
    test_cases = {
        "1 + 1": 2,
        " 2-1 + 2 ": 3,
        "(1+(4+5+2)-3)+(6+8)": 23,
        "2-(5-6)": 3,
        "10 + (2 + 3) - (5 - 4)": 14,
        "(7+8)-(3-2)": 14,
        "((2+3)+4)": 9,
        "1-(-1)": 2
    }
    
    solution = Solution()
    
    for expression, expected in test_cases.items():
        result = solution.calculate(expression)
        print(f"Expression: {expression}\nExpected: {expected}, Got: {result}\n")

# Run the tests
test_calculate()
```
- **Test Cases:** Includes a variety of expressions to validate the calculation method.
- **Output:** Prints the result of each expression along with the expected result
## Usage

1. **Copy the Code:Copy the Code:** Place the code into a Python file (e.g., evaluate_expression.py).
2. **Run the Script:** Execute the script using Python:
  
   python evaluate_expression.py
   
3. **Check Results:** Observe the output to ensure the calculate method produces the expected results.

## Example

The script evaluates different mathematical expressions and verifies their correctness. For example:
- For the expression "1 + 1", the expected result is 2.
- For the expression "(1+(4+5+2)-3)+(6+8)", the expected result is 23.

## Conclusion

This script demonstrates a stack-based approach to evaluate mathematical expressions with nested parentheses. It provides a clear solution for handling basic arithmetic operations and verifying results with test cases.
