count = 0
for number in range(1,4):
    count = count + number
print(count)



def sum_list(my_list):
    count = 0
    for number in my_list:
        count = count + number
    return count

assert sum_list([1,2,3]) == 6
    
