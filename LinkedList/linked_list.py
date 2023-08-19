from node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node

        elif self.head.value >= value:
            new_node.next = self.head
            self.head = new_node

        else:
            previous = self.head
            runner = self.head.next

            while((runner is not None) and(value > runner.value)):
                previous = runner
                runner = runner.next

            new_node.next = runner
            previous.next = new_node

    def print_list_items(self):
        if self.head is None:
            print("Empty List")
        else:
            runner = self.head
            while(runner is not None):
                print(runner.value, end = " ")
                runner = runner.next
            print()

    def count_nodes(self):
        count = 0
        if self.head is None:
            return 0
        else:
            runner = self.head
            while(runner is not None):
                count+=1
                runner = runner.next
        return count

    def find_node(self, value):
        if self.head is None:
            return False
        else:
            runner = self.head
            while (runner is not None):
                if runner.value == value:
                    return True
                    break
                else:
                    runner = runner.next
            return False

    def delete_node(self,value):
        if self.head is None:
            return ("Cannot Delete. List is Empty")
        elif (self.head.value == value):
            self.head = self.head.next
        else:
            previous = self.head
            runner = self.head.next
            while(runner is not None) and (value > runner.value) :
                previous = runner
                runner = runner.next

            if (runner is not None) and (value == runner.value) :
                previous.next = runner.next
                return True
            else:
                return False








