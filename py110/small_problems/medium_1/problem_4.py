# n: Place an integer value, n, in the register. Do not modify the stack.
# PUSH : Push the current register value onto the stack. Leave the value in the register.
# ADD : Pop a value from the stack and add it to the register value, storing the result in the register.
# SUB : Pop a value from the stack and subtract it from the register value, storing the result in the register.
# MULT : Pop a value from the stack and multiply it by the register value, storing the result in the register.
# DIV : Pop a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.
# REMAINDER : Pop a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.
# POP : Remove the topmost item from the stack and place it in the register.
# PRINT : Print the register value.

# integer_dict = {
#     "0": 0,
#     "1": 1, 
#     "2": 2,
#     "3": 3,
#     "4": 4,
#     "5": 5,
#     "6": 6,
#     "7": 7,
#     "8": 8,
#     "9": 9
# }

def minilang(program):
    stack = []
    register = 0

    for token in program.split():
        match token:
            case "ADD":
                register += stack.pop()
            case "DIV":
                register //= stack.pop()
            case "MULT":
                register *= stack.pop()
            case "REMAINDER":
                register %= stack.pop()
            case "SUB":
                register -= stack.pop()
            case "PUSH":
                stack.append(register)
            case "POP":
                register = stack.pop()
            case "PRINT":
                print(register)
            case _:
                register = int(token)

    return register


minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# # 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # 5
# # 3
# # 8

minilang('5 PUSH POP PRINT')
# # 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# # 12

minilang('-3 PUSH 5 SUB PRINT')
# # 8

minilang('6 PUSH')
# # (nothing is printed)
