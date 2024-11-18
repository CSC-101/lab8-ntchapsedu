#input is list of numbers
#output is list of lists each with three numbers except the last which could have 2 or 1
#while the list of nums is more than 3 make a new list and add the first num of list1 and then pop that num from list1
#do this 3 times and add that list to a new list, then continue doing this loop until the list1 is less than 3 nums
#if list1 is less than 3 nums just add the remaining nums to the new list
def groups_of_3(list1: list[int])->list[list[int]]:
    new_list = []
    while len(list1) > 3:
        temp = []
        for i in range(0,3):
            temp.append(list1[0])
            list1.pop(0)
        new_list.append(temp)
    new_list.append(list1)
    return new_list
