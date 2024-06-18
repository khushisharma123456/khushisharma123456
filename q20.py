num=int(input('Enter number of list elements: '))
lst1=[]
print('Enter the list of numbers: ')
for i in range(0,num):
    ele = int(input(''))
    lst1.append(ele)
print('The list is: ',lst1)
print('The sum of elements of the list is: ',sum(lst1))
