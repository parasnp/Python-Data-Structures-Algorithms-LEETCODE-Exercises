class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def find_kth_node_from_end(self, k):
        if k <= 0 or self.head is None:
            return None

        fast = self.head
        slow = self.head

        # Move the fast pointer k nodes ahead
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next

        # Move both pointers until the fast pointer reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow

# Example usage:
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 2
kth_node = my_linked_list.find_kth_node_from_end(k)

if kth_node:
    print(f"The {k}th node from the end is: {kth_node.value}")
else:
    print(f"There is no {k}th node from the end.")
