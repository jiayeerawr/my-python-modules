import math
import LinearStructures

data_list = []
for p in xrange(6):
    data_list.append(p)

print data_list

my_list = LinearStructures.LinkedList()
my_list.print_list()
my_list.append(data_list[1])
my_list.print_list()
my_list.prepend(data_list[0])
my_list.print_list()
my_list.set_head(LinearStructures.ListNode(data_list[1]))
my_list.print_list()
my_list.append(data_list[2])
my_list.print_list()
my_list.append(data_list[3])
my_list.print_list()
my_list.insert(1, data_list[4])
my_list.print_list()
my_list.insert(2, data_list[5])
my_list.print_list()
my_list.insert(3, data_list[0])
my_list.print_list()
my_list.insert(0, data_list[0])
my_list.print_list()
my_list.delete_first()
my_list.print_list()
my_list.delete_last()
my_list.print_list()
my_list.delete_at(1)
my_list.print_list()
my_list.insert(0, data_list[0])
my_list.print_list()
my_list.delete(0, True, True)
my_list.print_list()
my_list.delete(2)
my_list.print_list()
