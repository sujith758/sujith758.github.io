#Binary search in a list
list = [19,88,5,33,4]
#Sorting a list--> If True list is sorted in desending order,If false in asending order
list.sort(reverse = False)
#Passing the key to start search
key = 3
#To access the left sublist
low = 0
#To accsess the right sublist
high = len(list)-1
found = False
#While loop until the key is found in the list
while low<=high and not found:
    #Finding mid element in list
    mid = (low+high)//2
    if key == list[mid]:
          found = True
    elif key > list[mid]:
          low = mid+1
    else:
          high = mid-1
if found == True:
        print("Key:",key,"found")
else:
        print("Key:",key,"not found")
