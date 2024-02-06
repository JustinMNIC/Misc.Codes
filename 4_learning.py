def divide_by_two(num):
    return num / 2

def vreau_doar_sa_printez_ceva():
    print("\nMa gandesc la placinte cu brinza!\n")

def create_a_list_with_nums_in_a_range_devided_by_two(listtt):

    for num in listtt:
        vreau_doar_sa_printez_ceva()
        print(divide_by_two(num))
        
    print("\n yo, gata !")

create_a_list_with_nums_in_a_range_devided_by_two([1,2,3,4,5,6,7,8,9,10])