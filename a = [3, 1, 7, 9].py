a = [3, 1, 7, 9]
b = [2, 4, 1, 9, 3]
    for num in (a, b):
if a != b:
  distinct_elements.add(num)
    
    return sum(distinct_elements)


result = sum_of_distinct_elements_between_arrays(a, b)
print("Sum of distinct elements between arrays:", result)
