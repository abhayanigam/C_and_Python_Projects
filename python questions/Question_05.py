n = int(input("Enter the size :"))
arr = []
for i in range (0,n):
    element = int(input("Enter the element no. :"))
    arr.append(element)
print(arr)
arr_tuple = tuple(arr)
print(arr_tuple)
print(max(arr_tuple))
print(min(arr_tuple))