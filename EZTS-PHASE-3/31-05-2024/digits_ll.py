class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(num1, num2):
    digits1 = [int(d) for d in str(num1)][::-1]
    digits2 = [int(d) for d in str(num2)][::-1]

    carry = 0
    result_head = ListNode(0)
    current = result_head

    max_len = max(len(digits1), len(digits2))
    for i in range(max_len):
        d1 = digits1[i] if i < len(digits1) else 0
        d2 = digits2[i] if i < len(digits2) else 0
        total = d1 + d2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

    if carry:
        current.next = ListNode(carry)

    return result_head.next

def print_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(" -> ".join(map(str, values[::-1])))

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result = add_two_numbers(num1, num2)
print_list(result)
