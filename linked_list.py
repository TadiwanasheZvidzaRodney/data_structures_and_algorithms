print('hey there, Menace!')


class Node:
    def __init__(self, data=None, next_element=None):
        self.data = data
        self.next_element = next_element


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return

        iterator = self.head
        linked_list_string = ''
        while iterator:
            linked_list_string += str(iterator.data) + '-->'
            iterator = iterator.next_element
        print(linked_list_string)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        iterator = self.head
        while iterator.next_element:
            iterator = iterator.next_element

        iterator.next_element = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        counter = 0
        iterator = self.head
        while iterator:
            counter += 1
            iterator = iterator.next_element
        return counter

    def remove_element(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next_element
            return

        counter = 0
        iterator = self.head
        while iterator:
            if counter == index - 1:
                iterator.next_element = iterator.next_element.next_element
                break
            iterator = iterator.next_element
            counter += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('invalid index')

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                node = Node(data, iterator.next_element)
                iterator.next_element = node
                break
            iterator = iterator.next_element
            count += 1


if __name__ == '__main__':
    linked_list = LinkedList()
    # linked_list.insert_at_beginning(3)
    # linked_list.insert_at_beginning(6)
    # linked_list.insert_at_beginning(9)
    # linked_list.insert_at_end(12)
    # linked_list.insert_at_end(15)
    # linked_list.insert_at_end(18)
    linked_list.insert_values([21, 24, 27])
    linked_list.print()
    print('length:', linked_list.get_length())
    linked_list.remove_element(1)
    # linked_list.remove_element(10)    # raises an exception "invalid index"
    linked_list.print()
    print('length:', linked_list.get_length())
    linked_list.insert_at(0, 9)
    linked_list.print()
    print('length:', linked_list.get_length())
    linked_list.insert_at(1, 12)
    linked_list.print()
    print('length:', linked_list.get_length())
