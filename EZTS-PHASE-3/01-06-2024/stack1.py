# def is_palindrome(s):
#     stack = []
#     for char in s:
#         stack.append(char)
# 
#     reversed_s = ''
#     while stack:
#         reversed_s += stack.pop()
#     if s == reversed_s:
#         return "palindrome"
#     else:
#         return "not palindrome"
# 
# input_string = input("Enter a string: ")
# output = is_palindrome(input_string)
# print ( output)


# s=input()
# stack=list(s)
# for i in s:
#     if stack.pop()!=i:
#         print("Not a Palindrome")
#         break
# else:
#     print("Palindrome")

# # valid paranthesis
# s=input()
# stack = []
# opening_brackets = "([{"
# closing_brackets = ")]}"
# bracket_pairs = {")": "(", "]": "[", "}": "{"}
# 
# for char in s:
#     if char in opening_brackets:
#         stack.append(char)
#     elif char in closing_brackets:
#         if not stack or stack[-1] != bracket_pairs[char]:
#             print("n")
#         stack.pop()
#     else:
#         print("n")
# if len(stack) == 0:
#     print("t")

# stack=[]
# s=input()
# n=len(s)-1
# #print(n)
# flag=0
# if (s[0]==']' or s[0]=='}' or s[0]==')') or len(s)%2!=0:
#     print(False)
#     flag=0
# else:
#     for i in range(n+1):
#         if s[i]=='[' or s[i]=='(' or s[i]=='{':
#             stack.append(s[i])
#             flag+=1
#         elif s[i]==']' or s[i]=='}' or s[i]==')':
#             if (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']') or (stack[-1]=='(' and s[i]==')'):
#                 stack.pop()
#                 flag-=1
#             else:
#                 flag+=1
#                 break
#         else:
#             flag=-1
#             break
#     if flag==0:
#         print(True)
#     else:
#         print(False)



# def next_greater_number(digits):
#     n = len(digits)
#     i = n - 2
#     while i >= 0 and digits[i] >= digits[i + 1]:
#         i -= 1
#     if i == -1:
#         return digits
#     
#     j = n - 1
#     while digits[j] <= digits[i]:
#         j -= 1
#     
#     digits[i], digits[j] = digits[j], digits[i]
#     digits = digits[:i + 1] + digits[i + 1:][::-1]
#     
#     return ''.join(map(str, digits))
# t = int(input().strip())
# results = []
# 
# for _ in range(t):
#     n = int(input().strip())
#     digits = list(map(int, input().strip().split()))
#     result = next_greater_number(digits)
#     results.append(result)
# 
# for res in results:
#     print(res)


# class Solution:
#     def calPoints(self, operations):
#         resStack = []
#         for op in operations:
#             if not op.isdigit() and op[0] != '-':
#                 if op == 'D':
#                     resStack.append(2 * resStack[-1])
#                 elif op == '*':
#                     resStack.append(resStack[-1] * resStack[-2])
#                 elif op == 'C':
#                     resStack.pop()
#             else:
#                 resStack.append(int(op))
#         return sum(resStack)
# 
# s = Solution()
# print (s.calPoints(['5', '2', 'C', 'D', '*']))


