class Solution:
    def minLength(self, s: str) -> int:
        stk = []  # Start with an empty list as the stack
        for c in s:
            # Check for "AB" or "CD" pairs with the last character in the stack
            if (c == "B" and stk and stk[-1] == "A") or (c == "D" and stk and stk[-1] == "C"):
                stk.pop()  # Remove the last character if it forms a pair
            else:
                stk.append(c)  # Otherwise, add the current character to the stack
        return len(stk)