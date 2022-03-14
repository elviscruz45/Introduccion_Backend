def sum_two_smallest_numbers(numbers):
    number=numbers #lol
    number.sort(reverse=True)
    a=number.pop()
    b=number.pop()
    return a+b


lista=[10,23,2,5,6,7,8,10,20,1]

print(sum_two_smallest_numbers(lista))