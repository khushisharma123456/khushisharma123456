lst=[]
print('Enter the list of numbers: ')
for i in range(0,num):
    ele = int(input(''))
    lst.append(ele)
print('The list is: ',lst)

maximim=max(lst)
minimum=min(lst)
print('The maximum value in the list is: ',str(maximim))
print('The minimum value in the list is: ',str(minimum))
