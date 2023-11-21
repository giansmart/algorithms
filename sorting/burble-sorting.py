
def burble_sort(numbers: list): # sort in ascend manner
    changes = True
    n_changes = 0
    numbers_sort = numbers.copy()
    while changes:
        numbers_size = len(numbers)
        n_changes = 0
        for i in range(numbers_size):
            print(f"i={i}")
            if i + 1 < numbers_size: #if there are a next element	
                if numbers_sort[ i ] > numbers_sort[ i + 1 ]:
                    temp_val = numbers_sort[ i ] 
                    numbers_sort[ i ]  = numbers_sort[ i + 1 ]
                    numbers_sort[ i + 1 ] = temp_val
                    
                    n_changes += 1
        if n_changes == 0:
            changes = False
                

    return numbers_sort
    

arr = [30]

print(burble_sort(arr))