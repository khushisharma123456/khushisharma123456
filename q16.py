a= input("ener string: ")
freq = []
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print(str(freq))
