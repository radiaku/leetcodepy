def binary_search(data, target):
    low = 0
    high = len(data) - 1
    datacleaning = sorted(set(data), key = lambda ele: data.count(ele))
    datacleaning.sort()

    print(f"data: {data}")
    print(f"cleandata : {datacleaning}")
    
    while low <= high:
        middle = (low + high ) // 2
        
        if datacleaning[middle] == target: 
            return middle
        
        elif datacleaning[middle] > target:
            high = middle - 1
        else:
            low = middle + 1

    return -1

print(binary_search([1,2, 4, 7, 9, 3, 5, 11, 12 ,2, 3, 4, 14 , 17, 18], 11))    
    

