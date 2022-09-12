
def test(first_list,second_list):
    sorted_first_list = sorted(first_list)
    sorted_second_list = sorted(second_list)
    blank_list = [None] * items_in_lists
    for item_in_one, item_in_two in zip(sorted_first_list,sorted_second_list):
        index_order = first_list.index(item_in_one)
        blank_list[index_order] = item_in_two

    for item in blank_list:
        print(item)

first = True
while True:
    items_in_lists = int(input())
    if items_in_lists == 0:
        break

    if not first:
        print("")
    else:
        first = False

    list_one = []
    list_two = []

    for x in range(items_in_lists):
        i = int(input())
        list_one.append(i)

    for x in range(items_in_lists):
        i = int(input())
        list_two.append(i)

    test(list_one,list_two)
    
























