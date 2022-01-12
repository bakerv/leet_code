import collections


class Solution:
    def isValid(self, s: str) -> bool:
        # empty stack to monitor the required bracket sequence
        symbol_stack = collections.deque()
        for symbol in s:
            # for each opening backet, add the required closing bracket to the stack
            if symbol == '(':
                symbol_stack.append(')')
            elif symbol == '{':
                symbol_stack.append('}')
            elif symbol == '[':
                symbol_stack.append(']')

            # verify the correct closing bracket is being used
            else:
                try:
                    required_symbol = symbol_stack.pop()
                    if required_symbol != symbol:
                        return False
                except:
                    return False
        # return the truthfullness that all brackets have been closed
        return len(symbol_stack) == 0