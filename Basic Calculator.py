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

# Test the calculate function with different mathematical expressions
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