class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, other):
        dummy = Node(0)
        tail = dummy
        a, b = self.head, other.head

        while a and b:
            if a.value <= b.value:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        if a:
            tail.next = a
        if b:
            tail.next = b

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

    def insertion_sort(self):
        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            if not sorted_list or sorted_list.value >= current.value:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next and temp.next.value < current.value:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node

        self.head = sorted_list

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(4)
    list1.append(2)
    list1.append(1)
    list1.append(3)

    print("Оригінальний список:")
    list1.print_list()

    list1.reverse()
    print("Реверсований список:")
    list1.print_list()

    list1.insertion_sort()
    print("Відсортований список:")
    list1.print_list()

    list2 = LinkedList()
    list2.append(5)
    list2.append(6)
    list2.append(7)

    merged_list = list1.sorted_merge(list2)
    print("Об'єднаний відсортований список:")
    merged_list.print_list()
