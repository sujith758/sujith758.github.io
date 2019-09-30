#Bubble sorting a list
list = [10,15,4,23,0]
i = 0
#Nested loops for swapping and arranging numbers in list
for i in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            list[i],list[i+1]= list[i+1],list[i]
print(list)
