from linked_list import LinkedList

linkilist = LinkedList()

linkilist.insert_node(4)
linkilist.insert_node(3)
linkilist.insert_node(5)
linkilist.insert_node(58)

linkilist.print_list_items()
print(linkilist.count_nodes())
print(linkilist.find_node(8))
linkilist.delete_node(7)
linkilist.print_list_items()

