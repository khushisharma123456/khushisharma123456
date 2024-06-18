str1= input('Enter the first string: ')
str2= input('Enter the second string: ')

if sorted(str1)==sorted(str2):
    print('The strings are anagrams of each other.')
else:
    print('The strings are not anagrams of each other.')
