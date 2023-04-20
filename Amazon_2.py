class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert(root, item):
    temp = ListNode()
    temp.val = item
    temp.next = None
    if root == None:
        root = temp
    else:
        ptr = root
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = temp
    return root

def print_list(root):
    while root != None:
        print(root.val, end=" ")
        root = root.next

def array_to_list(arr):
    root = None
    for i in range(len(arr)):
        root = insert(root, arr[i])
    return root

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    carry = 0
    cur = dummy
    while l1 or l2 or carry:
        s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry = s // 10
        cur.next = ListNode(s % 10)
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

root1 = array_to_list(a)
root2 = array_to_list(b)
root3 = addTwoNumbers(root1, root2)
print_list(root3)