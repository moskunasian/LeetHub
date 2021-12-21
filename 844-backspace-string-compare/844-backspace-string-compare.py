class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # whenever we have nonbackspace push to stack
        # if we hit a backspace pop from stack
        
        def processStr(string, stack):
            for char in string:
                if char != '#':
                    stack.append(char)
                elif char == '#' and stack:
                    stack.pop()
            return stack
            
        
        return processStr(s, []) == processStr(t, [])
        
        