def cel_to_fahr(cel):
    return (cel * 9/5) + 32

def fahr_to_cel(fahr):
    return (fahr - 32) * 5/9

convert=input('Type F for final temperature in fahrenheit or type C for vice vesra: ')
temp=float(input('Enter the temperature: '))
if convert == 'F':
    print('The desired answer is: ',cel_to_fahr(temp))
else:
    print('The desired answer is: ',fahr_to_cel(temp))
