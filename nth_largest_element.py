n = int(input("How many elements needs to add to list:"))
list1 = []
#inputting elements to list by user inputs
for i in range(0,n):
     elem = int(input("Enter list elements:"))
     list1.append(elem)
print("List before sorting!!!")
print(list1)
print("sorting the list without sort function")
for i in range(0,n):
   for j in range(i+1,n):
         if list1[i]>list1[j]:
             temp = list1[i]
             list1[i]=list1[j]
             list1[j]=temp
print(" Sorted list:",list1)
m = int(input("Enter value for m largest in the list(choose a value less than n):"))
list2=[]
for i in range(0,m):
     large = 0
     for j in range(len(list1)):
         if list1[j]>large:
            large =list1[j]
     list1.remove(large)
     list2.append(large)
print(m,"th largest elements of list will be:",list2)

 
