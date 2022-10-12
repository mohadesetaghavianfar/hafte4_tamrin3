list1=[]
list2=[]
for i in range(10):
    arr=int(input('enter: '))
    list1.append(arr)
for i in range(len(list1)):

    for j in range(0 , len(list1)-i-1):

        if list1[j]>list1[j+1]:
            list1[j], list1[j+1]=list1[j+1],list1[j]

            
for i in range(len(list1)):
    list2.append(list1[i])
print(list2)