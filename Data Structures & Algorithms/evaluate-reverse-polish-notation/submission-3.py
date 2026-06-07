def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for char in tokens:
            print(f"Character is {char}")
            if is_number(char):
                print("Added to stack\n")
                stack.append(int(char))
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                print(f"Popped values {v1} and {v2}")
                if char == "+":
                    stack.append(v1+v2)
                elif char == "*":
                    stack.append(v1*v2)
                elif char == "-":
                    stack.append(v2-v1)
                elif char == "/":
                    stack.append(int(v2/v1))
            print(stack)
        
        return stack[-1]
        
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
print(sol.evalRPN(tokens))
