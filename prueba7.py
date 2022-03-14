
def sum_two_smallest_numbers(numbers):
    lista=[]
    inicial=max(numbers)
    for i in numbers:        
        if i<inicial:
            inicial=i
    lista.append(inicial)
    numbers.pop(numbers.find(inicial))
    return lista




lista=[10,23,4,5,6,7,8,10,20,1]

print(sum_two_smallest_numbers(lista))