# Program 1:
n = int(input("How many elements needs to add to list:"))
list1 = []
# inputting elements to list by user inputs
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
print("After Sorting the list:",list1)
print("First Largest Element in the  List:",max(list1))
