list = ["Red","Green","White","Black","Pink","Yellow"]

#method 1:-
# for index,item in enumerate(list):
#     if index not in (0,4,5):
#         print("{0} : {1}".format(index,item))

#method 2:-
list = [item for (index,item) in enumerate(list) if index not in (0,4,5)]
print(list)