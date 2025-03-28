OPERATORS = "+-*/"

def precedence(op):
    if op in "*/":
        return 2
    elif op in "+-":
        return 1
    return 0

def prefix_to_infix(sequence: str) -> str:
    stack = []
    for token in reversed(sequence):
        if token in OPERATORS:
            operand1 = stack.pop()
            operand2 = stack.pop()

            if isinstance(operand1, tuple):
                op1, prec1 = operand1
                if precedence(token) > prec1:
                    operand1_str = f"({op1})"
                else:
                    operand1_str = op1
            else:
                operand1_str = operand1

            if isinstance(operand2, tuple):
                op2, prec2 = operand2
                if precedence(token) > prec2 or (token in "-/" and precedence(token) == prec2):
                    operand2_str = f"({op2})"
                else:
                    operand2_str = op2
            else:
                operand2_str = operand2

            new_expr = f"{operand1_str}{token}{operand2_str}"
            stack.append((new_expr, precedence(token)))
        else:
            stack.append(token)

    result = stack.pop()
    return result[0] if isinstance(result, tuple) else result

if __name__ == '__main__':
    s = input().strip()
    print(prefix_to_infix(s))
