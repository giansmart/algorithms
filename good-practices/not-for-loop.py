import time
from itertools import accumulate

# Use List Comprehension / Generator Expression

def is_prime(number):
    sequence = list(range(2, number))
    divisible_numbers = [ seq for seq in sequence if number % seq == 0]
    return True if len(divisible_numbers) == 0 else False

def is_prime_for(number):
    sequence = list(range(2, number))
    divisible_numbers = []
    for seq in sequence:
        if number % seq == 0:
            divisible_numbers.append(seq)
            break
    return True if len(divisible_numbers) == 0 else False

def use_map():
    my_list = list(range(1, 5))
    double_list = list(map(lambda x: x * 2, my_list))
    print(double_list)

def multiple_list_comprehension():
    result = [(i,j)
              for i in list(range(0,5))
              for j in list(range(0,3))]
    print(result)

# start_time = time.time()
# print(is_prime(43245311))
# end_time = time.time()
# print(f'{end_time - start_time} seconds')

# start_time = time.time()
# print(is_prime_for(43245311))
# end_time = time.time()
# print(f'{end_time - start_time} seconds')



multiple_list_comprehension()