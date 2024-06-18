def check_string(given, prefix, suffix):
    return given.startswith(prefix) or given.endswith(suffix)

str1=input('Enter the string: ')
print(check_string(str1, 'h', 'i')) 
