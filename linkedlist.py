class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def make_list(self):
        node_list = []
        current = self.head_node
        while current:
            node_list.append(current.get_value())
            current = current.get_next_node()
        return node_list


node1 = LinkedList(5)
node1.insert_beginning(4)
node1.insert_beginning(3)
node1.insert_beginning(2)
node1.insert_beginning(1)


print(node1.make_list())
